from app.models.qa_model import answer_question
from app.utils.pdf_parser import extract_text_from_pdf
from app.utils.text_cleaner import clean_resume_text


RESUME_PATH = (
    "data/sample_resumes/sample.pdf"
)


def main():

    raw_text = extract_text_from_pdf(
        RESUME_PATH
    )

    resume_text = clean_resume_text(
        raw_text
    )


    questions = [
        "What is the candidate's CGPA?",
        "What programming language does the candidate know?",
        "What projects has the candidate worked on?",
        "What database technologies are mentioned?",
    ]


    print(
        "========================================"
    )

    print(
        "          RESUMEIQ RESUME Q&A"
    )

    print(
        "========================================"
    )


    for question in questions:

        answer = answer_question(
            question,
            resume_text,
        )

        print(
            f"\nQuestion: {question}"
        )

        print(
            f"Answer: {answer}"
        )


if __name__ == "__main__":
    main()