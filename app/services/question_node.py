from app.services.llm import llm


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

    try:

        response = llm.invoke(prompt)

        questions = response.content.strip().split("\n")

        cleaned_questions = [
        q.replace("-", "").strip()
        for q in questions
        if q.strip() and "Here are" not in q
]

    except Exception as e:

        print("\nLLM FAILED — USING FALLBACK QUESTIONS")
        print(e)

        cleaned_questions = [
            "What is a neuron?",
            "Why are weights important?",
            "Why do activation functions matter?"
        ]

    state["generated_questions"] = cleaned_questions

    print("\nGenerated Questions:")

    for q in cleaned_questions:
        print(f"- {q}")

    return state