"""from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
#from app.api.routes import router
from app.graph.workflow import graph
from app.rag.initialize import build_rag_pipeline
from pydantic import BaseModel
app = FastAPI()

# CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#app.include_router(router)
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

    global vectorstore

    if vectorstore is None:
        vectorstore = build_rag_pipeline(
            "data/notes/neural_networks.txt"
        )

    response = {
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
        "current_checkpoint": {
            "id": "cp1",
            "title": "Neural Network Basics",
            "objectives": [
                "Understand neurons",
                "Understand weights",
                "Understand activation functions"
            ],
            "threshold": 0.7
        },
        "generated_questions": [
            "What is the role of weights in a neural network?",
            "How does an activation function affect neuron output?",
            "Why is forward propagation important in training?"
        ],
        "learner_answers": ["", "", ""],
        "weak_areas": [],
        "score": 0.0,
        "completed": False,
        "session_complete": False,
        "messages": [
            "Starting topic: Neural Networks",
            "Loaded checkpoint: Neural Network Basics"
        ],
        "completed_checkpoints": [],
        "retry_count": 0,
        "feynman_explanation": "",
        "retrieved_context": ""
    }

    return response"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.graph.workflow import graph
from app.rag.initialize import build_rag_pipeline

app = FastAPI()

# =========================
# CORS
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# GLOBAL VECTORSTORE
# =========================
vectorstore = None


# =========================
# REQUEST MODELS
# =========================
class EvaluationRequest(BaseModel):
    answers: list[str]


# =========================
# STARTUP
# =========================
@app.on_event("startup")
def startup_event():

    global vectorstore

    print("\n=== INITIALIZING RAG ===")

    vectorstore = build_rag_pipeline(
        "data/notes/neural_networks.txt"
    )


# =========================
# HOME ROUTE
# =========================
@app.get("/")
def home():

    return {
        "message": "Learning Agent API Running"
    }


# =========================
# START SESSION
# =========================
@app.post("/start-session")
def start_session():

    global vectorstore

    if vectorstore is None:

        vectorstore = build_rag_pipeline(
            "data/notes/neural_networks.txt"
        )

    response = {

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

        "current_checkpoint": {
            "id": "cp1",
            "title": "Neural Network Basics",
            "objectives": [
                "Understand neurons",
                "Understand weights",
                "Understand activation functions"
            ],
            "threshold": 0.7
        },

        "generated_questions": [
            "What is the role of weights in a neural network?",
            "How does an activation function affect neuron output?",
            "Why is forward propagation important in training?"
        ],

        "learner_answers": ["", "", ""],

        "weak_areas": [],

        "score": 0.0,

        "completed": False,

        "session_complete": False,

        "messages": [
            "Starting topic: Neural Networks",
            "Loaded checkpoint: Neural Network Basics"
        ],

        "completed_checkpoints": [],

        "retry_count": 0,

        "feynman_explanation": "",

        "retrieved_context": ""
    }

    return response


# =========================
# EVALUATE ANSWERS
# =========================
@app.post("/evaluate")
def evaluate_answers(data: EvaluationRequest):

    global vectorstore

    if vectorstore is None:

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
            }
        ],

        "current_checkpoint_index": 0,

        "score": 0.0,

        "completed_checkpoints": [],

        "messages": [],

        "retry_count": 0,

        "vectorstore": vectorstore,

        # USER ANSWERS
        "learner_answers": data.answers
    }

    result = graph.invoke(initial_state)

    return result