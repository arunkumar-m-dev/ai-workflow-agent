from langgraph.graph import StateGraph
from typing import TypedDict
from dotenv import load_dotenv
load_dotenv()
# ---- State ----
class AgentState(TypedDict):
    user_input: str
    parsed: dict
    result: str

# ---- Nodes ----
def parser_node(state: AgentState):
    text = state["user_input"]
    return {
        "parsed": {
            "task": "run_report" if "report" in text else "unknown"
        }
    }

def decision_node(state: AgentState):
    task = state["parsed"]["task"]
    return {"parsed": {"task": task}}

def execution_node(state: AgentState):
    task = state["parsed"]["task"]
    return {"result": f"Executed task: {task}"}

# ---- Graph ----
builder = StateGraph(AgentState)
builder.add_node("parser", parser_node)
builder.add_node("decision", decision_node)
builder.add_node("execution", execution_node)

builder.set_entry_point("parser")
builder.add_edge("parser", "decision")
builder.add_edge("decision", "execution")

graph = builder.compile()