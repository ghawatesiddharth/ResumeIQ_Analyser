from app.utils.pdf_parser import extract_text_from_pdf
from app.utils.text_cleaner import clean_resume_text
from app.utils.text_chunker import chunk_text


RESUME_PATH = "data/sample_resumes/sample.pdf"


def main():
    raw_text = extract_text_from_pdf(
        RESUME_PATH
    )

    cleaned_text = clean_resume_text(
        raw_text
    )

    chunks = chunk_text(
        cleaned_text,
        words_per_chunk=300,
    )

    print("===== TEXT CHUNKING =====")

    print(
        f"Total chunks: {len(chunks)}"
    )

    for index, chunk in enumerate(
        chunks,
        start=1,
    ):
        print(
            f"\n--- Chunk {index} ---"
        )

        print(
            f"Word count: {len(chunk.split())}"
        )

        print(chunk)


if __name__ == "__main__":
    main()