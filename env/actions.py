from pydantic import BaseModel
from typing import Literal

class Action(BaseModel):
    action_type: Literal[
        "classify",
        "prioritize",
        "respond",
        "resolve"
    ]
    content: str