from langgraph.graph import StateGraph
from langgraph.graph import START, END

from app.state import MedicalState

from app.agents.ocr_agent import ocr_agent
from app.agents.detection_agent import detection_agent
from app.agents.rag_agent import rag_agent
from app.agents.report_agent import report_agent


graph = StateGraph(MedicalState)


# -----------------------------------
# NODES
# -----------------------------------

graph.add_node("ocr", ocr_agent)

graph.add_node("detection", detection_agent)

graph.add_node("rag", rag_agent)

graph.add_node("report", report_agent)


# -----------------------------------
# EDGES
# -----------------------------------

graph.add_edge(START, "ocr")

graph.add_edge("ocr", "detection")

graph.add_edge("detection", "rag")

graph.add_edge("rag", "report")

graph.add_edge("report", END)


app_graph = graph.compile()