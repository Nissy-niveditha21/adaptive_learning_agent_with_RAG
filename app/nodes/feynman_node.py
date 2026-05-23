from app.services.llm import llm


def feynman_teaching(state):

    print("\n=== FEYNMAN TEACHING NODE ===")

    weak_areas = state["weak_areas"]

    checkpoint = state["current_checkpoint"]

    prompt = f"""
Explain these concepts very simply.

Weak Areas:
{weak_areas}

Rules:
- beginner friendly
- use analogies
- avoid technical jargon
- short explanations
"""

    response = llm.invoke(prompt)

    explanation = response.content

    state["feynman_explanation"] = explanation

    print("\nFeynman Explanation:\n")

    print(explanation)
    state["retry_count"] += 1

    print(f"\nRetry Count: {state['retry_count']}")

    return state