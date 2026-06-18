def calculate_score(skills):

    required_skills = [
        "Python",
        "SQL",
        "Machine Learning",
        "Git",
        "GitHub",
        "FastAPI",
        "Docker",
        "AWS"
    ]

    matched = 0

    for skill in required_skills:
        if skill in skills:
            matched += 1

    score = (matched / len(required_skills)) * 100

    return round(score)


def get_missing_skills(skills):

    required_skills = [
        "Python",
        "SQL",
        "Machine Learning",
        "Git",
        "GitHub",
        "FastAPI",
        "Docker",
        "AWS"
    ]

    missing = []

    for skill in required_skills:
        if skill not in skills:
            missing.append(skill)

    return missing
