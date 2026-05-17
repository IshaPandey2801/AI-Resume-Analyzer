def extract_skills(resume_text):
    """
    Extract technical skills from resume
    """

    # Predefined skill database
    skills_db = [

        # Programming Languages
        "python",
        "java",
        "c++",
        "sql",

        # AI/ML
        "machine learning",
        "deep learning",
        "nlp",
        "tensorflow",
        "pandas",
        "numpy",

        # Web Development
        "html",
        "css",
        "javascript",
        "flask",

        # Databases
        "mysql",
        "sqlite",

        # Tools
        "git",
        "github",
        "power bi",
        "excel",

        # Generative AI
        "prompt engineering",
        "generative ai",
        "langchain"

        "tf-idf",
        "cosine similarity",
        "recommendation systems",
        "huggingface",
        "gradio",
        "streamlit",
        "ollama",

        "streamlit",
        "langchain",
        "docker",
        "aws",
        "kubernetes",
    ]

    detected_skills = []

    # Check skills in resume
    for skill in skills_db:

        if skill.lower() in resume_text.lower():
            detected_skills.append(skill)

    return detected_skills