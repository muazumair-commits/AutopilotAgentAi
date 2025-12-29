from langgraph.graph import StateGraph, END
from src.state import AgentState
from src.agents.planner import planner_agent
from src.agents.researcher import researcher_agent
from src.agents.writer import writer_agent
from src.agents.editor import editor_agent

def create_graph():
    # 1. Initialize Graph
    workflow = StateGraph(AgentState)

    # 2. Add Nodes
    workflow.add_node("planner", planner_agent)
    workflow.add_node("researcher", researcher_agent)
    workflow.add_node("writer", writer_agent)
    workflow.add_node("editor", editor_agent)

    # 3. Define Edges (Linear Flow for v1)
    workflow.set_entry_point("planner")
    
    workflow.add_edge("planner", "researcher")
    workflow.add_edge("researcher", "writer")
    workflow.add_edge("writer", "editor")
    workflow.add_edge("editor", END)

    # 4. Compile
    app = workflow.compile()
    return app
