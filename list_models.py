import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

try:
    print("Listing models...")
    # The new SDK might use different methods to list models, 
    # but let's try the common one or handle the error.
    # For google-genai SDK 0.x/1.x:
    models = client.models.list()
    
    print("\nAvailable Models:")
    for m in models:
        # Check if it supports generateContent
        if "generateContent" in (m.supported_actions or []):
            print(f"- {m.name} (ID: {m.display_name})")
        else:
            print(f"- {m.name} [No generateContent]")
            
except Exception as e:
    print(f"Error listing models: {e}")
