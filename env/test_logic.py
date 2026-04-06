from state import InternalState, update_satisfaction
from actions import Action
from reward import compute_reward
from environment import grade, inject_noise

def test_logic():
    # Setup state
    state = InternalState(
        ticket_id="T1",
        customer_query="I have a billing issue.",
        true_category="Billing",
        true_urgency="High",
        sentiment="neutral",
        complexity=1.2,
        history=[]
    )

    print(f"Initial satisfaction: {state.satisfaction}")

    # Action: Respond with empathy
    action1 = Action(action_type="respond", content="I am sorry for the trouble.")
    update_satisfaction(state, action1)
    state.history.append("respond")
    print(f"After empathy respond: {state.satisfaction}")

    # Action: Classify correctly
    action2 = Action(action_type="classify", content="Billing")
    reward2 = compute_reward(state, action2, predicted="Billing")
    state.history.append("classify")
    print(f"Classification reward: {reward2}")

    # Action: Resolve with Technical (Consistency Penalty Test)
    action3 = Action(action_type="resolve", content="Technical")
    state.resolved = True
    reward3 = compute_reward(state, action3, predicted=None)
    print(f"Resolution reward (Billing history, Technical resolution): {reward3}")

    # Inject Noise Test
    query = "HELP"
    noisy_query = inject_noise(query)
    print(f"Noisy query: {noisy_query}")

    # Grading Test
    task = {"category": "Billing", "urgency": "High"}
    trajectory = [
        {"action": "classify", "value": "Billing"},
        {"action": "prioritize", "value": "High"},
        {"action": "respond", "value": "Sorry about that."},
        {"action": "resolve", "value": "Done"}
    ]
    final_score = grade(task, trajectory, state)
    print(f"Final Grade: {final_score}")

if __name__ == "__main__":
    test_logic()
