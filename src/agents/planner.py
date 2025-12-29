import os
from google import genai
from src.state import AgentState

def planner_agent(state: AgentState):
    """
    Decomposes the topic into a research plan.
    """
    print(f"🧠 PLANNER: Analyzing topic '{state['topic']}'...")
    
    # Ensure API Key is loaded
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ PLANNER: GEMINI_API_KEY not found in environment.")
    
    client = genai.Client(api_key=api_key)
    
    prompt = f"""
    You are a Senior Market Research Planner.
    
    TOPIC: {state['topic']}
    
    Goal: Create a research plan to write a comprehensive 10-page market report.
    Identify 4-5 distinct, high-value sub-topics or research questions that cover:
    1. Market Overview & Size
    2. Key Trends & Drivers
    3. Major Players & Competition
    4. Future Outlook & Challenges
    
    Output ONLY a clean list of strings, one per line. Do not number them.
    """
    
    try:
        from src.utils import generate_with_retry
        response = generate_with_retry(
            model_client=client,
            model_id="gemini-1.5-flash-001",
            contents=prompt
        )
    except Exception as e:
        print(f"❌ PLANNER Error: {e}")
        return {"research_plan": []}
    
    # Simple parsing: split by newlines and clean up
    plan = [line.strip().strip("- ") for line in response.text.strip().split("\n") if line.strip()]
    
    print(f"🧠 PLANNER: Created plan with {len(plan)} items.")
    return {"research_plan": plan}
