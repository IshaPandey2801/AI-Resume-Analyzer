def calculate_resume_jd_match(resume_skills, jd_skills):
    """
    Calculate skill match percentage
    """

    # Convert to lowercase sets
    resume_skills_set = set(
        skill.lower() for skill in resume_skills
    )

    jd_skills_set = set(
        skill.lower() for skill in jd_skills
    )

    # Find matching skills
    matched_skills = resume_skills_set.intersection(
        jd_skills_set
    )

    # Avoid division by zero
    if len(jd_skills_set) == 0:
        return 0, []

    # Calculate percentage
    match_percentage = (
        len(matched_skills) / len(jd_skills_set)
    ) * 100

    return round(match_percentage, 2), list(matched_skills)


def find_missing_skills(resume_skills, jd_skills):
    """
    Find skills missing from resume
    """

    resume_skills_set = set(
        skill.lower() for skill in resume_skills
    )

    jd_skills_set = set(
        skill.lower() for skill in jd_skills
    )

    missing_skills = jd_skills_set - resume_skills_set

    return list(missing_skills)