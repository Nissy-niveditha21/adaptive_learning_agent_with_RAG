from fastapi import FastAPI

from app.graph.workflow import graph
from app.rag.initialize import build_rag_pipeline

app = FastAPI()

vectorstore = None


@app.on_event("startup")
def startup_event():
    global vectorstore

    print("\n=== INITIALIZING RAG ===")

    vectorstore = build_rag_pipeline(
        "data/notes/neural_networks.txt"
    )


@app.get("/")
def home():
    return {
        "message": "Learning Agent API Running"
    }


@app.post("/start-session")
def start_session():

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
            }
        ],

        "current_checkpoint_index": 0,
        "score": 0.0,
        "completed_checkpoints": [],
        "messages": [],
        "retry_count": 0,
        "vectorstore": vectorstore
    }

    result = graph.invoke(initial_state)

    return result