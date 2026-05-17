def calculate_ats_score(resume_text, detected_skills):
    """
    Calculate ATS score for resume
    """

    score = 0

    # -------------------------------
    # 1. Skill Score
    # -------------------------------

    skill_score = min(len(detected_skills) * 5, 50)

    score += skill_score

    # -------------------------------
    # 2. Resume Sections Score
    # -------------------------------

    sections = [
        "education",
        "experience",
        "skills",
        "project",
        "certification"
    ]

    section_score = 0

    for section in sections:

        if section in resume_text.lower():
            section_score += 6

    score += section_score

    # -------------------------------
    # 3. Resume Length Score
    # -------------------------------

    word_count = len(resume_text.split())

    if word_count >= 300:
        score += 20

    elif word_count >= 200:
        score += 15

    elif word_count >= 100:
        score += 10

    return min(score, 100)