from app.services.llm import invoke_llm


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

    try:
        response = invoke_llm(prompt, timeout=12)
        explanation = response.content
    except Exception as exc:
        print("Feynman LLM invoke failed or timed out, using fallback explanation:\n", exc)
        explanation = "The AI tutor is currently unavailable for a full explanation, but here are the key ideas: neurons pass signals, weights control influence, and activation functions decide whether a signal should continue."

    state["feynman_explanation"] = explanation

    print("\nFeynman Explanation:\n")

    print(explanation)
    state["retry_count"] += 1

    print(f"\nRetry Count: {state['retry_count']}")

    return state