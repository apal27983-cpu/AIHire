import fitz


def extract_text_from_pdf(
    file_path: str
):
    text = ""

    pdf = fitz.open(file_path)

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text

COMMON_SKILLS = [
    "python",
    "java",
    "sql",
    "fastapi",
    "django",
    "flask",
    "react",
    "javascript",
    "html",
    "css",
    "postgresql",
    "mysql",
    "docker",
    "git",
    "aws",
    "machine learning",
    "data science",
    "pandas",
    "numpy",
    "tensorflow"
]


def extract_skills(
    text: str
):
    text = text.lower()

    skills = []

    for skill in COMMON_SKILLS:
        if skill in text:
            skills.append(skill)

    return list(set(skills))

