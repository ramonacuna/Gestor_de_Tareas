from fastapi import FastAPI
from app.api.routers import tareas

app = FastAPI(title="Gestor de Tareas API")

app.include_router(tareas.router, prefix="/Tareas", tags=["Tareas"])