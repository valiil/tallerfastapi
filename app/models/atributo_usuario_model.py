from pydantic import BaseModel

class AtributoUsuario(BaseModel):
    id_usuario: int
    id_atributo: int
    valor: str
    descripcion: str
