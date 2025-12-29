import os
from src.graph import create_graph

# Mock keys to prevent init errors if checks present
os.environ["GEMINI_API_KEY"] = "mock_key"
os.environ["SERPAPI_API_KEY"] = "mock_key"

try:
    print("Initializing Graph...")
    app = create_graph()
    print("Graph compiled successfully.")
    
    print("Graph Structure:")
    # Printing the graph structure if available, or just success
    print("Nodes:", app.nodes.keys() if hasattr(app, 'nodes') else "Nodes initialized")
    
except Exception as e:
    print(f"FAILED to compile graph: {e}")
