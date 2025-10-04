# from typing import Optional
# from pydantic import BaseModel

# class Tarea(BaseModel):
#     id: int
#     titulo: str
#     descripcion: Optional[str] = None
#     completado: bool = False

class Tarea:
    def __init__(self, id: int, title: str, description: str, completed: bool = False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed