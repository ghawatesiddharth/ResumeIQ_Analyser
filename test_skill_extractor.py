from app.utils.pdf_parser import extract_text_from_pdf
from app.utils.text_cleaner import clean_resume_text
from app.nlp.skill_extractor import extract_skills


PDF_PATH = "data/sample_resumes/sample.pdf"


def main():
    # Step 1: Extract text from PDF
    raw_text = extract_text_from_pdf(PDF_PATH)

    # Step 2: Clean extracted text
    cleaned_text = clean_resume_text(raw_text)

    # Step 3: Extract canonical skills
    skills = extract_skills(cleaned_text)

    print("===== EXTRACTED SKILLS =====")

    for skill in skills:
        print(f"- {skill}")

    print(f"\nTotal skills found: {len(skills)}")


if __name__ == "__main__":
    main()