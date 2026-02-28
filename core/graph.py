from langgraph.graph import StateGraph, START, END
from core.state import ContentState
from core.agents import analyze_voice, reel_agent, carousel_agent, twitter_agent, static_agent

workflow = StateGraph(ContentState)

workflow.add_node("analyzer", analyze_voice)
workflow.add_node("reel", reel_agent)
workflow.add_node("carousel", carousel_agent)
workflow.add_node("twitter", twitter_agent)
workflow.add_node("static", static_agent)

# First, analyze the voice
workflow.add_edge(START, "analyzer")

# Then, run all 4 content generators IN PARALLEL
workflow.add_edge("analyzer", "reel")
workflow.add_edge("analyzer", "carousel")
workflow.add_edge("analyzer", "twitter")
workflow.add_edge("analyzer", "static")

# Connect all outputs to the end
workflow.add_edge("reel", END)
workflow.add_edge("carousel", END)
workflow.add_edge("twitter", END)
workflow.add_edge("static", END)

# Compile it into the variable that main.py is looking for
content_machine = workflow.compile()