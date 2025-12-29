# Written in: researcher.py
import os
from google import genai
from google.genai import types
from serpapi import GoogleSearch
from dotenv import load_dotenv

# 1. Load your environment variables from .env
load_dotenv()

class GeminiResearcher:
    def __init__(self):
        # Initialize Gemini Client (Uses GEMINI_API_KEY from .env)
        self.gemini = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        
        # User also needs SERPAPI_API_KEY in .env

    def web_search(self, query):
        """Perform a web search using SerpAPI."""
        print(f"🔍 Searching the web for: {query}...")
        
        params = {
            "q": query,
            "api_key": os.getenv("SERPAPI_API_KEY"),
            "num": 5
        }
        
        search = GoogleSearch(params)
        results = search.get_dict()
        
        # Return organic results list
        return results.get("organic_results", [])

    def generate_research_report(self, topic):
        """Collects web data and uses Gemini to write a report."""
        
        # Step A: Get Context from SerpAPI
        raw_results = self.web_search(topic)
        
        # Format results into a clean string for the LLM
        context_text = ""
        for i, res in enumerate(raw_results):
            # Adapting to SerpAPI structure
            link = res.get('link', 'No Link')
            snippet = res.get('snippet', 'No Content')
            context_text += f"\n[{i+1}] Source: {link}\nContent: {snippet}\n"

        # Step B: Create the Prompt for Gemini
        prompt = f"""
        You are an expert AI Research Assistant. Your goal is to write a high-quality, 
        professional research report based on the provided web context.

        TOPIC: {topic}

        WEB CONTEXT:
        {context_text}

        INSTRUCTIONS:
        1. Summarize the key findings from the sources.
        2. Use a professional and objective tone.
        3. Include a 'Sources' section at the end listing the URLs provided.
        4. If the context doesn't contain enough info, state what is missing.
        """

        # Step C: Call Gemini 1.5 Flash (or 2.0 Flash) with Grounding
        print(f"🤖 Gemini is analyzing and writing the report...")
        
        response = self.gemini.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                tools=[types.Tool(google_search=types.GoogleSearch())]
            )
        )

        return response.text

# --- Simple Test Execution ---
if __name__ == "__main__":
    researcher = GeminiResearcher()
    
    user_topic = "Current state of commercial nuclear fusion 2025"
    report = researcher.generate_research_report(user_topic)
    
    print("\n" + "="*50)
    print("FINAL RESEARCH REPORT")
    print("="*50 + "\n")
    print(report)
