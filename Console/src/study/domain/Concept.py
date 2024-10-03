from typing import List
import uuid

class Concept:
    def __init__(self, subject_id: uuid.UUID, question: str, correct_text: str, options: List[str]):
        self.id = uuid.uuid4()
        self.subject_id = subject_id
        self.question = question
        self.correct_text = correct_text
        self.options = options