import pymupdf

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from all pages of a PDF resume.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        Combined text extracted from the PDF.
    """
    document = pymupdf.open(pdf_path)

    pages_text = []

    for page in document:
        text = page.get_text()
        pages_text.append(text)

    document.close()

    return "\n".join(pages_text)