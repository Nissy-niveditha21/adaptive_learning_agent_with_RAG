from pydantic import BaseModel
from typing import List


class Checkpoint(BaseModel):

    id: str

    title: str

    objectives: List[str]

    threshold: float = 0.7