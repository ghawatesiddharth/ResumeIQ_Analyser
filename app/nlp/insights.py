def generate_insights(
    skill_match_percentage: float,
    matched_skills: list[str],
    missing_skills: list[str],
    text_similarity_percentage: float,
) -> dict:
    """
    Generate practical insights from resume/job
    matching results.
    """

    # ---------------------------------
    # Overall assessment
    # ---------------------------------

    if skill_match_percentage >= 80:
        overall_assessment = (
            "Strong match"
        )

    elif skill_match_percentage >= 60:
        overall_assessment = (
            "Moderate match"
        )

    elif skill_match_percentage >= 40:
        overall_assessment = (
            "Partial match"
        )

    else:
        overall_assessment = (
            "Low match"
        )


    # ---------------------------------
    # Strength message
    # ---------------------------------

    if matched_skills:

        strength_message = (
            "The resume demonstrates strong "
            "coverage of several required skills, "
            "including "
            + ", ".join(matched_skills[:5])
            + "."
        )

    else:

        strength_message = (
            "No major skill overlap was detected "
            "between the resume and job description."
        )


    # ---------------------------------
    # Missing skills
    # ---------------------------------

    if missing_skills:

        missing_message = (
            f"{len(missing_skills)} required "
            "skill(s) are missing from the "
            "detected resume skills: "
            + ", ".join(missing_skills)
            + "."
        )

    else:

        missing_message = (
            "All detected job requirements are "
            "covered by the resume."
        )


    # ---------------------------------
    # Recommendation
    # ---------------------------------

    if missing_skills:

        recommendation = (
            "Consider strengthening or adding "
            "evidence for these skills in the "
            "resume if you have relevant experience: "
            + ", ".join(missing_skills)
            + "."
        )

    else:

        recommendation = (
            "The resume covers the detected "
            "technical requirements well. "
            "Focus on clearly presenting relevant "
            "projects and achievements."
        )


    # ---------------------------------
    # Text similarity interpretation
    # ---------------------------------

    if text_similarity_percentage >= 50:

        similarity_message = (
            "The resume has strong textual "
            "alignment with the job description."
        )

    elif text_similarity_percentage >= 25:

        similarity_message = (
            "The resume has moderate textual "
            "alignment with the job description."
        )

    else:

        similarity_message = (
            "The resume has relatively low textual "
            "alignment with the job description. "
            "Consider using more relevant terminology "
            "when it accurately reflects your experience."
        )


    return {
        "overall_assessment": overall_assessment,
        "strength_message": strength_message,
        "missing_message": missing_message,
        "recommendation": recommendation,
        "similarity_message": similarity_message,
    }