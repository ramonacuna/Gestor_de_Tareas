from pydantic import BaseModel

class CrearTarea(BaseModel):
    titulo : str
    descripcion : str

class ActualizarTarea(BaseModel):
    titulo: str
    descripcion: str
    completado: bool

class RespuestaTarea(BaseModel):
    id : int
    titulo : str
    descripcion: str 
    completado: bool

    class Config:
        orm_mode = True



