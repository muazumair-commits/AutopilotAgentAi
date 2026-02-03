import os
from src.state import AgentState
from src.utils import generate_with_bytez

def planner_agent(state: AgentState):
    """
    Decomposes the topic into a research plan.
    """
    print(f"🧠 PLANNER: Analyzing topic '{state['topic']}'...")
    
    system_msg = "You are a Senior Market Research Planner."
    
    prompt = f"""
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
        response_text = generate_with_bytez(
            model_id="google/gemini-2.5-flash-lite",
            prompt=prompt,
            system_message=system_msg,
            max_tokens=1024
        )
    except Exception as e:
        print(f"❌ PLANNER Error: {e}")
        return {"research_plan": []}
    
    # Simple parsing: split by newlines and clean up
    plan = [line.strip().strip("- ") for line in response_text.strip().split("\n") if line.strip()]
    
    print(f"🧠 PLANNER: Created plan with {len(plan)} items.")
    return {"research_plan": plan}
