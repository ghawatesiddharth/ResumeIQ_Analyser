import re


def clean_resume_text(text: str) -> str:
    """
    Clean and normalize text extracted from a resume PDF.

    The function removes unnecessary whitespace while preserving
    meaningful resume information such as punctuation, numbers,
    dates, and technical terms.
    """

    # Normalize Windows-style line endings
    text = text.replace("\r\n", "\n")

    # Replace tabs with spaces
    text = text.replace("\t", " ")

    # Remove whitespace at the beginning/end of each line
    lines = [line.strip() for line in text.split("\n")]

    # Remove completely empty lines
    lines = [line for line in lines if line]

    # Rebuild the text
    text = "\n".join(lines)

    # Collapse repeated spaces inside lines
    text = re.sub(r"[ ]{2,}", " ", text)

    # Remove spaces before common punctuation
    text = re.sub(r"\s+([,.;:!?])", r"\1", text)

    return text.strip()