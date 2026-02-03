import os
import time
from serpapi import GoogleSearch
from src.state import AgentState
from src.utils import generate_with_bytez

class ResearcherModule:
    def __init__(self):
        self.serpapi_key = os.getenv("SERPAPI_API_KEY")

    def search_web(self, query):
        print(f"  🔍 searching for: {query}")
        params = {
            "q": query,
            "api_key": self.serpapi_key,
            "num": 5
        }
        try:
            search = GoogleSearch(params)
            results = search.get_dict()
            organic = results.get("organic_results", [])
            
            # Simple synthesis
            content = ""
            for res in organic:
                title = res.get("title", "")
                snippet = res.get("snippet", "")
                link = res.get("link", "")
                content += f"Source: {title} ({link})\nSummary: {snippet}\n---\n"
                
            if not content:
                content = "No search results found."
        except Exception as e:
            print(f"⚠️ SerpAPI Error: {e}")
            content = f"Error during search: {e}"
            
        return content

    def research_topic(self, subtopic):
        # 1. Gather raw data
        raw_data = self.search_web(subtopic)
        
        # 2. Synthesize with Bytez-powered Gemini
        print(f"  🤖 analyzing data for: {subtopic}")
        
        system_msg = "You are a Market Researcher."
        
        prompt = f"""
        SUB-TOPIC: {subtopic}
        
        RAW SEARCH CONTEXT:
        {raw_data}
        
        Task: Write a detailed research note on this sub-topic. 
        Synthesize the provided context. You can also use your internal knowledge 
        updated with the search results.
        """
        
        response_text = generate_with_bytez(
            model_id="google/gemini-2.5-pro",
            prompt=prompt,
            system_message=system_msg,
            max_tokens=2048
        )
        return response_text

def researcher_agent(state: AgentState):
    """
    Iterates through the plan and conducts research.
    """
    print(f"🕵️ RESEARCHER: Starting research on {len(state['research_plan'])} items...")
    
    researcher = ResearcherModule()
    research_data = {}
    
    # In a real async system, we'd do this in parallel. 
    # For now, sequential to avoid rate limits or complexity.
    for topic in state["research_plan"]:
        findings = researcher.research_topic(topic)
        research_data[topic] = findings
        time.sleep(2) # Be nice to APIs
        
    print("🕵️ RESEARCHER: Research complete.")
    return {"research_data": research_data}
