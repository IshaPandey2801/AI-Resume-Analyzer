def classify_resume(skills):

    if "machine learning" in skills or "python" in skills:
        return "Data Science Resume"

    elif "html" in skills or "css" in skills:
        return "Frontend Developer Resume"

    elif "java" in skills:
        return "Java Developer Resume"

    return "General Resume"