import os
from src.state import AgentState
from src.utils import generate_with_bytez

def editor_agent(state: AgentState):
    """
    Compiles drafts into a final report.
    """
    print("📝 EDITOR: Compiling final report...")
    
    # Combine all drafts
    full_draft = ""
    for topic, content in state["draft_sections"].items():
        full_draft += f"\n\n## {topic}\n\n{content}"
    
    system_msg = "You are the Chief Editor of a Market Research Firm."
    
    prompt = f"""
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
    
    response_text = generate_with_bytez(
        model_id="google/gemini-2.5-flash",
        prompt=prompt,
        system_message=system_msg,
        max_tokens=4096
    )
    
    print("📝 EDITOR: Final report generated.")
    return {"final_report": response_text}
