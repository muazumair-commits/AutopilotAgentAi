import streamlit as st
import os
from dotenv import load_dotenv
from src.graph import create_graph

# Load environment variables
load_dotenv()

st.set_page_config(page_title="AI Market Researcher", page_icon="🕵️")

st.title("🕵️ Autonomous Market Research Agent")
st.write("Powered by LangGraph, SerpAPI, and Gemini Flash Latest")

# Sidebar for inputs (masked keys if not in env)
with st.sidebar:
    st.header("Configuration")
    if not os.getenv("GEMINI_API_KEY"):
        os.environ["GEMINI_API_KEY"] = st.text_input("Gemini API Key", type="password")
    if not os.getenv("SERPAPI_API_KEY"):
        os.environ["SERPAPI_API_KEY"] = st.text_input("SerpAPI Key", type="password")

topic = st.text_input("Enter a research topic:", placeholder="e.g., Generative AI in Healthcare")

if st.button("Start Research"):
    if not topic:
        st.warning("Please enter a topic.")
    else:
        # Initialize Graph
        app = create_graph()
        
        # Initial State
        initial_state = {
            "topic": topic,
            "research_plan": [],
            "research_data": {},
            "draft_sections": {},
            "final_report": "",
            "iteration": 0
        }
        
        status_text = st.empty()
        report_area = st.container()
        
        with st.status("Running Agent Pipeline...", expanded=True) as status:
            # Stream the graph execution
            # LangGraph stream returns events
            for event in app.stream(initial_state):
                for node, output in event.items():
                    if node == "planner":
                        st.write("✅ **Planner**: Research plan created.")
                        with st.expander("View Plan"):
                            st.write(output.get("research_plan", []))
                    
                    elif node == "researcher":
                        st.write("✅ **Researcher**: Data gathered.")
                        with st.expander("View Research Data"):
                            st.write(output.get("research_data", {}).keys())
                            
                    elif node == "writer":
                        st.write("✅ **Writer**: Sections drafted.")
                    
                    elif node == "editor":
                        st.write("✅ **Editor**: Final report compiled.")
                        # This works because editor outputs final_report
                        final_report = output.get("final_report", "")

            status.update(label="Research Complete!", state="complete", expanded=False)
            
        # Display Report
        st.divider()
        st.header(f"Final Report: {topic}")
        st.markdown(final_report)
