from typing import List
from app.models.tarea import Tarea
from app.repositories.base import InterfazRepositorio

#Aplicamos un singleton para que solo exista una unica instancia del repositorio en memoria 

class MemoriaRepositorio(InterfazRepositorio):
    _instance = None 

    def __new__(cls):
         if cls._instance is None:
             cls._instance = super(MemoriaRepositorio, cls).__new__(cls)
             cls._instance.tareas = []
             cls._instance.counter = 1
         return cls._instance

    def add(self, tarea: Tarea) -> Tarea:
        tarea.id = self._instance.counter
        self._instance.counter += 1
        self._instance.tareas.append(tarea)
        return tarea

    def get_all(self) -> List[Tarea]:
        return self._instance.tareas

    def get_by_id(self, tarea_id: int) -> Tarea:
         return next((t for t in self._instance.tareas if t.id == tarea_id), None)   
     
    def update(self, tarea: Tarea) -> Tarea:
         for i, t in enumerate(self._instance.tareas):
             if t.id == tarea.id:
                 self._instance.tareas[i] = tarea
                 return tarea
         return None    
    def delete(self, tarea_id: int):
        self._instance.tareas = [t for t in self._instance.tareas if t.id != tarea_id]

