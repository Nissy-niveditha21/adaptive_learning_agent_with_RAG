def continue_or_end(state):

    print("\n=== SESSION ROUTER ===")

    if state["session_complete"]:
        return "end"

    return "continue"