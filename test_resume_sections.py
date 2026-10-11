from app.utils.pdf_parser import extract_text_from_pdf
from app.utils.resume_sections import extract_resume_sections
from app.utils.text_cleaner import clean_resume_text


RESUME_PATH = "data/sample_resumes/sample.pdf"


def main():
    raw_text = extract_text_from_pdf(
        RESUME_PATH
    )

    cleaned_text = clean_resume_text(
        raw_text
    )

    sections = extract_resume_sections(
        cleaned_text
    )

    print("===== RESUME SECTIONS =====")

    for section_name, content in sections.items():

        print(
            f"\n--- {section_name.upper()} ---"
        )

        print(content[:500])


if __name__ == "__main__":
    main()