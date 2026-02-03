# Bytez API Quick Start Guide

## 🚀 Quick Setup (5 Minutes)

### 1. Install Package
```powershell
pip install langchain_bytez
```

### 2. Add API Key to `.env`
```env
BYTEZ_API_KEY=your_bytez_api_key_here
```

### 3. Update `requirements.txt`
Add this line:
```
langchain_bytez
```

### 4. Test Connection
```powershell
python test_bytez_integration.py
```

---

## 📝 Model ID Reference

### Gemini Models (via Bytez)
```python
"google/gemini-2.5-pro"           # Current model (high capability)
"google/gemini-1.5-pro"           # Balanced
"google/gemini-2.0-flash-exp"     # Latest experimental
```

### OpenAI Models (via Bytez)
```python
"openai/gpt-4"                    # Most capable
"openai/gpt-4-turbo"              # Faster GPT-4
"openai/gpt-3.5-turbo"            # Fast and cheap
```

### Anthropic Models (via Bytez)
```python
"anthropic/claude-3-opus"         # Most capable
"anthropic/claude-3-sonnet"       # Balanced
"anthropic/claude-3-haiku"        # Fast and cheap
```

---

## 🔧 Usage in Agents

### Basic Pattern
```python
from src.utils import generate_with_bytez

response_text = generate_with_bytez(
    model_id="google/gemini-1.5-flash-8b",
    prompt="Your prompt here",
    system_message="You are a helpful assistant.",
    max_tokens=2048
)
```

### Mix Different Models
```python
# planner.py
model_id="openai/gpt-4"  # Use GPT-4 for planning

# researcher.py
model_id="google/gemini-1.5-flash-8b"  # Use Gemini for research

# writer.py
model_id="anthropic/claude-3-sonnet"  # Use Claude for writing

# editor.py
model_id="openai/gpt-4"  # Use GPT-4 for editing
```

---

## ✅ Testing Checklist

- [ ] Installed `langchain_bytez`
- [ ] Added `BYTEZ_API_KEY` to `.env`
- [ ] Updated `requirements.txt`
- [ ] Modified `src/utils.py`
- [ ] Updated all 4 agent files
- [ ] Ran `test_bytez_integration.py` successfully
- [ ] Tested full app with `streamlit run app.py`
- [ ] Verified report quality matches previous version

---

## 🐛 Common Issues

**"BYTEZ_API_KEY not found"**
→ Check `.env` file and ensure `load_dotenv()` is called

**"Module not found: langchain_bytez"**
→ Run `pip install langchain_bytez`

**"Invalid model_id"**
→ Use format `provider/model-name` (e.g., `google/gemini-1.5-flash-8b`)

**Slow responses**
→ Try a faster model like `google/gemini-1.5-flash-8b` or `openai/gpt-3.5-turbo`

---

## 📚 Full Documentation

See `walkthrough.md` in the artifacts folder for complete step-by-step instructions.
