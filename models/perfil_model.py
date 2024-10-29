from pydantic import BaseModel


class Perfil(BaseModel):
    nombre:str
    descripcion: str
    
    