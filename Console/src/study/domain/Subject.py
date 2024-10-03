from typing import List
import uuid

from study.domain import Concept

class Subject:
    def __init__(self, title: str):
        self.id = uuid.uuid4()
        self.title = title
        self.concepts: List[Concept] = []