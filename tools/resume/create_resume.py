from pydantic import BaseModel
from tools.utils import get_gemini_model, generate_with_retry

class RichToolDescription(BaseModel):
    description: str
    use_when: str
    side_effects: str | None = None

CreateResumeDescription = RichToolDescription(
    description="Create a new resume from scratch.",
    use_when="Use this when the user wants to create a new resume.",
    side_effects="Generates a new resume in LaTeX format.",
)

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
    template_type: str = "modern",
) -> str:
    """
    Generates a professional LaTeX resume from user-provided details.
    """
    prompt = f"""
    Create a professional LaTeX resume based on the following details.
    Use a {template_type} and clean LaTeX template.
    Respond ONLY with the completed LaTeX document code, without any explanation or extra text.

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
    """

    model = get_gemini_model()
    return generate_with_retry(model, prompt)
