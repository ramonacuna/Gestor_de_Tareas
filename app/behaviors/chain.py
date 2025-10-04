from app.models.tarea import Tarea
from app.repositories.base import InterfazRepositorio

class Handler:
    def __init__(self, next_handler=None):
        self.next = next_handler

    def handle(self, tarea: Tarea):
        if self.next:
            return self.next.handle(tarea)
        return tarea

class TitleLengthValidator(Handler):
    def handle(self, tarea: Tarea):
        if len(tarea.title) < 3:
            raise ValueError("El título de la tarea es demasiado corto")
        return super().handle(tarea)

class DuplicateValidator(Handler):
    def __init__(self, repo: InterfazRepositorio, next_handler=None):
        super().__init__(next_handler)
        self.repo = repo

    def handle(self, tarea: Tarea):
        if any(t.title == tarea.title for t in self.repo.get_all()):
            raise ValueError("La tarea ya existe")
        return super().handle(tarea)