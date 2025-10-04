from typing import List
from app.models.tarea import Tarea

#Patron Repository Pattern aplicado al generar un contrato que deben manejar todos los repositorios

class InterfazRepositorio:

    def add(self, tarea: Tarea) -> Tarea:
        pass

    def get_all(self) -> List[Tarea]:
        pass

    def get_by_id(self, Tarea_id: int) -> Tarea: 
        pass

    def update(self, tarea: Tarea) -> Tarea:
        pass

    def delete(self, tarea_id: int) -> None:
        pass