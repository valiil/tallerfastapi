from pydantic import BaseModel


class Transporte(BaseModel):
    matricula:str
    modelo: str
    tipo: str
    color: str
    capacidad:int
    alto: str
    ancho: float
    largo: float
    ano: int
    id_perfil:int
    