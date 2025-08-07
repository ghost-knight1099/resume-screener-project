import re
from pdfminer.high_level import extract_text

# Example skill list — expand as needed
SKILLS = [
    "Python", "Flask", "Django", "NLP", "Machine Learning", "Deep Learning",
    "SQL", "Java", "JavaScript", "React", "AWS", "Docker", "Kubernetes"
]

def extract_email(text):
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match.group() if match else None

def extract_phone(text):
    match = re.search(r"\+?\d[\d\s\-]{9,14}", text)
    return match.group() if match else None

def extract_name(text):
    # Naive: Take first line or first capitalized phrase — improve later with NLP
    lines = text.split('\n')
    for line in lines:
        if line.strip() and len(line.split()) <= 4:
            return line.strip()
    return "Unknown"

def extract_skills(text):
    found = [skill for skill in SKILLS if skill.lower() in text.lower()]
    return list(set(found))

def parse_resume(file):
    text = extract_text(file)
    
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text)
    }
