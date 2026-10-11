from app.nlp.job_matcher import calculate_skill_match
from app.nlp.skill_extractor import extract_skills
from app.nlp.text_matcher import calculate_text_similarity
from app.utils.pdf_parser import extract_text_from_pdf
from app.utils.text_cleaner import clean_resume_text
from app.utils.text_loader import load_text_file


RESUME_PATH = "data/sample_resumes/sample.pdf"

JOB_DESCRIPTION_PATH = (
    "data/sample_job_descriptions/data_scientist.txt"
)


def main():
    # -----------------------------------------
    # 1. Process Resume
    # -----------------------------------------

    raw_resume = extract_text_from_pdf(
        RESUME_PATH
    )

    cleaned_resume = clean_resume_text(
        raw_resume
    )

    resume_skills = extract_skills(
        cleaned_resume
    )

    # -----------------------------------------
    # 2. Process Job Description
    # -----------------------------------------

    job_description = load_text_file(
        JOB_DESCRIPTION_PATH
    )

    cleaned_job_description = clean_resume_text(
        job_description
    )

    job_skills = extract_skills(
        cleaned_job_description
    )

    # -----------------------------------------
    # 3. Skill Match
    # -----------------------------------------

    skill_result = calculate_skill_match(
        resume_skills,
        job_skills,
    )

    # -----------------------------------------
    # 4. Text Similarity
    # -----------------------------------------

    text_similarity = calculate_text_similarity(
        cleaned_resume,
        cleaned_job_description,
    )

    # -----------------------------------------
    # 5. Display Results
    # -----------------------------------------

    print("===== RESUME SKILLS =====")

    for skill in resume_skills:
        print(f"- {skill}")

    print("\n===== JOB SKILLS =====")

    for skill in job_skills:
        print(f"- {skill}")

    print("\n===== SKILL MATCH ANALYSIS =====")

    print("\nMatched Skills:")

    for skill in skill_result["matched_skills"]:
        print(f"✓ {skill}")

    print("\nMissing Skills:")

    for skill in skill_result["missing_skills"]:
        print(f"✗ {skill}")

    print(
        f"\nSkill Match: "
        f"{skill_result['match_percentage']}%"
    )

    print("\n===== TEXT SIMILARITY =====")

    print(
        f"Resume ↔ Job Description: "
        f"{text_similarity}%"
    )


if __name__ == "__main__":
    main()