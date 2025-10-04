from typing import List
from app.models.tarea import Tarea

class SortStrategy:
    def sort(self, tareas: List[Tarea]) -> List[Tarea]:
        return tareas

class SortByTitle(SortStrategy):
    def sort(self, tareas: List[Tarea]) -> List[Tarea]:
        return sorted(tareas, key=lambda t: t.title)

class SortByCompleted(SortStrategy):
    def sort(self, tarea: List[Tarea]) -> List[Tarea]:
        return sorted(tarea, key=lambda t: t.completed)

class SortById(SortStrategy):
    def sort(self, tareas: List[Tarea]) -> List[Tarea]:
        return sorted(tareas, key=lambda t: t.id)