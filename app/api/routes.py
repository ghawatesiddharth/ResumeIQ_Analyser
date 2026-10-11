from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from app.services.resume_service import analyze_resume
from app.utils.pdf_parser import extract_text_from_pdf
from app.utils.text_cleaner import clean_resume_text


router = APIRouter()


MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB


@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "ResumeIQ API",
    }


@router.post("/analyze")
async def analyze(
    resume: UploadFile = File(...),
    job_description: str = Form(...),
):
    """
    Analyze an uploaded PDF resume against
    a user-provided job description.
    """

    # -----------------------------------------
    # Validate filename
    # -----------------------------------------

    if not resume.filename:
        raise HTTPException(
            status_code=400,
            detail="Please upload a resume PDF.",
        )

    # -----------------------------------------
    # Validate file extension
    # -----------------------------------------

    file_extension = Path(
        resume.filename
    ).suffix.lower()

    if file_extension != ".pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF resume files are supported.",
        )

    # -----------------------------------------
    # Validate job description
    # -----------------------------------------

    if not job_description.strip():
        raise HTTPException(
            status_code=400,
            detail="Please enter a job description.",
        )

    if len(job_description.strip()) < 30:
        raise HTTPException(
            status_code=400,
            detail=(
                "Job description is too short. "
                "Please provide a meaningful job description."
            ),
        )

    # -----------------------------------------
    # Read uploaded file
    # -----------------------------------------

    try:
        file_content = await resume.read()

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Unable to read the uploaded file.",
        )

    # -----------------------------------------
    # Validate file size
    # -----------------------------------------

    if not file_content:
        raise HTTPException(
            status_code=400,
            detail="The uploaded resume is empty.",
        )

    if len(file_content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail=(
                "Resume file is too large. "
                "Please upload a PDF smaller than 5 MB."
            ),
        )

    temporary_path = None

    try:

        # -------------------------------------
        # Save temporary PDF
        # -------------------------------------

        with NamedTemporaryFile(
            delete=False,
            suffix=".pdf",
        ) as temporary_file:

            temporary_file.write(
                file_content
            )

            temporary_path = temporary_file.name

        # -------------------------------------
        # Validate PDF content
        # -------------------------------------

        try:

            raw_resume = extract_text_from_pdf(
                temporary_path
            )

        except Exception:

            raise HTTPException(
                status_code=400,
                detail=(
                    "The uploaded file could not "
                    "be read as a valid PDF."
                ),
            )

        # -------------------------------------
        # Validate extracted text
        # -------------------------------------

        cleaned_resume = clean_resume_text(
            raw_resume
        )

        if not cleaned_resume:

            raise HTTPException(
                status_code=400,
                detail=(
                    "No readable text was found "
                    "in the resume. Please upload "
                    "a text-based PDF."
                ),
            )

        if len(cleaned_resume) < 100:

            raise HTTPException(
                status_code=400,
                detail=(
                    "The resume contains too little "
                    "readable text for analysis."
                ),
            )

        # -------------------------------------
        # Run ResumeIQ analysis
        # -------------------------------------

        result = analyze_resume(
            temporary_path,
            job_description,
        )

        return {
            "filename": resume.filename,
            "analysis": result,
        }

    except HTTPException:
        raise

    except Exception as error:

        print(
            f"Resume analysis error: {error}"
        )

        raise HTTPException(
            status_code=500,
            detail=(
                "Resume analysis failed. "
                "Please check the uploaded resume "
                "and job description and try again."
            ),
        )

    finally:

        # -------------------------------------
        # Delete temporary file
        # -------------------------------------

        if temporary_path:

            temporary_file_path = Path(
                temporary_path
            )

            if temporary_file_path.exists():

                temporary_file_path.unlink()