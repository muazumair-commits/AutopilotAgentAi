import os
from google import genai
from src.state import AgentState

def editor_agent(state: AgentState):
    """
    Compiles drafts into a final report.
    """
    print("📝 EDITOR: Compiling final report...")
    
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    # Combine all drafts
    full_draft = ""
    for topic, content in state["draft_sections"].items():
        full_draft += f"\n\n## {topic}\n\n{content}"
        
    prompt = f"""
    You are the Chief Editor of a Market Research Firm.
    
    TOPIC: {state['topic']}
    
    FULL DRAFT:
    {full_draft}
    
    Task: Assemble the final 10-page equivalence Market Report.
    1. Add a Title and Executive Summary at the beginning.
    2. Ensure the flow is logical between sections.
    3. Add a "Conclusion & Strategic Recommendations" section at the end.
    4. Ensure specific formatting (Markdown).
    5. List References/Sources if available in the text.
    
    Return the complete Markdown report.
    """
    
    from src.utils import generate_with_retry
    response = generate_with_retry(
        model_client=client,
        model_id="gemini-1.5-flash-8b",
        contents=prompt
    )
    
    print("📝 EDITOR: Final report generated.")
    return {"final_report": response.text}
