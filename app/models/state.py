from typing import TypedDict, List, Dict


class LearningState(TypedDict):

    topic: str

    checkpoints: List[Dict]

    current_checkpoint_index: int

    current_checkpoint: Dict

    generated_questions: List[str]

    learner_answers: List[str]

    weak_areas: List[str]

    feynman_explanation: str

    score: float

    completed: bool

    session_complete: bool

    messages: List[str]

    completed_checkpoints: List[str]
    retry_count: int