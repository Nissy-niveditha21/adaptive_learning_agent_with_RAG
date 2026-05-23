from langgraph.graph import StateGraph, END

from app.models.state import LearningState

from app.nodes.start_node import start_learning
from app.nodes.checkpoint_node import checkpoint_node
from app.nodes.question_node import generate_questions
from app.nodes.assessment_node import assess_answers
from app.nodes.pass_node import pass_node
from app.nodes.fail_node import fail_node
from app.nodes.progress_node import progress_node
from app.nodes.router import evaluate_score
from app.nodes.session_router import continue_or_end
from app.nodes.feynman_node import feynman_teaching
from app.nodes.retry_router import retry_or_end
workflow = StateGraph(LearningState)

# -------------------------
# ADD NODES
# -------------------------

workflow.add_node("start", start_learning)

workflow.add_node("checkpoint", checkpoint_node)

workflow.add_node("question_node", generate_questions)

workflow.add_node("assessment_node", assess_answers)

workflow.add_node("pass_node", pass_node)

workflow.add_node("fail_node", fail_node)

workflow.add_node("progress_node", progress_node)

workflow.add_node(
    "feynman_node",
    feynman_teaching
)
workflow.add_conditional_edges(
    "feynman_node",
    retry_or_end,
    {
        "retry": "question_node",
        "end": END
    }
)

# -------------------------
# ENTRY POINT
# -------------------------

workflow.set_entry_point("start")


# -------------------------
# MAIN FLOW
# -------------------------

workflow.add_edge("start", "checkpoint")

workflow.add_edge("checkpoint", "question_node")

workflow.add_edge("question_node", "assessment_node")


# -------------------------
# PASS / FAIL ROUTING
# -------------------------

workflow.add_conditional_edges(
    "assessment_node",
    evaluate_score,
    {
        "pass_node": "pass_node",
        "fail_node": "fail_node"
    }
)


# -------------------------
# PASS FLOW
# -------------------------

workflow.add_edge("pass_node", "progress_node")


# -------------------------
# SESSION CONTINUATION
# -------------------------

workflow.add_conditional_edges(
    "progress_node",
    continue_or_end,
    {
        "continue": "checkpoint",
        "end": END
    }
)


# -------------------------
# FAIL FLOW
# -------------------------

workflow.add_edge("fail_node", "feynman_node")


# -------------------------
# COMPILE
# -------------------------

graph = workflow.compile()