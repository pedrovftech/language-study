import json
from typing import List
from study.domain.Concept import Concept
from study.domain.Subject import Subject


class NewStudiesService():
    def read_json_file(self, file_path: str) -> List[Subject]:
        subjects = []    
        with open(file_path, 'r', encoding='utf-8') as file:            
            data = json.load(file)

            for item in data:
                print(item["title"])
                subject = Subject(title=item["title"])
                for concept_data in item["concepts"]:
                    concept = Concept(
                        subject_id=subject.id,
                        question=concept_data["question"],
                        correct_text=concept_data["correct_text"],
                        options=concept_data["options"]
                    )
                    subject.concepts.append(concept)
                subjects.append(subject)

        return subjects
    
    def ask_question(self, subject):
        print(f"\nTopic: {subject.title}")
    
    def get_response(self, concept):
        question = concept.question
        correct_answer = concept.correct_text
        options = ", ".join(concept.options)
                
        return input(f"{question} ({options}): ").strip()

    def ask_questions(self, subjects: List[Subject]):
        for subject in subjects:
            self.ask_question(subject)

            for concept in subject.concepts:
                response = self.get_response(concept)
                
                # Check the answer
                if response.lower() == concept.correct_text.lower():
                    print("Correct!")
                else:
                    print(f"Incorrect. The correct answer is '{correct_answer}'.")
    
    def execute(self):
        subjects = self.read_json_file('data.json')

        self.ask_questions(subjects)