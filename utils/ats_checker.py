def calculate_ats_score(text):

    score = 0
    suggestions = []

    sections = {
        "education": 20,
        "skills": 20,
        "projects": 20,
        "experience": 20,
        "internship": 20
    }

    text = text.lower()

    for section, marks in sections.items():

        if section in text:
            score += marks
        else:
            suggestions.append(f"Add {section.title()} section")

    return score, suggestions