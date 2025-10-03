from typing import Optional
from pydantic import BaseModel

class Tarea(BaseModel):
    id: int
    titulo: str
    descripcion: Optional[str] = None
    completado: bool = False