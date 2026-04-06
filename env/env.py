from state import Observation, InternalState
from reward import compute_reward
from tasks import TASKS, inject_noise
from generator import generate_ticket

class SupportEnv:
    def __init__(self):
        self.state = None
        self.task = None

    def reset(self, task_name=None):
        if task_name and task_name in TASKS:
            task = TASKS[task_name]
        else:
            task = generate_ticket()

        # Noisy query is already included in generate_ticket for dynamic tasks,
        # but for static tasks we add it here.
        if task_name:
            task["query"] = inject_noise(task["query"])

        self.task = task
        self.state = InternalState(
            ticket_id="T1",
            customer_query=task["query"],
            true_category=task["category"],
            true_urgency=task["urgency"],
            sentiment=task["sentiment"],
            complexity=task["complexity"]
        )

        return self._get_obs()

    def step(self, action):
        predicted = action.content

        obs, reward, done = None, 0, False

        reward = compute_reward(self.state, action, predicted)

        self.state.history.append(f"{action.action_type}:{action.content}")

        if action.action_type == "resolve" and self.state.resolved:
            done = True

        obs = self._get_obs()

        return obs, reward, done, {}

    def state_view(self):
        return self.state.dict()

    def _get_obs(self):
        return Observation(
            ticket_id=self.state.ticket_id,
            customer_query=self.state.customer_query,
            history=self.state.history,
            resolved=self.state.resolved,
            satisfaction=self.state.satisfaction
        )
