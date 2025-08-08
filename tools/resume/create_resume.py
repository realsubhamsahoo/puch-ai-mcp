import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def create_resume(
    name: str,
    address: str,
    linkedin_url: str,
    github_url: str,
    website_url: str,
    education: str,
    experience: str,
    projects: str,
    achievements: str,
    extracurriculars: str,
) -> str:
    """
    Generates a professional LaTeX resume from user-provided details.
    """
    prompt = f"""
    Create a professional LaTeX resume based on the following details.
    Use a clean and modern LaTeX template.

    Name: {name}
    Address: {address}
    LinkedIn: {linkedin_url}
    GitHub: {github_url}
    Website: {website_url}

    Education:
    {education}

    Work Experience:
    {experience}

    Projects:
    {projects}

    Achievements/Certifications:
    {achievements}

    Extracurricular Activities:
    {extracurriculars}

    Please generate the full LaTeX code for the resume.
    """

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text
