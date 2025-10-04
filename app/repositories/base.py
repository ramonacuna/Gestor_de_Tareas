from typing import List
from app.models.tarea import Tarea
from abc import ABC, abstractmethod

#Patron Repository Pattern aplicado al generar un contrato que deben manejar todos los repositorios

class InterfazRepositorio(ABC):

    @abstractmethod
    def add(self, tarea: Tarea) -> Tarea:
        pass
    @abstractmethod
    def get_all(self) -> List[Tarea]:
        pass
    @abstractmethod
    def get_by_id(self, Tarea_id: int) -> Tarea: 
        pass
    @abstractmethod
    def update(self, tarea: Tarea) -> Tarea:
        pass
    @abstractmethod
    def delete(self, tarea_id: int) -> None:
        pass