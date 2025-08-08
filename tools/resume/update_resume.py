import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

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

    Existing LaTeX Resume:
    ```latex
    {existing_resume_latex}
    ```

    Target Job Profile: {target_job_profile}

    Sections to Improve: {sections_to_improve}

    Please provide the full, updated LaTeX code for the resume.
    """

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text
