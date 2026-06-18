def extract_skills(resume_text):

    skills_db = [
        "Python",
        "NumPy",
        "Pandas",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch",
        "FastAPI",
        "Docker",
        "Git",
        "GitHub",
        "SQL",
        "MySQL",
        "AWS",
        "Streamlit",
        "LangChain",
        "RAG",
        "LLM"
    ]

    detected_skills = []

    for skill in skills_db:
        if skill.lower() in resume_text.lower():
            detected_skills.append(skill)

    return detected_skills
