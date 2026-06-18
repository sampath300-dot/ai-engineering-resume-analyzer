import streamlit as st
import os

from resume_parser import extract_text
from skill_extractor import extract_skills
from scorer import calculate_score, get_missing_skills

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title(" AI Engineering Placement Readiness Analyzer")
st.write(
    "Upload your resume and evaluate your readiness for AI Engineering internships and placements."
)

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Resume uploaded successfully!")

    resume_text = extract_text(file_path)

    skills = extract_skills(resume_text)

    score = calculate_score(skills)

    missing_skills = get_missing_skills(skills)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Resume Score")

        st.metric(
            label="Score",
            value=f"{score}/100"
        )

    with col2:
        st.subheader("Skills Found")

        if skills:
            for skill in skills:
                st.success(skill)
        else:
            st.error("No skills detected")

    st.subheader("Missing Skills")

    if missing_skills:
        for skill in missing_skills:
            st.warning(skill)

    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=300
    )
