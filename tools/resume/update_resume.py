from pydantic import BaseModel
from tools.utils import get_gemini_model, generate_with_retry

class RichToolDescription(BaseModel):
    description: str
    use_when: str
    side_effects: str | None = None

UpdateResumeDescription = RichToolDescription(
    description="Update an existing resume.",
    use_when="Use this when the user wants to update an existing resume.",
    side_effects="Updates an existing resume in LaTeX format.",
)

def update_resume(
    existing_resume_latex: str,
    target_job_profile: str,
    sections_to_improve: str,
) -> str:
    """
    Updates an existing LaTeX resume to better match a target job profile.
    """
    prompt = f"""
    Update the following LaTeX resume to be optimized for the target job profile.
    Focus on improving the specified sections for better ATS compatibility.
    Respond ONLY with the completed LaTeX document code, without any explanation or extra text.

    Existing LaTeX Resume:
    ```latex
    {existing_resume_latex}
    ```

    Target Job Profile: {target_job_profile}

    Sections to Improve: {sections_to_improve}
    """

    model = get_gemini_model()
    return generate_with_retry(model, prompt)
