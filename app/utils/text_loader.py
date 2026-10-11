from pathlib import Path


def load_text_file(file_path: str) -> str:
    """
    Load text content from a text file.

    Args:
        file_path: Path to the text file.

    Returns:
        Text contained in the file.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Text file not found: {file_path}"
        )

    return path.read_text(encoding="utf-8")