from fastapi import APIRouter, HTTPException
from controllers.cargaTransportador_controller import CargaTransportadorController

router = APIRouter()
carga_transportador_controller = CargaTransportadorController()

@router.get("/cargas/transportador/{transportador_id}")
async def get_cargas_por_transportador(transportador_id: int):
    return carga_transportador_controller.get_cargas_por_transportador(transportador_id)
