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
    target_job_role: str,
    user_description: str,
) -> str:
    """
    Generates a professional LaTeX resume from user-provided details.
    """
    prompt = f"""
    Create a professional and complete LaTeX resume for a person named {name}.
    The user is targeting the job role of '{target_job_role}'.
    Here is a short description from the user: '{user_description}'.

    Based on this information, generate a resume. Invent plausible details for sections like Education, Work Experience, Projects, etc. The user will be able to update these sections later.
    Use a clean and modern LaTeX template.

    IMPORTANT: For each section of the resume (e.g., Education, Work Experience, Projects, Skills), you MUST enclose the entire section's LaTeX code, including the section heading, within special comment markers.
    The format for these markers is:
    % BEGIN_SECTION: [SECTION_NAME]
    ... LaTeX code for the section ...
    % END_SECTION: [SECTION_NAME]

    For example:
    % BEGIN_SECTION: Education
    \\section*{{Education}}
    \\resumeSubheadingListStart
      \\resumeSubheading
        {{University of Example}}{{Anytown, USA}}
        {{Bachelor of Science in Computer Science}}{{2020 -- 2024}}
    \\resumeSubheadingListEnd
    % END_SECTION: Education

    Please generate the full LaTeX code for the resume with these markers for all standard resume sections, including:
    - Contact Information
    - Education
    - Work Experience
    - Projects
    - Skills
    - Achievements/Certifications
    - Extracurricular Activities
    """

    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content(prompt)
    return response.text
