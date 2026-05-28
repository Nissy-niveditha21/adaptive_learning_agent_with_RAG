# 🧠 AI Learning Agent

![AI Learning Agent Preview](frontend/public/learning-agent-hero.svg)

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-18+-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-5+-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![RAG](https://img.shields.io/badge/RAG-Enabled-8A2BE2?style=for-the-badge)

**An elegant AI tutoring platform that blends retrieval-augmented learning, structured checkpoints, and intelligent feedback into a polished educational workflow.**

</div>

---

## ✨ Overview

The **AI Learning Agent** is a guided study assistant built for active learning. It combines a polished React interface with a FastAPI backend and a graph-driven workflow that adapts learner progress, retrieves source context, and delivers explainable feedback in a tutorial-friendly flow.

### What makes it special

- **Adaptive learning workflow** with checkpoints, retries, and progress tracking.
- **Retrieval-Augmented Generation (RAG)** grounded in curated notes and reference material.
- **Conceptual questioning + Feynman-style explanations** to reinforce understanding.
- **Semantic evaluation** for answer quality, clarity, and conceptual coverage.
- **Modern dashboard UX** designed for responsive study sessions.

---

## 🧩 Core Architecture

```mermaid
flowchart LR
    classDef frontend fill:#0f172a,stroke:#22c55e,color:#f8fafc,stroke-width:2px;
    classDef api fill:#1e293b,stroke:#38bdf8,color:#f8fafc,stroke-width:2px;
    classDef workflow fill:#312e81,stroke:#a78bfa,color:#f8fafc,stroke-width:2px;
    classDef rag fill:#7c2d12,stroke:#fb923c,color:#f8fafc,stroke-width:2px;
    classDef results fill:#14532d,stroke:#4ade80,color:#f8fafc,stroke-width:2px;

    User["Learner"] -->|starts session| FE["React + Vite UI"]:::frontend
    FE -->|POST /start-session| API["FastAPI Backend"]:::api
    API -->|orchestrates| WF["Graph Workflow"]:::workflow
    WF -->|retrieves notes| RAG["RAG Pipeline"]:::rag
    RAG -->|context + answers| WF
    WF -->|progress & feedback| API
    API -->|renders outcome| FE
    FE -->|visualizes progress| RES["Session Insights"]:::results
```

---

## 🔁 Learning Loop

```mermaid
flowchart TD
    classDef start fill:#1e1b4b,stroke:#818cf8,color:#f8fafc,stroke-width:2px;
    classDef question fill:#0f172a,stroke:#22c55e,color:#f8fafc,stroke-width:2px;
    classDef retrieve fill:#7c2d12,stroke:#fb923c,color:#f8fafc,stroke-width:2px;
    classDef evaluate fill:#164e63,stroke:#22d3ee,color:#f8fafc,stroke-width:2px;
    classDef explain fill:#14532d,stroke:#4ade80,color:#f8fafc,stroke-width:2px;

    Start["Session Start"]:::start --> Ask["Generate Conceptual Question"]:::question
    Ask --> Retrieve["Retrieve Relevant Context"]:::retrieve
    Retrieve --> Answer["Learner Response"]
    Answer --> Evaluate["Semantic Evaluation"]:::evaluate
    Evaluate -->|feedback + score| Explain["Explain with Feynman-style reasoning"]:::explain
    Explain -->|retry or progress| Ask
```

---

## 🗂️ Key Modules

| Area | Purpose |
| --- | --- |
| `api.py` | FastAPI entry point and session API surface |
| `app/graph/` | Workflow orchestration and learning graph logic |
| `app/rag/` | Retrieval initialization and RAG setup |
| `app/services/` | Evaluation, retrievers, checkpoints, and session helpers |
| `frontend/` | React + Vite dashboard and study interface |
| `sessions/` | Saved session outputs and progress artifacts |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Node.js + npm
- A local virtual environment for Python dependencies

### 1. Start the backend

From the repository root:

```powershell
cd d:\projects\Learning_agent_RAG
.\venv\Scripts\python.exe -m uvicorn api:app --reload --host 127.0.0.1 --port 8000
```

### 2. Start the frontend

```powershell
cd d:\projects\Learning_agent_RAG\frontend
npm install
npm run dev -- --host 127.0.0.1 --port 5173
```

### 3. Open the application

- Frontend: http://127.0.0.1:5173
- Backend API: http://127.0.0.1:8000

---

## 📈 Project Highlights

- **Structured educational workflow** for guided tutoring and checkpoints.
- **Grounded explanations** connected to retrieval context.
- **Performance dashboards** for progress, retries, and session insights.
- **Production-ready patterns** for AI-assisted learning applications.

---

## 🧪 Notes

- The frontend uses `axios` and `react-markdown` for API communication and formatted instructional output.
- The primary learning session begins through `POST /start-session`.
- The repository serves as a practical blueprint for interactive educational agents, retrieval-based context, and adaptive feedback loops.

---

## 🎨 Presentation Notes

This README uses a refined visual structure with:

- **rich status badges** for stack clarity
- **Mermaid graphs** for architecture and learning flow
- **color-coded sections** to highlight major system components and stages

---

## 📄 License

This project is provided for educational, experimental, and development-focused use.

