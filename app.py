import streamlit as st

from utils.extractor import (
    extract_text,
    extract_email,
    extract_phone,
    extract_skills
)

from utils.ats_checker import calculate_ats_score
from utils.role_predictor import predict_role
from utils.question_generator import generate_questions

st.set_page_config(
    page_title="AI Interview Preparation Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Interview Preparation Assistant")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file is not None:

    # Extract Resume Text
    text = extract_text(uploaded_file)

    # Extract Information
    email = extract_email(text)
    phone = extract_phone(text)
    skills = extract_skills(text)

    # Predict Role
    predicted_role = predict_role(skills)

    # ATS Score
    score, suggestions = calculate_ats_score(text)

    # Generate Questions
    questions = generate_questions(skills)

    # Resume Analysis
    st.header("📄 Resume Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📧 Email")
        st.write(email)

        st.subheader("📱 Phone")
        st.write(phone)

    with col2:
        st.subheader("🎯 Predicted Job Role")
        st.success(predicted_role)

    # Skills
    st.subheader("🛠 Skills")

    if skills:
        for skill in skills:
            st.write(f"✅ {skill}")
    else:
        st.warning("No skills detected.")

    # ATS Score
    st.subheader("📊 ATS Score")

    st.progress(score / 100)

    st.write(f"### Score: {score}/100")

    # Resume Quality Message
    if score < 60:
        st.error("Your resume needs significant improvement.")

    elif score < 80:
        st.warning("Your resume is good but can be improved further.")

    else:
        st.success("Your resume is ATS-friendly.")

    # Suggestions
    st.subheader("💡 Suggestions")

    if suggestions:
        for suggestion in suggestions:
            st.write(f"⚠️ {suggestion}")
    else:
        st.success("Excellent Resume! No suggestions found.")

    # Resume Building Resources
    if score < 80:

        st.subheader("📚 Recommended Resume Building Resources")

        st.markdown("""
### Resume Building Videos

1. Resume Writing: How to Create a Strong Resume  
https://www.youtube.com/watch?v=LcohcyoCXn8

2. Resume Writing: 4 Tips on How to Write a Standout Resume  
https://www.youtube.com/watch?v=aD7fP-2u3iY

3. Professor Heather Austin Resume Tutorials  
https://www.youtube.com/@ProfessorHeatherAustin

4. FreeCodeCamp Career & Resume Guidance  
https://www.youtube.com/@freecodecamp
""")

    # Interview Questions
    st.subheader("🎤 Interview Questions")

    if questions:
        for i, question in enumerate(questions, start=1):
            st.write(f"{i}. {question}")
    else:
        st.info("No interview questions available.")

    # Resume Text Viewer
    with st.expander("📄 View Extracted Resume Text"):
        st.write(text)