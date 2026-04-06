def grade(task, trajectory):
    score = 0

    correct_category = any(
        step["action"] == "classify" and step["value"] == task["category"]
        for step in trajectory
    )

    correct_urgency = any(
        step["action"] == "prioritize" and step["value"] == task["urgency"]
        for step in trajectory
    )

    resolved = any(
        step["action"] == "resolve"
        for step in trajectory
    )

    score += 0.3 if correct_category else 0
    score += 0.3 if correct_urgency else 0
    score += 0.4 if resolved else 0

    return round(score, 2)