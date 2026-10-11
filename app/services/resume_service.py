from app.models.summarizer import summarize_resume
from app.nlp.insights import generate_insights
from app.nlp.job_matcher import calculate_skill_match
from app.nlp.skill_extractor import extract_skills
from app.nlp.text_matcher import calculate_text_similarity
from app.utils.pdf_parser import extract_text_from_pdf
from app.utils.text_cleaner import clean_resume_text


def analyze_resume(
    resume_path: str,
    job_description: str,
) -> dict:
    """
    Run the complete ResumeIQ analysis pipeline
    using an uploaded resume and user-provided
    job description.
    """

    # ---------------------------------
    # Resume processing
    # ---------------------------------

    raw_resume = extract_text_from_pdf(
        resume_path
    )

    cleaned_resume = clean_resume_text(
        raw_resume
    )

    resume_skills = extract_skills(
        cleaned_resume
    )


    # ---------------------------------
    # Job description processing
    # ---------------------------------

    cleaned_job_description = clean_resume_text(
        job_description
    )

    job_skills = extract_skills(
        cleaned_job_description
    )


    # ---------------------------------
    # Skill matching
    # ---------------------------------

    skill_result = calculate_skill_match(
        resume_skills,
        job_skills,
    )


    # ---------------------------------
    # Text similarity
    # ---------------------------------

    text_similarity = calculate_text_similarity(
        cleaned_resume,
        cleaned_job_description,
    )


    # ---------------------------------
    # AI resume summary
    # ---------------------------------

    summary = summarize_resume(
        cleaned_resume
    )


    # ---------------------------------
    # Analysis insights
    # ---------------------------------

    insights = generate_insights(
        skill_result["match_percentage"],
        skill_result["matched_skills"],
        skill_result["missing_skills"],
        text_similarity,
    )


    # ---------------------------------
    # Final result
    # ---------------------------------

    return {
        "resume_skills": resume_skills,

        "job_skills": job_skills,

        "matched_skills": skill_result[
            "matched_skills"
        ],

        "missing_skills": skill_result[
            "missing_skills"
        ],

        "skill_match_percentage": skill_result[
            "match_percentage"
        ],

        "text_similarity_percentage": (
            text_similarity
        ),

        "summary": summary,

        "insights": insights,
    }