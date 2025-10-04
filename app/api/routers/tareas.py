from fastapi import APIRouter, Query
from app.schemas.task_schema import CrearTarea, ActualizarTarea
from app.repositories.factory import RepositoryFactory
from app.repositories.decorators import TareaRepositoryLogger
from app.repositories.proxies import SecureTareaRepositoryProxy
from app.services.task_service import TareaService
from app.facade.app_facade import AppFacade
from app.behaviors.strategy import SortById, SortByTitle, SortByCompleted

router = APIRouter()

repo = RepositoryFactory.create_repository()
repo = TareaRepositoryLogger(repo)
repo = SecureTareaRepositoryProxy(repo, role="admin")

tarea_service = TareaService(repo)
facade = AppFacade(tarea_service)

@router.post("/")
def create_tarea(tarea: CrearTarea):
    return facade.create_tarea(tarea)

@router.get("/")
def list_tareas(sort_by: str = Query("id", enum=["id", "title", "completed"])):
    strategies = {"id": SortById(), "title": SortByTitle(), "completed": SortByCompleted()}
    return facade.list_tareas(strategy=strategies.get(sort_by))

@router.put("/{tarea_id}")
def update_tarea(tarea_id: int, tarea: ActualizarTarea):
    return facade.update_tarea(tarea_id, tarea)

@router.delete("/{tarea_id}")
def delete_tarea(tarea_id: int):
    return facade.delete_tarea(tarea_id)
