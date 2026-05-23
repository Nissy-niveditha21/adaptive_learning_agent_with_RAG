def evaluate_score(state):

    print("\n=== ROUTER NODE ===")

    checkpoint = state["current_checkpoint"]

    threshold = checkpoint["threshold"]

    print(f"Score: {state['score']}")
    print(f"Threshold: {threshold}")

    if state["score"] >= threshold:
        return "pass_node"

    return "fail_node"