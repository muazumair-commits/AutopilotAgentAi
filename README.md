# 🕵️ Autonomous Market Research Agent

An autonomous AI system powered by **LangGraph**, **SerpAPI**, and **Bytez (Gemini 2.5 Flash)** that conducts deep web research and generates comprehensive 10-page market reports.

## 🚀 Features
- **Multi-Agent Orchestration**: Uses LangGraph to coordinate Planner, Researcher, Writer, and Editor agents.
- **Real-time Web Research**: Integrates SerpAPI for live web browsing.
- **Deep Synthesis**: Powered by Gemini 2.5 Flash via Bytez SDK for high-quality, professional analysis.
- **Streamlit UI**: Clean, interactive dashboard for topic input and report viewing.

## 🛠️ Setup & Installation

### 1. Prerequisites
- Python 3.9+
- [SerpAPI Key](https://serpapi.com/)
- [Bytez API Key](https://bytez.com/)

### 2. Installation
```powershell
# Clone the repository
git clone <your-repo-url>
cd AI-marketresearch-agent

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
Rename `.env.example` to `.env` (or create one) and add your keys:
```env
BYTEZ_API_KEY=your_bytez_key
SERPAPI_API_KEY=your_serpapi_key
```

## 💻 Usage

### Run the Web Dashboard
```powershell
streamlit run app.py
```

### Run Integration Tests
```powershell
python test_agents_bytez.py
```

## 🏗️ Project Structure
- `app.py`: Streamlit entry point.
- `src/`: Core logic and agent definitions.
  - `agents/`: Individual agent logic (Planner, Researcher, Writer, Editor).
  - `graph.py`: LangGraph workflow definition.
  - `utils.py`: Shared utilities and Bytez integration.
- `test_agents_bytez.py`: Comprehensive pipeline verification script.

## 📜 License
MIT
