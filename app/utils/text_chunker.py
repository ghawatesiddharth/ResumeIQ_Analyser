def chunk_text(
    text: str,
    words_per_chunk: int = 300,
) -> list[str]:
    """
    Split text into manageable word-based chunks.

    Args:
        text: Input text.
        words_per_chunk: Maximum approximate number
            of words in each chunk.

    Returns:
        List of text chunks.
    """

    words = text.split()

    chunks = []

    for start in range(
        0,
        len(words),
        words_per_chunk,
    ):
        chunk = " ".join(
            words[start:start + words_per_chunk]
        )

        if chunk:
            chunks.append(chunk)

    return chunks