text = """
I know Python, SQL and Machine Learning.
"""

SKILLS = [
    "Python",
    "SQL",
    "Machine Learning",
    "TensorFlow"
]

found_skills = []

for skill in SKILLS:
    if skill in text:
        found_skills.append(skill)

print(found_skills)