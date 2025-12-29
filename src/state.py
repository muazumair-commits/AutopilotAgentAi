from typing import TypedDict, List, Dict, Annotated
import operator

class AgentState(TypedDict):
    topic: str
    research_plan: List[str]
    research_data: Dict[str, str]  # Map of question -> synthesized findings
    draft_sections: Dict[str, str] # Map of section title -> content
    final_report: str
    iteration: int
