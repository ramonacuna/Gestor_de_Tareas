from app.repositories.base import InterfazRepositorio
from app.models.tarea import Tarea

class SecureTareaRepositoryProxy(InterfazRepositorio):
    def __init__(self, wrapped: InterfazRepositorio, role: str):
        self._wrapped = wrapped
        self.role = role

    def _check_permission(self):
        if self.role != "admin":
            raise PermissionError("No tienes permisos para esta operación")

    def add(self, tarea: Tarea) -> Tarea:
        self._check_permission()
        return self._wrapped.add(tarea)

    def get_all(self):
        return self._wrapped.get_all()

    def get_by_id(self, tarea_id: int):
        return self._wrapped.get_by_id(tarea_id)

    def update(self, tarea: Tarea):
        self._check_permission()
        return self._wrapped.update(tarea)

    def delete(self, tarea_id: int):
        self._check_permission()
        return self._wrapped.delete(tarea_id)
