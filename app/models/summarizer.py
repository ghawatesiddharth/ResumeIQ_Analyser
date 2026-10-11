from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

from app.utils.resume_sections import extract_resume_sections


MODEL_NAME = "google-t5/t5-small"


# Load tokenizer and model once.
tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME
)


SUMMARY_SECTIONS = [
    "education",
    "technical skills",
    "projects",
    "leadership & activities",
    "achievements",
]


def summarize_text(
    text: str,
    max_new_tokens: int = 100,
) -> str:
    """
    Generate a summary for a piece of resume text.

    Args:
        text: Text to summarize.
        max_new_tokens: Maximum number of generated tokens.

    Returns:
        Generated summary.
    """

    if not text.strip():
        return ""

    prompt = "summarize: " + text

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        max_length=512,
        truncation=True,
    )

    outputs = model.generate(
        inputs["input_ids"],
        max_new_tokens=max_new_tokens,
        do_sample=False,
    )

    return tokenizer.decode(
        outputs[0],
        skip_special_tokens=True,
    )


def summarize_resume(
    text: str,
    max_new_tokens: int = 100,
) -> str:
    """
    Generate an AI-powered summary from the important
    sections of a resume.

    Contact information is excluded from summarization.

    Args:
        text: Cleaned resume text.
        max_new_tokens: Maximum generated tokens per section.

    Returns:
        Combined AI-generated resume summary.
    """

    if not text.strip():
        return ""

    sections = extract_resume_sections(text)

    summaries = []

    for section_name in SUMMARY_SECTIONS:

        section_content = sections.get(
            section_name,
            "",
        )

        if not section_content.strip():
            continue

        summary = summarize_text(
            section_content,
            max_new_tokens=max_new_tokens,
        )

        if summary:
            summaries.append(summary)

    return " ".join(summaries)