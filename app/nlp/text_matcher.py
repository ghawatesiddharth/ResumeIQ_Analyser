from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_text_similarity(
    resume_text: str,
    job_description: str,
) -> float:
    """
    Calculate similarity between a resume and a job description
    using TF-IDF vectorization and cosine similarity.

    Args:
        resume_text: Cleaned resume text.
        job_description: Cleaned job description text.

    Returns:
        Similarity percentage between 0 and 100.
    """

    documents = [
        resume_text,
        job_description,
    ]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(
        documents
    )

    similarity_matrix = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2],
    )

    similarity_score = similarity_matrix[0][0] * 100

    return round(similarity_score, 2)