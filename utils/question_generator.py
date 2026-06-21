QUESTION_BANK = {
    "Python": [
        "What are Python decorators?",
        "What is the difference between a list and a tuple?",
        "Explain list comprehensions."
    ],

    "SQL": [
        "What is the difference between DELETE, DROP and TRUNCATE?",
        "What are SQL JOINs?",
        "Explain normalization."
    ],

    "Machine Learning": [
        "What is overfitting?",
        "Explain bias-variance tradeoff.",
        "What is cross-validation?"
    ],

    "Deep Learning": [
        "What is a neural network?",
        "What is backpropagation?",
        "What is the difference between CNN and RNN?"
    ],

    "OpenCV": [
        "What is OpenCV?",
        "How does image preprocessing work?",
        "What are contours in OpenCV?"
    ],

    "YOLOv8": [
        "What is object detection?",
        "How does YOLO work?",
        "Why is YOLO faster than traditional methods?"
    ],

    "HTML": [
        "What is the difference between HTML and HTML5?",
        "What are semantic tags?"
    ],

    "CSS": [
        "What is the CSS box model?",
        "Difference between flexbox and grid?"
    ],

    "JavaScript": [
        "What is the difference between var, let and const?",
        "Explain closures in JavaScript."
    ]
}


def generate_questions(skills):

    questions = []

    for skill in skills:
        if skill in QUESTION_BANK:
            questions.extend(QUESTION_BANK[skill])

    return questions