def calculate_skill_match(
    resume_skills: list[str],
    job_skills: list[str],
) -> dict:
    """
    Compare resume skills against skills required by a job.

    Args:
        resume_skills: Skills found in the candidate's resume.
        job_skills: Skills required by the job description.

    Returns:
        Dictionary containing matched skills, missing skills,
        and the skill match percentage.
    """

    resume_skill_set = {
        skill.lower(): skill
        for skill in resume_skills
    }

    job_skill_set = {
        skill.lower(): skill
        for skill in job_skills
    }

    matched_skill_keys = (
        set(resume_skill_set.keys())
        & set(job_skill_set.keys())
    )

    missing_skill_keys = (
        set(job_skill_set.keys())
        - set(resume_skill_set.keys())
    )

    matched_skills = sorted(
        resume_skill_set[key]
        for key in matched_skill_keys
    )

    missing_skills = sorted(
        job_skill_set[key]
        for key in missing_skill_keys
    )

    if not job_skill_set:
        match_percentage = 0.0
    else:
        match_percentage = (
            len(matched_skills)
            / len(job_skill_set)
        ) * 100

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_percentage": round(match_percentage, 2),
    }