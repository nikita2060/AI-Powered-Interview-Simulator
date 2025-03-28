import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_response(user_input):
    response = genai.generate_text(prompt=user_input)
    return response
