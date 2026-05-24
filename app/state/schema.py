from typing import TypedDict, List, Dict, Any

class LearningState(TypedDict):
    topic: str
    checkpoints: List[Dict[str, Any]]
    current_checkpoint_index: int
    score: float
    completed_checkpoints: List[str]
    messages: List[str]
    retry_count: int
    vectorstore: Any