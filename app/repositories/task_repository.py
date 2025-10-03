from app.models.tarea import Tarea
from typing import List,Optional


class InterfazRepositorio:

    def add(self, tarea: Tarea) -> Tarea:
        pass

    def get_all(self) -> List[Tarea]:
        pass

    def get_by_id(self, task_id: int) -> Optional[Tarea]:
        pass

    def update(self, tarea: Tarea) -> Tarea:
        pass

    def delete(self, tarea_id: int) -> None:
        pass

class MemoriaRepositorio(InterfazRepositorio):
    def __init__(self):
        self._tareas: List[Tarea] = []
        self._contador = 1

    
    def add(self, tarea: Tarea) -> Tarea:
        tarea.id = self._contador
        self._contador += 1
        self._tareas.append(tarea)
        return tarea

    def get_all(self) -> List[Tarea]:
        return self._tareas

    def get_by_id(self, tarea_id: int) -> Optional[Tarea]:
        return next((t for t in self._tareas if t.id == tarea_id),None)

    def update(self, tarea: Tarea) -> Tarea:
        for i,t in enumerate(self._tareas):
            if t.id == tarea.id :
                self._tareas[i] = tarea
                return tarea
        raise ValueError("Tarea no encontrada")

    def delete(self, tarea_id: int) -> None:
        self._tareas = [t for t in self._tareas if t.id != tarea_id]
