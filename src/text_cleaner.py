import re


def clean_resume_text(text):
    """
    Clean extracted resume text
    """

    # Convert text to lowercase
    text = text.lower()

    # Remove extra spaces and tabs
    text = re.sub(r'\s+', ' ', text)

    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s.#:+/-]', '', text)

    # Remove extra spaces again
    text = text.strip()

    return text