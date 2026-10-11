from app.utils.pdf_parser import extract_text_from_pdf
from app.utils.text_cleaner import clean_resume_text


pdf_path = "data/sample_resumes/sample.pdf"

raw_text = extract_text_from_pdf(pdf_path)
cleaned_text = clean_resume_text(raw_text)

print("===== CLEANED RESUME =====")
print(cleaned_text)