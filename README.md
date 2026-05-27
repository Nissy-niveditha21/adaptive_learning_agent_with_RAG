# AI Learning Agent

![AI Learning Agent Preview](frontend/public/learning-agent-hero.svg)

A polished AI tutoring application that combines a React + Vite frontend with a FastAPI-backed learning workflow. The system is designed to guide learners through structured checkpoints, generate conceptual questions, evaluate responses, and provide Feynman-style explanations grounded in retrieved source material.

## Overview

This project demonstrates an end-to-end learning assistant powered by:

- a modern frontend interface for interactive study sessions
- a Python backend for session orchestration and evaluation
- retrieval-augmented generation (RAG) using project notes
- structured learning checkpoints and feedback loops

### Key Components

- Frontend: `frontend/`
- Backend API: `api.py`
- Workflow logic: `app/graph/`
- RAG and retrieval setup: `app/rag/`
- Session state and evaluation logic: `app/models/`, `app/services/`

## Core Features

- Structured checkpoint-based learning flow
- AI-generated conceptual questions for deeper understanding
- Semantic answer evaluation and performance feedback
- Feynman-style explanatory responses rendered in markdown
- Session tracking, retry support, and progress monitoring
- Responsive, user-friendly dashboard experience

## Architecture

The application follows a simple but effective architecture:

1. The frontend starts a learning session through the API.
2. The backend initializes a RAG pipeline from the project notes.
3. The learning workflow generates questions, retrieves relevant context, and evaluates learner input.
4. The interface displays progress, feedback, and explanations to the user.

## Prerequisites

Before running the project locally, ensure you have:

- Python 3.10 or newer
- Node.js and npm
- A virtual environment for the backend (the repository already includes `venv/`)

## Getting Started

### 1. Start the backend

From the project root, run:

```powershell
cd d:\projects\Learning_agent_RAG
.\venv\Scripts\python.exe -m uvicorn api:app --reload --host 127.0.0.1 --port 8000
```

### 2. Start the frontend

From the frontend directory, run:

```powershell
cd d:\projects\Learning_agent_RAG\frontend
npm install
npm run dev -- --host 127.0.0.1 --port 5173
```

### 3. Open the application

Once both services are running, use:

- Frontend: http://127.0.0.1:5173
- Backend API: http://127.0.0.1:8000

## Project Structure

```text
.
├── api.py                  # FastAPI application entry point
├── main.py                 # Standalone workflow execution example
├── app/                    # Graph, RAG, models, services, and workflow logic
├── data/                   # Notes and reference materials used by the RAG pipeline
├── frontend/               # React + Vite interface
└── sessions/               # Stored session outputs
```

## Notes

- The frontend relies on `axios` and `react-markdown` for API interaction and formatted explanations.
- The main learning session begins with `POST /start-session`.
- The project is intended as a practical example of AI-powered educational assistance, retrieval-based context, and structured learning feedback.

## License

This project is provided for educational and development purposes.

