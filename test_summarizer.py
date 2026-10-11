from app.models.summarizer import summarize_resume
from app.utils.pdf_parser import extract_text_from_pdf
from app.utils.text_cleaner import clean_resume_text


RESUME_PATH = "data/sample_resumes/sample.pdf"


def main():
    # -----------------------------------------
    # 1. Extract Resume Text
    # -----------------------------------------

    raw_text = extract_text_from_pdf(
        RESUME_PATH
    )

    # -----------------------------------------
    # 2. Clean Resume Text
    # -----------------------------------------

    cleaned_text = clean_resume_text(
        raw_text
    )

    # -----------------------------------------
    # 3. Generate AI Summary
    # -----------------------------------------

    summary = summarize_resume(
        cleaned_text,
        max_new_tokens=100,
    )

    # -----------------------------------------
    # 4. Display Result
    # -----------------------------------------

    print(
        "===== AI GENERATED RESUME SUMMARY ====="
    )

    print()

    print(summary)


if __name__ == "__main__":
    main()