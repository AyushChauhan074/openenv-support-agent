from pydantic import BaseModel
from typing import List, Optional

class Observation(BaseModel):
    ticket_id: str
    customer_query: str
    category: Optional[str] = None
    urgency: Optional[str] = None
    history: List[str] = []
    resolved: bool = False
    satisfaction: float = 0.5

class InternalState(BaseModel):
    ticket_id: str
    customer_query: str

    true_category: str
    true_urgency: str

    sentiment: str
    complexity: float

    attempts: int = 0
    classified: bool = False
    prioritized: bool = False
    resolved: bool = False

    satisfaction: float = 0.5
    history: List[str] = []