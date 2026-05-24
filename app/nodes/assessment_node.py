from app.services.semantic_evaluator import semantic_score
from app.data.reference_answers import REFERENCE_ANSWERS


def assess_answers(state):

    print("\n=== ASSESSMENT NODE ===")

    questions = state["generated_questions"]

    learner_answers = []

    total_score = 0

    weak_areas = []

    for q in questions:

        print(f"\nQuestion: {q}")

        answer = input("Your Answer: ")

        learner_answers.append(answer)
        bad_answers = ["no", "idk", "i dont know"]

        if answer.lower() in bad_answers:
            similarity = 0
        reference = REFERENCE_ANSWERS.get(q, "")

        score = semantic_score(
            reference,
            answer
        )

        print(f"Semantic Score: {score}")

        total_score += score

        if score < 0.6:
            weak_areas.append(q)

    final_score = total_score / len(questions)

    state["learner_answers"] = learner_answers

    state["score"] = final_score

    state["weak_areas"] = weak_areas

    print(f"\nFinal Score: {final_score}")

    return state