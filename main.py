from app.graph.workflow import graph
from app.rag.initialize import build_rag_pipeline
from app.models.state import LearningState
import json

if __name__ == "__main__":

    print("\n=== INITIALIZING RAG ===")

    # Build vector database
    vectorstore = build_rag_pipeline(
        "data/notes/neural_networks.txt"
    )

    # Initial workflow state
    initial_state: LearningState = {

        "topic": "Neural Networks",

        "checkpoints": [

            {
                "id": "cp1",
                "title": "Neural Network Basics",

                "objectives": [
                    "Understand neurons",
                    "Understand weights",
                    "Understand activation functions"
                ],

                "threshold": 0.7
            },

            {
                "id": "cp2",
                "title": "Forward Propagation",

                "objectives": [
                    "Understand input flow",
                    "Understand weighted sums",
                    "Understand prediction generation"
                ],

                "threshold": 0.7
            },

            {
                "id": "cp3",
                "title": "Backpropagation",

                "objectives": [
                    "Understand loss calculation",
                    "Understand gradient descent",
                    "Understand weight updates"
                ],

                "threshold": 0.7
            }

        ],

        "current_checkpoint_index": 0,

        "current_checkpoint": None,

        "generated_questions": [],

        "learner_answers": [],

        "retrieved_context": "",

        "weak_areas": [],

        "feynman_explanation": "",

        "score": 0.0,

        "completed": False,

        "session_complete": False,

        "messages": [],

        "completed_checkpoints": [],

        "retry_count": 0,

        "vectorstore": vectorstore
    }

    print("\n=== STARTING SESSION ===\n")

    try:

        result = graph.invoke(initial_state)

        print("\n=== FINAL RESULT ===\n")

        print(result)
        with open("sessions/session_001.json", "w") as f:
            json.dump(result, f, indent=4)
        print("\nSession saved successfully.")

    except Exception as e:

        print("\n=== ERROR OCCURRED ===\n")

        print(e)