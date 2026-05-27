from app.services.llm import invoke_llm


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

    try:
        response = invoke_llm(prompt, timeout=12)
        content = response.content
        if isinstance(content, list):
            content = "\n".join(str(item) for item in content)
        else:
            content = str(content)
        questions = content.strip().split("\n")
    except Exception as exc:
        print("LLM invoke failed or timed out, using fallback questions:\n", exc)
        questions = [
            "What is the role of weights in a neural network?",
            "How does an activation function affect neuron output?",
            "Why is forward propagation important in training?"
        ]

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