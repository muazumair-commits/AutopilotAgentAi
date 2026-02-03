import os
import time
from src.state import AgentState
from src.utils import generate_with_bytez

def writer_agent(state: AgentState):
    """
    Synthesizes research into draft sections.
    """
    print("✍️ WRITER: Drafting sections...")
    
    draft_sections = {}
    system_msg = "You are an Expert Market Analyst."
    
    for topic, research in state["research_data"].items():
        print(f"  ✍️ writing section: {topic}")
        
        prompt = f"""
        SECTION TOPIC: {topic}
        
        RESEARCH NOTES:
        {research}
        
        Task: Write a comprehensive, professional report section on this topic.
        - Use Markdown formatting.
        - Include data points if available.
        - Be objective and analytical.
        - Do NOT include a generic conclusion at the end of every section.
        """
        
        response_text = generate_with_bytez(
            model_id="google/gemini-2.0-flash-exp",
            prompt=prompt,
            system_message=system_msg,
            max_tokens=2048
        )
        draft_sections[topic] = response_text
        time.sleep(2)
        
    print("✍️ WRITER: Drafting complete.")
    return {"draft_sections": draft_sections}
