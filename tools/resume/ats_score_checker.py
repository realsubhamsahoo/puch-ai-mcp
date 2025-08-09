from pydantic import BaseModel
from tools.utils import get_gemini_model, generate_with_retry

class RichToolDescription(BaseModel):
    description: str
    use_when: str
    side_effects: str | None = None

AtsScoreCheckerDescription = RichToolDescription(
    description="Check the ATS score of a resume.",
    use_when="Use this when the user wants to check the ATS score of their resume.",
    side_effects="Returns the ATS score and suggestions for improvement.",
)

def ats_score_checker(
    resume_text: str,
    target_role: str,
    experience_level: str,
) -> str:
    """
    Checks the ATS score of a resume and provides improvement suggestions.
    """
    prompt = f"""
    Analyze the following resume and provide an ATS score.
    If the resume is in LaTeX format, you can ignore the preamble and focus on the content.

    Resume (LaTeX or plain text):
    ```
    {resume_text}
    ```

    Target Role: {target_role}
    Experience Level: {experience_level}

    Respond with a JSON object with the following keys:
    - "overall_score": A general ATS score out of 100.
    - "role_specific_score": An ATS score based on the target role and experience level, out of 100.
    - "suggestions": A list of specific, actionable suggestions for improvement.

    Do not include any extra text or explanation in your response.
    """

    model = get_gemini_model()
    return generate_with_retry(model, prompt)
