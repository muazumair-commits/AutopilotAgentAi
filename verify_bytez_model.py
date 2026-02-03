from src.utils import generate_with_bytez
from dotenv import load_dotenv
import os

load_dotenv()

models_to_test = [
    "google/gemini-2.0-flash-exp",
    "google/gemini-1.5-flash",
    "google/gemini-1.5-pro",
]

for model in models_to_test:
    print(f"Testing {model}...")
    try:
        res = generate_with_bytez("Hi", model_id=model)
        print(f"SUCCESS: {model}")
        break  # Found one
    except Exception as e:
        print(f"FAIL: {model} -> {e}")
