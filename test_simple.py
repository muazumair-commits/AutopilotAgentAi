"""
Simple test to verify Bytez integration works
"""
import os
import sys
from dotenv import load_dotenv

# Load environment
load_dotenv()

print("=" * 60)
print("BYTEZ INTEGRATION TEST")
print("=" * 60)

# Step 1: Check API key
print("\n[1/4] Checking API key...")
api_key = os.getenv("BYTEZ_API_KEY")
if not api_key:
    print("❌ BYTEZ_API_KEY not found in .env file")
    sys.exit(1)
print(f"✅ API key found: {api_key[:15]}...")

# Step 2: Test import
print("\n[2/4] Testing imports...")
try:
    from langchain_bytez import BytezChatModel
    from langchain.schema import HumanMessage, SystemMessage
    print("✅ Imports successful")
except Exception as e:
    print(f"❌ Import failed: {e}")
    sys.exit(1)

# Step 3: Test model creation
print("\n[3/4] Creating Bytez model...")
try:
    model = BytezChatModel(
        model_id="google/gemini-2.5-pro",
        api_key=api_key,
        capacity={"min": 1, "max": 1},
        params={"max_new_tokens": 100},
        timeout=10,
    )
    print("✅ Model created successfully")
except Exception as e:
    print(f"❌ Model creation failed: {e}")
    sys.exit(1)

# Step 4: Test API call
print("\n[4/4] Testing API call...")
try:
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content="Say 'Bytez integration successful!' if you can read this.")
    ]
    response = model.invoke(messages)
    print(f"✅ API call successful!")
    print(f"\nResponse: {response.content}")
except Exception as e:
    print(f"❌ API call failed: {e}")
    print("\nPossible issues:")
    print("- Check your BYTEZ_API_KEY is valid")
    print("- Verify internet connection")
    print("- Check Bytez service status")
    sys.exit(1)

print("\n" + "=" * 60)
print("ALL TESTS PASSED! ✅")
print("=" * 60)
print("\nBytez integration is working correctly.")
print("You can now run: streamlit run app.py")
