import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini AI
genai.configure(api_key=GEMINI_API_KEY)



def test_gemini_api():
    """
    Sends a test message to Gemini AI.
    """
    try:
        model_name = "gemini-1.5-pro-latest"  # Ensure this is correct!
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Tell me about yourself.")
        print("✅ Gemini AI Response:", response.text)
    except Exception as e:
        print("❌ API Error:", e)

if __name__ == "__main__":
    # list_available_models()  # Show available models
    test_gemini_api()  # Test AI response
