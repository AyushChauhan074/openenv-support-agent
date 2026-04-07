from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import os

from env.env import SupportEnv
from env.actions import Action
from env.environment import grade

app = FastAPI(title="ScalorX OpenEnv API")

# Global environment instance
env = SupportEnv()

@app.get("/")
async def health_check():
    return {"status": "ok", "message": "Support Agent OpenEnv Running"}

class StepInput(BaseModel):
    action_type: str
    content: str

@app.post("/reset")
async def reset(task_name: Optional[str] = None):
    obs = env.reset(task_name=task_name)
    return obs.dict()

@app.post("/step")
async def step(input: StepInput):
    # Convert input to Action model for validation
    try:
        action = Action(action_type=input.action_type, content=input.content)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs.dict(),
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
async def get_state():
    if env.state is None:
        raise HTTPException(status_code=400, detail="Environment not initialized. Call /reset first.")
    return env.state_view()

@app.post("/grader")
async def get_grader():
    if env.state is None or env.task is None:
        raise HTTPException(status_code=400, detail="Environment not initialized.")
    
    # Reconstruct trajectory from history for the grade function
    # The history is stored as "action_type:content" in env.step
    trajectory = []
    for h in env.state.history:
        parts = h.split(":", 1)
        if len(parts) == 2:
            trajectory.append({"action": parts[0], "value": parts[1]})
            
    score = grade(env.task, trajectory, env.state)
    return {"score": score}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
