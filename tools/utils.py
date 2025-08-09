import os
import time
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

genai.configure(api_key=GEMINI_API_KEY)

def get_gemini_model(model_name: str = 'gemini-pro'):
    """
    Returns a configured GenerativeModel instance with a simple retry mechanism.
    """
    return genai.GenerativeModel(model_name)

def generate_with_retry(model, prompt, retries=3, delay=5):
    """
    Generates content with a simple retry mechanism.
    """
    for i in range(retries):
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error generating content: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
    raise Exception(f"Failed to generate content after {retries} retries.")
