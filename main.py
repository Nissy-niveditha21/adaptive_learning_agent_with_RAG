from app.graph.workflow import graph

from app.services.checkpoints import CHECKPOINTS


initial_state = {

    "topic": "Neural Networks",

    "checkpoints": CHECKPOINTS,

    "current_checkpoint_index": 0,

    "current_checkpoint": {},

    "score": 0.0,

    "completed": False,

    "session_complete": False,

    "messages": [],

    "completed_checkpoints": [],
    "generated_questions": [],

    "learner_answers": [],

    "weak_areas": [],

    "feynman_explanation": "",
    "retry_count": 0
}


result = graph.invoke(initial_state)

print("\n=== FINAL STATE ===\n")

print(result)