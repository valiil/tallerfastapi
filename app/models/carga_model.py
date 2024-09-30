from pydantic import BaseModel
from datetime import date

class Carga(BaseModel):
    peso: float
    largo: float
    ancho: float
    alto: float
    descripcion: str
    fecha_recogida: date
    fecha_entrega: date
    estado_actual: str
    origen: str
    destino: str
    ubicacion: str
    tipo: str
    id_perfil: int
