def evaluate_answer(question, answer):

    answer = answer.lower()

    # extremely basic prototype scoring

    keywords = [
        "activation",
        "weight",
        "neuron",
        "prediction",
        "function"
    ]

    matches = 0

    for keyword in keywords:

        if keyword in answer:
            matches += 1

    score = matches / len(keywords)

    return min(score, 1.0)