from pydantic import BaseModel
from datetime import date
from typing import Optional

class CargaPorEmpresa(BaseModel):
    id: int
    peso: float
    largo: float
    ancho: float
    alto: float
    tipo: str
    fecha_recogida: date
    fecha_entrega: date
    estado_actual: str
    origen: str
    destino: str
    descripcion: Optional[str] = None
