from transformers import (
    AutoModelForQuestionAnswering,
    AutoTokenizer,
)

from app.utils.text_chunker import chunk_text


MODEL_NAME = "distilbert-base-cased-distilled-squad"


tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME
)

model = AutoModelForQuestionAnswering.from_pretrained(
    MODEL_NAME
)


def answer_question_from_context(
    question: str,
    context: str,
) -> tuple[str, float]:
    """
    Answer a question from one context chunk.

    Returns:
        answer, confidence score
    """

    inputs = tokenizer(
        question,
        context,
        return_tensors="pt",
        truncation=True,
        max_length=512,
    )

    outputs = model(**inputs)

    start_logits = outputs.start_logits[0]
    end_logits = outputs.end_logits[0]

    start_position = start_logits.argmax().item()
    end_position = end_logits.argmax().item()

    if end_position < start_position:
        return "", 0.0

    answer_tokens = inputs["input_ids"][
        0,
        start_position:end_position + 1,
    ]

    answer = tokenizer.decode(
        answer_tokens,
        skip_special_tokens=True,
    ).strip()

    start_score = start_logits[
        start_position
    ].item()

    end_score = end_logits[
        end_position
    ].item()

    confidence = (
        start_score + end_score
    ) / 2

    return answer, confidence


def answer_question(
    question: str,
    context: str,
) -> str:
    """
    Answer a question using multiple resume chunks.
    """

    if not question.strip():
        return "Please provide a question."

    if not context.strip():
        return "No resume context is available."

    chunks = chunk_text(
        context,
        words_per_chunk=180,
    )

    best_answer = ""
    best_confidence = float("-inf")


    for chunk in chunks:

        answer, confidence = (
            answer_question_from_context(
                question,
                chunk,
            )
        )

        if not answer:
            continue

        if confidence > best_confidence:

            best_answer = answer
            best_confidence = confidence


    if not best_answer:
        return (
            "I could not find an answer "
            "in the resume."
        )

    return best_answer