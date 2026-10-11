from app.services.resume_service import analyze_resume


RESUME_PATH = (
    "data/sample_resumes/sample.pdf"
)


JOB_DESCRIPTION = """
Data Scientist

We are looking for a Data Scientist to join our team.

Requirements:

- Strong Python programming skills.
- Experience with SQL and PostgreSQL.
- Knowledge of Machine Learning and Deep Learning.
- Experience with Pandas, NumPy and scikit-learn.
- Experience with FastAPI for building APIs.
- Familiarity with Docker and AWS.
- Experience with Exploratory Data Analysis and Feature Engineering.
- Knowledge of Git and GitHub.
- Experience with Natural Language Processing is a plus.
"""


def main():

    result = analyze_resume(
        RESUME_PATH,
        JOB_DESCRIPTION,
    )


    print(
        "========================================"
    )

    print(
        "             RESUMEIQ ANALYSIS"
    )

    print(
        "========================================"
    )


    print("\n===== AI SUMMARY =====")

    print(
        result["summary"]
    )


    print("\n===== RESUME SKILLS =====")

    for skill in result["resume_skills"]:

        print(
            f"- {skill}"
        )


    print("\n===== JOB SKILLS =====")

    for skill in result["job_skills"]:

        print(
            f"- {skill}"
        )


    print("\n===== MATCHED SKILLS =====")

    for skill in result["matched_skills"]:

        print(
            f"✓ {skill}"
        )


    print("\n===== MISSING SKILLS =====")

    for skill in result["missing_skills"]:

        print(
            f"✗ {skill}"
        )


    print(
        "\nSkill Match: "
        f"{result['skill_match_percentage']}%"
    )


    print(
        "Text Similarity: "
        f"{result['text_similarity_percentage']}%"
    )


if __name__ == "__main__":
    main()