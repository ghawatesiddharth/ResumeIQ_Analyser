from app.utils.pdf_parser import extract_text_from_pdf


pdf_path = "data/sample_resumes/sample.pdf"

resume_text = extract_text_from_pdf(pdf_path)

print(resume_text)