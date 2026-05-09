from langgraph.graph import StateGraph, END
from app.graph.states.state import BloodRequestState
from app.graph.nodes.intake_request_node import intake_request_node, last_node
from app.graph.nodes.donor_search_node import donor_search_node
from app.graph.nodes.hospital_verification_node import hospital_verification_node



builder = StateGraph(BloodRequestState)
builder.add_node("intake_request", intake_request_node)
builder.add_node("donor_search", donor_search_node)
builder.add_node("hospital_verification", hospital_verification_node)
builder.add_node("last_node", last_node)
builder.set_entry_point("intake_request")

builder.add_edge("intake_request", "hospital_verification")
builder.add_edge("hospital_verification", "donor_search")
builder.add_edge("donor_search", "last_node")
builder.add_edge("last_node", END)
graph = builder.compile()




