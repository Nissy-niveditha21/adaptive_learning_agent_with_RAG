from app.graph.workflow import graph
from app.rag.initialize import build_rag_pipeline


if __name__ == "__main__":

    print("\n=== INITIALIZING RAG ===")

    vectorstore = build_rag_pipeline(
        "data/notes/neural_networks.txt"
    )

    initial_state = {
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
    "score": 0.0,
    "completed_checkpoints": [],
    "messages": [],
    "retry_count": 0,
    "vectorstore": vectorstore
}

    print("\n=== STARTING SESSION ===\n")

    result = graph.invoke(initial_state)

    print("\n=== FINAL RESULT ===\n")
    print(result)