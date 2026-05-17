from langchain_ollama import OllamaLLM


# Load local LLM
llm = OllamaLLM(model="tinyllama")


def generate_resume_suggestions(
    ats_score,
    matched_skills,
    missing_skills
):
    """
    Generate AI suggestions for resume improvement
    """

    prompt = f"""
    You are an ATS resume expert.

    ATS Score: {ats_score}

    Matched Skills:
    {matched_skills}

    Missing Skills:
    {missing_skills}

    Give short and specific suggestions.

    Focus mainly on:
    - missing skills
    - projects to add
    - technologies to learn

    Keep response concise.
    """

    response = llm.invoke(prompt)

    return response