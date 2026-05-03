from langgraph.graph import StateGraph, END
from app.graph.states.state import BloodRequestState
from app.graph.nodes.intake_request_node import intake_request_node, last_node


builder = StateGraph(BloodRequestState)
builder.add_node("intake_request", intake_request_node)
builder.add_node("last_node", last_node)
builder.set_entry_point("intake_request")

builder.add_edge("intake_request", "last_node")
builder.add_edge("last_node", END)
graph = builder.compile()




