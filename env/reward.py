def compute_reward(state, action, predicted):
    reward = 0

    # dependency penalties
    if action.action_type == "prioritize" and not state.classified:
        return -0.3

    if action.action_type == "resolve" and not state.classified:
        return -0.4

    # classification
    if action.action_type == "classify":
        if predicted == state.true_category:
            reward += 0.25 * state.complexity
            state.classified = True
        else:
            reward -= 0.15

    # urgency
    if action.action_type == "prioritize":
        if predicted == state.true_urgency:
            reward += 0.2 * state.complexity
            state.prioritized = True
        else:
            reward -= 0.1

    # response
    if action.action_type == "respond":
        length_score = min(len(action.content) / 50, 1)
        empathy = 1 if "sorry" in action.content.lower() else 0
        clarity = 1 if "." in action.content else 0

        reward += 0.2 * (0.4 * length_score + 0.3 * empathy + 0.3 * clarity)

        # satisfaction dynamics
        if empathy:
            state.satisfaction += 0.1
        else:
            state.satisfaction -= 0.05

    # resolution
    if action.action_type == "resolve":
        if state.classified:
            state.resolved = True
            reward += 0.3 * state.satisfaction
        else:
            reward -= 0.3

    # penalties
    state.attempts += 1
    reward -= 0.05 * state.attempts

    state.satisfaction = max(0, min(1, state.satisfaction))

    return round(reward, 3)