import os
from google import genai
from src.state import AgentState

def writer_agent(state: AgentState):
    """
    Synthesizes research into draft sections.
    """
    print("✍️ WRITER: Drafting sections...")
    
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    draft_sections = {}
    
    for topic, research in state["research_data"].items():
        print(f"  ✍️ writing section: {topic}")
        prompt = f"""
        You are an Expert Market Analyst.
        
        SECTION TOPIC: {topic}
        
        RESEARCH NOTES:
        {research}
        
        Task: Write a comprehensive, professional report section on this topic.
        - Use Markdown formatting.
        - Include data points if available.
        - Be objective and analytical.
        - Do NOT include a generic conclusion at the end of every section.
        """
        
        from src.utils import generate_with_retry
        response = generate_with_retry(
            model_client=client,
            model_id="gemini-flash-latest",
            contents=prompt
        )
        draft_sections[topic] = response.text
        import time
        time.sleep(2) # Reduced delay, relying on retry logic
        
    print("✍️ WRITER: Drafting complete.")
    return {"draft_sections": draft_sections}
