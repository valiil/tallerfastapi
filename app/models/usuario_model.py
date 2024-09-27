from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    usuario: str
    contrasena: str
    nombre: str
    apellido: str
    documento: str
    telefono: str
    id_perfil: int
    