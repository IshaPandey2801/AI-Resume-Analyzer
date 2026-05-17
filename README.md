# AI-Resume-Analyzer

An AI-powered Resume Analyzer built using Python, Generative AI, and NLP techniques.
This project helps users analyze resumes, calculate ATS scores, compare resumes with job descriptions, and get AI-generated improvement suggestions.

Built with:

* Python
* LangChain
* Ollama
* Streamlit

#  Features

- Upload Resume (PDF/DOCX)
- Extract Resume Text
- AI-based Skill Detection
- ATS Score Generation
- Resume vs Job Description Matching
- Missing Skills Analysis
- AI-generated Resume Suggestions
- Clean and Interactive UI
- 100% Free Local LLM Setup using Ollama

# How It Works

Resume Upload
      ↓
Text Extraction
      ↓
Skill Analysis
      ↓
ATS Score Calculation
      ↓
Job Description Matching
      ↓
Missing Skills Detection
      ↓
AI Suggestions Generation


#  Tech Stack

| Technology          | Purpose           |
| ------------------- | ----------------- |
| Python              | Core Programming  |
| LangChain           | LLM Workflow      |
| Ollama              | Local LLM Runtime |
| Streamlit           | Frontend UI       |
| FAISS               | Vector Database   |
| PyPDF2 / pdfplumber | PDF Processing    |


# 📂 Project Structure

AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│
├── utils/
│   ├── pdf_extractor.py
│   ├── skill_extractor.py
│   ├── ats_calculator.py
│   ├── jd_matcher.py
│   └── llm_handler.py
│
├── models/
│
└── assets/


#  Installation

## 1️) Clone Repository
git clone <your-repo-link>
cd AI-Resume-Analyzer

## 2️) Create Virtual Environment
### Windows
python -m venv venv
venv\Scripts\activate

## 3️) Install Dependencies
pip install -r requirements.txt


#  Run Project
streamlit run app.py


#  Future Improvements
* Multi-resume comparison
* Resume chatbot
* Interview question generator
* LinkedIn profile analyzer
* Resume ranking system
* Deployment on cloud


#  Learning Outcomes
This project demonstrates:
* Generative AI integration
* NLP fundamentals
* Resume parsing
* Prompt engineering
* RAG concepts
* Local LLM usage
* Streamlit UI development


# Support
If you found this project helpful, give it a ⭐ on GitHub.


# 👩‍💻 Author
Shreya Pandey
