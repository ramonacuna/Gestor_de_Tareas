from typing import List
from app.models.tarea import Tarea
from app.schemas.task_schema import CrearTarea, ActualizarTarea
from app.repositories.base import InterfazRepositorio
from app.behaviors.observer import tarea_created
from app.behaviors.strategy import SortStrategy
from app.behaviors.chain import TitleLengthValidator, DuplicateValidator

class TareaService:
    def __init__(self, repository: InterfazRepositorio):
        self.repository = repository

    def create_tarea(self, tarea_data: CrearTarea) -> Tarea:
        tarea = Tarea(id=0, title=tarea_data.title, description=tarea_data.description, completed=False)

        chain = TitleLengthValidator(DuplicateValidator(self.repository))
        chain.handle(tarea)

        new_tarea = self.repository.add(tarea)

        tarea_created.notify(new_tarea)

        return new_tarea

    def list_tareas(self, strategy: SortStrategy = None) -> List[Tarea]:
        tareas = self.repository.get_all()
        if strategy:
            return strategy.sort(tareas)
        return tareas

    def get_tarea(self, tarea_id: int) -> Tarea:
        tarea = self.repository.get_by_id(tarea_id)
        if not tarea:
            raise ValueError("Tarea not found")
        return tarea

    def update_tarea(self, tarea_id: int, tarea_data: ActualizarTarea) -> Tarea:
        tarea = self.get_tarea(tarea_id)
        tarea.title = tarea_data.title
        tarea.description = tarea_data.description
        tarea.completed = tarea_data.completed
        return self.repository.update(tarea)

    def delete_tarea(self, tarea_id: int):
        self.repository.delete(tarea_id)
