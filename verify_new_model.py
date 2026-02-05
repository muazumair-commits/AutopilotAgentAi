
import os
import sys
from dotenv import load_dotenv
from bytez import Bytez

# Flush output immediately
sys.stdout.reconfigure(line_buffering=True)

load_dotenv()
api_key = os.getenv("BYTEZ_API_KEY")
client = Bytez(api_key)

model_id = "google/gemini-2.5-flash"
print(f"Testing model: {model_id}")

try:
    model = client.model(model_id)
    messages = [{"role": "user", "content": "Hello"}]
    result = model.run(messages)
    
    if result.error:
        print(f"❌ Error: {result.error}")
    else:
        print(f"✅ Success! Output: {result.output}")
        
except Exception as e:
    print(f"❌ Exception: {e}")
