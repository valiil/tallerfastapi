from fastapi import APIRouter, HTTPException
from controllers.cargaEmpresa_controller import CargaEmpresaController

router = APIRouter()
carga_empresa_controller = CargaEmpresaController()

@router.get("/cargas/empresa/{empresa_id}")
async def get_cargas_por_empresa(empresa_id: int):
    return carga_empresa_controller.get_cargas_por_empresa(empresa_id)
