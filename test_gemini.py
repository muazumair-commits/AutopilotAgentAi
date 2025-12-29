
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Skipping test: GEMINI_API_KEY not found.")
    exit()

client = genai.Client(api_key=api_key)

models_to_test = ["gemini-1.5-flash-001", "gemini-1.5-flash", "gemini-flash-latest"]

print("Testing Gemini Models...")
for model in models_to_test:
    print(f"--- Testing model: {model} ---")
    try:
        response = client.models.generate_content(
            model=model,
            contents="Hello"
        )
        print(f"SUCCESS: {model}")
    except Exception as e:
        print(f"FAILED: {model} - {e}")
