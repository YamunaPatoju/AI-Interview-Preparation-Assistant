def predict_role(skills):

    skills = [skill.lower() for skill in skills]

    if any(skill in skills for skill in [
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "opencv",
        "yolov8"
    ]):
        return "AI/ML Engineer"

    elif all(skill in skills for skill in [
        "html",
        "css",
        "javascript"
    ]):
        return "Frontend Developer"

    elif any(skill in skills for skill in [
        "sql",
        "pandas",
        "numpy"
    ]):
        return "Data Analyst"

    elif any(skill in skills for skill in [
        "java",
        "c++",
        "python"
    ]):
        return "Software Developer"

    else:
        return "General IT Role"