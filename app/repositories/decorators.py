from app.models.tarea import Tarea
from app.repositories.base import InterfazRepositorio

class TareaRepositoryLogger(InterfazRepositorio):
    def __init__(self, wrapped: InterfazRepositorio):
        self._wrapped = wrapped

    def add(self, tarea: Tarea) -> Tarea:
        print(f"[LOG] Agregando tarea: {tarea.title}")
        return self._wrapped.add(tarea)

    def get_all(self):
        print("[LOG] Revisando todas las tareas")
        return self._wrapped.get_all()

    def get_by_id(self, tarea_id: int):
        print(f"[LOG] Revisando tarea {tarea_id}")
        return self._wrapped.get_by_id(tarea_id)

    def update(self, tarea: Tarea):
        print(f"[LOG] Actualizando tarea {tarea.id}")
        return self._wrapped.update(tarea)

    def delete(self, tarea_id: int):
        print(f"[LOG] Borrando tarea {tarea_id}")
        return self._wrapped.delete(tarea_id)