from app.services.llm import llm


def generate_questions(state):

    print("\n=== QUESTION GENERATION NODE ===")

    checkpoint = state["current_checkpoint"]

    title = checkpoint["title"]

    objectives = checkpoint["objectives"]

    prompt = f"""
    Generate 3 conceptual questions.

    Topic:
    {title}

    Objectives:
    {objectives}

    Focus on:
    - reasoning
    - conceptual understanding
    - application

    Return only questions.
    """

    response = llm.invoke(prompt)

    questions = response.content.strip().split("\n")

    cleaned_questions = [
        q.strip("- ").strip()
        for q in questions
        if q.strip()
    ]

    state["generated_questions"] = cleaned_questions

    print("\nGenerated Questions:")

    for q in cleaned_questions:
        print(f"- {q}")

    return state