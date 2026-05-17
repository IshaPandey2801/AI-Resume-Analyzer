import plotly.express as px
import os
import streamlit as st
from PIL import Image
import pytesseract
from docx import Document
from src.resume_classifier import classify_resume


st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}

.stButton>button {
    border-radius: 10px;
    height: 50px;
    font-size: 18px;
    font-weight: 600;
}

.skill-box {
    padding: 10px;
    border-radius: 12px;
    margin: 5px;
    display: inline-block;
}
</style>
""", unsafe_allow_html=True)





st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


from src.file_parser import (
    extract_text
)

from src.text_cleaner import (
    clean_resume_text
)

from src.skill_extractor import (
    extract_skills
)

from src.ats_score import (
    calculate_ats_score
)

from src.jd_matcher import (
    calculate_resume_jd_match,
    find_missing_skills
)

from src.suggestion_engine import (
    generate_resume_suggestions
)




# Title
st.title("📄 AI Resume Analyzer")

st.markdown(
    "Analyze resumes using ATS scoring, NLP, and Generative AI"
)

# File uploader
uploaded_file = st.file_uploader(
    "Upload Your Resume",
    type=["pdf", "docx", "png", "jpg", "jpeg"]
)

# Success message
if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

# Job description
job_description = st.text_area(
    "Paste Job Description",
    height=200
)

# Analyze button
analyze_button = st.button(
    "Analyze Resume"
)

# Analyze action
if analyze_button:

    # Check upload
    if uploaded_file is None:

        st.error("Please upload a resume.")

    # Check JD
    elif not job_description.strip():

        st.error("Please paste job description.")

    else:

        with st.spinner("Analyzing Resume..."):

            # Save uploaded file temporarily
            temp_resume_path = os.path.join(
                "data/resumes",
                uploaded_file.name
            )

            with open(temp_resume_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Extract resume text
            resume_text = extract_text(
                temp_resume_path
            )

            # Clean resume text
            cleaned_resume = clean_resume_text(
                resume_text
            )

            
            # Extract resume skills
            resume_skills = extract_skills(
                cleaned_resume
            )

            resume_category = classify_resume(resume_skills)

            # ATS Score
            ats_score = calculate_ats_score(
                cleaned_resume,
                resume_skills
            )



            # Clean JD
            cleaned_jd = clean_resume_text(
                job_description
            )

            # Extract JD skills
            jd_skills = extract_skills(
                cleaned_jd
            )

            # Match Score
            match_score, matched_skills = (
                calculate_resume_jd_match(
                    resume_skills,
                    jd_skills
                )
            )

            # Missing Skills
            missing_skills = find_missing_skills(
                resume_skills,
                jd_skills
            )

            # AI Suggestions
            ai_suggestions = (
                generate_resume_suggestions(
                    ats_score,
                    matched_skills,
                    missing_skills
                )
            )

            st.download_button(
                label="Download AI Suggestions",
                data=ai_suggestions,
                file_name="resume_suggestions.txt",
                mime="text/plain"
            )

            # ---------------------------
            # DISPLAY RESULTS
            # ---------------------------

            tab1, tab2, tab3, tab4 = st.tabs([
                "📊 Analysis",
                "🛠 Skills",
                "📈 Charts",
                "🤖 AI Suggestions"
            ])

            # ===================================
            # TAB 1 — ANALYSIS
            # ===================================

            with tab1:

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "ATS Score",
                        f"{ats_score}/100"
                    )

                    if ats_score >= 80:
                        st.success("Strong Resume")

                    elif ats_score >= 60:
                        st.warning("Average Resume")

                    else:
                        st.error("Weak Resume")


                with col2:
                    st.metric(
                        "Resume-JD Match",
                        f"{match_score:.1f}%"
                    )

                st.write("ATS Progress")

                st.progress(ats_score / 100)

            # ===================================
            # TAB 2 — SKILLS
            # ===================================

            with tab2:

                # ----------------------
                # Detected Skills
                # ----------------------

                st.subheader("Resume Category")

                st.success(resume_category)


                st.subheader("Detected Skills")

                detected_html = ""

                for skill in resume_skills:

                    detected_html += f'''
                    <span style="
                        background-color:#d1fae5;
                        padding:8px 14px;
                        border-radius:20px;
                        margin:5px;
                        display:inline-flex;
                        align-items:center;
                        white-space:nowrap;
                        color:black;
                        font-weight:500;
                    ">
                        {skill}
                    </span>
                    '''

                st.markdown(
                    detected_html,
                    unsafe_allow_html=True
                )

                # ----------------------
                # Matched Skills
                # ----------------------

                st.subheader("Matched Skills")

                matched_html = ""

                for skill in matched_skills:

                    matched_html += f'''
                    <span style="
                        background-color:#dbeafe;
                        padding:8px 14px;
                        border-radius:20px;
                        margin:5px;
                        display:inline-flex;
                        align-items:center;
                        white-space:nowrap;
                        color:black;
                        font-weight:500;
                    ">
                        {skill}
                    </span>
                    '''

                st.markdown(
                    matched_html,
                    unsafe_allow_html=True
                )

                # ----------------------
                # Missing Skills
                # ----------------------

                st.subheader("Missing Skills")

                if missing_skills:

                    missing_html = ""

                    for skill in missing_skills:

                        missing_html += f'''
                        <span style="
                            background-color:#fee2e2;
                            padding:8px 14px;
                            border-radius:20px;
                            margin:5px;
                            display:inline-flex;
                            align-items:center;
                            white-space:nowrap;
                            color:black;
                            font-weight:500;
                        ">
                            {skill}
                        </span>
                        '''

                    st.markdown(
                        missing_html,
                        unsafe_allow_html=True
                    )

                else:

                    st.success("No Missing Skills Found")


                if missing_skills:

                    st.subheader("Recommended Skills to Learn")

                    for skill in missing_skills[:5]:
                        st.write("•", skill)



            # ===================================
            # TAB 3 — CHARTS
            # ===================================

            with tab3:

                st.subheader("Resume Skill Analysis")

                extra_skills = list(
                    set(resume_skills) - set(matched_skills)
                )

                chart_data = {
                    "Category": [
                        "Matched Skills",
                        "Missing Skills",
                        "Extra Skills"
                    ],
                    "Count": [
                        len(matched_skills),
                        len(missing_skills),
                        len(extra_skills)
                    ]
                }

                fig = px.pie(
                    names=chart_data["Category"],
                    values=chart_data["Count"],
                    title="Resume Skill Analysis",
                    hole=0.4
                )

                fig.update_layout(
                    height=450
                )

                st.plotly_chart(
                    fig,
                    width="stretch"
                )

            # ===================================
            # TAB 4 — AI SUGGESTIONS
            # ===================================

            with tab4:

                st.subheader("AI Suggestions")

                st.text_area(
                    "AI Career Suggestions",
                    ai_suggestions,
                    height=300
                )





            # ---------------------------
            # DOWNLOAD REPORT
            # ---------------------------

            report = f"""
            AI RESUME ANALYSIS REPORT
            ==========================

            ATS Score: {ats_score}/100

            Resume-JD Match: {match_score}%

            Detected Skills:
            {', '.join(resume_skills)}

            Matched Skills:
            {', '.join(matched_skills)}

            Missing Skills:
            {', '.join(missing_skills)}

            AI Suggestions:
            {ai_suggestions}
            """

            st.download_button(
                label="📥 Download Report",
                data=report,
                file_name="resume_analysis_report.txt",
                mime="text/plain"
            )


            