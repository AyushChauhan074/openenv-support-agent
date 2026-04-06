from fastapi import FastAPI
from env.environment import SupportEnv
from env.actions import Action
from env.grader import grade
from env.tasks import TASKS

app = FastAPI()
env = SupportEnv()
trajectory = []
current_task = "easy"

@app.post("/reset")
def reset(task: str = "easy"):
    global trajectory, current_task
    trajectory = []
    current_task = task
    return env.reset(task)

@app.post("/step")
def step(action: Action):
    obs, reward, done, _ = env.step(action)

    trajectory.append({
        "action": action.action_type,
        "value": action.content
    })

    return {
        "observation": obs,
        "reward": reward,
        "done": done
    }

@app.get("/state")
def state():
    return env.state_view()

@app.get("/tasks")
def tasks():
    return list(TASKS.keys())

@app.post("/grader")
def run_grader():
    return {"score": grade(TASKS[current_task], trajectory, env.state)}