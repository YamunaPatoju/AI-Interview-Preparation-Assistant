import re
import pdfplumber
from skills import SKILLS


def extract_text(uploaded_file):
    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_email(text):
    emails = re.findall(r'\S+@\S+', text)

    if emails:
        return emails[0]

    return "Not Found"


def extract_phone(text):
    phones = re.findall(r'\d{10}', text)

    if phones:
        return phones[0]

    return "Not Found"


def extract_skills(text):

    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills