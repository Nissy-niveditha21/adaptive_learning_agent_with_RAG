#from langchain_google_genai import ChatGoogleGenerativeAI
import os
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

"""llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.3
)"""
model_name = os.getenv("OLLAMA_MODEL", "llama3:latest")
llm = ChatOllama(
    model=model_name,
    temperature=0.3
)


def invoke_llm(prompt, timeout=12):
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(llm.invoke, prompt)
        try:
            return future.result(timeout=timeout)
        except TimeoutError:
            future.cancel()
            raise TimeoutError("LLM invocation timed out")


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

    response = invoke_llm(prompt, timeout=12)
    content = response.content
    if isinstance(content, list):
        content = "\n".join(str(item) for item in content)
    else:
        content = str(content)

    questions = content.strip().split("\n")

    cleaned_questions = [
        q.replace("-", "").strip()
        for q in questions if q.strip()
    ]

    state["generated_questions"] = cleaned_questions

    print("\nGenerated Questions:")
    for q in cleaned_questions:
        print(f"- {q}")

    return state