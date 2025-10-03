from typing import List
from app.models.tarea import Tarea
from app.schemas.task_schema import CrearTarea,ActualizarTarea
from app.repositories.task_repository import InterfazRepositorio
from fastapi import HTTPException

class ServicioTarea:
    #Constructor
    def __init__(self, repositorio: InterfazRepositorio):
        self.repositorio = repositorio
    #Getters and Setter
    def crearTarea(self, datosTarea: CrearTarea) -> Tarea:
        tarea = Tarea(id=0, titulo=datosTarea.titulo, descripcion=datosTarea.descripcion)
        return self.repositorio.add(tarea)
    
    def listarTareas(self) -> List[Tarea]:
        return self.repositorio.get_all()
    
    def traerTarea(self, idTarea: int) -> Tarea:
        tarea = self.repositorio.get_by_id(idTarea)
        if not tarea:
            raise ValueError("Tarea no encontrada")
        return tarea
    
    def actualizarTarea(self, idTarea: int, datosTarea: ActualizarTarea):
        tareaVieja = self.traerTarea(idTarea)

        tareaActualizada = Tarea(id=tareaVieja.id,
                                 titulo=datosTarea.titulo,
                                 descripcion=datosTarea.descripcion,
                                 completado=datosTarea.completado
                                 )     
        return self.repositorio.update(tareaVieja)
    
    def borrarTarea(self, idtarea : int):
        self.repositorio.delete(idtarea)