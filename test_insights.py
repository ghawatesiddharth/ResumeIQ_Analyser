from app.nlp.insights import generate_insights


def main():

    result = generate_insights(
        skill_match_percentage=81.25,
        matched_skills=[
            "Python",
            "SQL",
            "Machine Learning",
            "FastAPI",
            "Git",
        ],
        missing_skills=[
            "AWS",
            "Docker",
            "Cloud",
        ],
        text_similarity_percentage=23.05,
    )


    print(
        "========================================"
    )

    print(
        "          RESUMEIQ INSIGHTS"
    )

    print(
        "========================================"
    )


    for key, value in result.items():

        print(
            f"\n{key}:"
        )

        print(value)


if __name__ == "__main__":
    main()