from src.resume_parser import extract_text_from_pdf
from src.text_cleaner import clean_resume_text
from src.skill_extractor import extract_skills
from src.ats_score import calculate_ats_score
from src.jd_matcher import (
    calculate_resume_jd_match,
    find_missing_skills
)
from src.suggestion_engine import (
    generate_resume_suggestions
)

# Resume path
resume_path = "data/resumes/sample_resume.pdf"

# Extract resume text
resume_text = extract_text_from_pdf(resume_path)

# Clean resume text
cleaned_text = clean_resume_text(resume_text)

# Extract resume skills
skills = extract_skills(cleaned_text)

# Calculate ATS score
ats_score = calculate_ats_score(cleaned_text, skills)

#sample job description
job_description = """
We are hiring a Python Developer with experience in:

Python
SQL
Machine Learning
Flask
Git
Docker
AWS
Kubernetes
LangChain
Streamlit
NLP
"""

# Clean JD text
cleaned_jd = clean_resume_text(job_description)

# Extract JD skills
jd_skills = extract_skills(cleaned_jd)

# Calculate Resume-JD Match
match_score, matched_skills = calculate_resume_jd_match(
    skills,
    jd_skills
)

# Find missing skills
missing_skills = find_missing_skills(
    skills,
    jd_skills
)

# Generate AI Suggestions
ai_suggestions = generate_resume_suggestions(
    ats_score,
    matched_skills,
    missing_skills
)

# Print detected skills
print("\nDetected Skills:\n")

for skill in skills:
    print("-", skill)

# Print ATS score
print(f"\nATS Score: {ats_score}/100")

# Print JD Match Score
print(f"\nResume-JD Match Score: {match_score}%")

# Print matched skills
print("\nMatched Skills:")

for skill in matched_skills:
    print("-", skill)

#print for missing skill
print("\nMissing Skills:")

if missing_skills:

    for skill in missing_skills:
        print("-", skill)

else:
    print("No missing skills found")

print("\nAI Resume Suggestions:\n")

print(ai_suggestions)