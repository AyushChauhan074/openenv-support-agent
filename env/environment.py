from .semantic import semantic_similarity

def grade(task, trajectory, state):
    category_correct = any(
        t["action"] == "classify" and t["value"] == task["category"]
        for t in trajectory
    )

    urgency_correct = any(
        t["action"] == "prioritize" and t["value"] == task["urgency"]
        for t in trajectory
    )

    responses = [t["value"] for t in trajectory if t["action"] == "respond"]

    semantic_scores = [
        semantic_similarity("We are resolving your issue", r)
        for r in responses
    ]

    response_score = sum(semantic_scores) / (len(semantic_scores) + 1)

    resolved = any(t["action"] == "resolve" for t in trajectory)
    efficiency = max(0, 1 - len(trajectory) / 10)

    score = (
        0.2 * category_correct +
        0.2 * urgency_correct +
        0.2 * response_score +
        0.2 * resolved +
        0.1 * efficiency +
        0.1 * state.satisfaction
    )

    return round(score, 3)