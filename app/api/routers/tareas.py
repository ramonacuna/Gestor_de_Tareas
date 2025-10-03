from fastapi import APIRouter, Depends,HTTPException
from typing import List
from app.schemas.task_schema import CrearTarea,ActualizarTarea,RespuestaTarea
from app.repositories.task_repository import MemoriaRepositorio
from app.services.task_service import ServicioTarea

router = APIRouter()

#Inyeccion dependencia
#def get_servicioTarea():
#repositorio = MemoriaRepositorio()
#return ServicioTarea(repositorio)

repositorio = MemoriaRepositorio()
servicio = ServicioTarea(repositorio)
def get_servicioTarea():
    return servicio

@router.post("/", response_model=RespuestaTarea)
def crearTarea(tarea: CrearTarea, servicio: ServicioTarea = Depends(get_servicioTarea)):
    return servicio.crearTarea(tarea)

@router.get("/", response_model=List[RespuestaTarea])
def listarTareas(servicio: ServicioTarea = Depends(get_servicioTarea)):
    return servicio.listarTareas()

@router.get("/{idTarea}", response_model=RespuestaTarea)
def traerTarea(idTarea: int, servicio:ServicioTarea = Depends(get_servicioTarea)):
    try:
        return servicio.traerTarea(idTarea)
    except ValueError:
        raise HTTPException(status_code=404,detail="No se encontro la tarea")
    
@router.delete("/{idTarea}")
def borrarTarea(idTarea: int, service: ServicioTarea = Depends(get_servicioTarea)):
    service.borrarTarea(idTarea)
    return{"message":"Tarea borrada"}