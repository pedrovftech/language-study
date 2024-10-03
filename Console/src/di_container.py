from study.services.newStudyService import NewStudiesService
from study.services.reviewStudyService import ReviewStudiesService


class DIContainer:
    def __init__(self):
        self.workers = {
            1: NewStudiesService,
            2: ReviewStudiesService
        }

    def get_worker(self, choice):
        worker_class = self.workers.get(choice)
        if not worker_class:
            raise ValueError("Invalid option.")
        return worker_class()    
