import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

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

    Resume (LaTeX or plain text):
    ```
    {resume_text}
    ```

    Target Role: {target_role}
    Experience Level: {experience_level}

    Please provide the following:
    1. A general ATS score out of 100.
    2. An ATS score based on the target role and experience level, out of 100.
    3. A list of specific, actionable suggestions for improvement.
    """

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text
