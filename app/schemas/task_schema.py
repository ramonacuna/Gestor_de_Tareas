from pydantic import BaseModel

class CrearTarea(BaseModel):
    title : str
    description : str

class ActualizarTarea(BaseModel):
    title: str
    description: str
    completed: bool

class RespuestaTarea(BaseModel):
    id : int
    title : str
    description: str 
    completed: bool

    class Config:
        orm_attributes = True



        