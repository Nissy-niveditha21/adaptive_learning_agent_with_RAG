#from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

"""llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.3
)"""
llm = ChatOllama(
    model="llama3",
    temperature=0.3
)
def generate_questions(state):

    print("\n=== QUESTION GENERATION NODE ===")

    checkpoint = state["current_checkpoint"]
    context = state["retrieved_context"]

    prompt = f"""
    You are a tutor.

    Topic:
    {checkpoint['title']}

    Objectives:
    {checkpoint['objectives']}

    Study Material:
    {context}

    Generate 3 short conceptual questions.
    """

    response = llm.invoke(prompt)

    questions = response.content.strip().split("\n")

    cleaned_questions = [
        q.replace("-", "").strip()
        for q in questions if q.strip()
    ]

    state["generated_questions"] = cleaned_questions

    print("\nGenerated Questions:")

    for q in cleaned_questions:
        print(f"- {q}")

    return state