from fastapi import APIRouter, HTTPException
from controllers.transporte_controller import *
from models.transporte_model import Transporte

router = APIRouter()

nuevo_transporte = TransporteController()


@router.post("/create_transporte")
async def create_transporte(transporte: Transporte):
    rpta = nuevo_transporte.create_transporte(transporte)
    return rpta


@router.get("/get_transporte/{transporte_id}", response_model=Transporte)
async def get_transporte(transporte_id: int):
    rpta = nuevo_transporte.get_transporte(transporte_id)
    return rpta

@router.get("/get_transportes/")
async def get_transportes():
    rpta = nuevo_transporte.get_transportes()
    return rpta

@router.put("/update_transporte/{transporte_id}")
async def update_transporte(transporte_id: int, transporte: Transporte):
    rpta = nuevo_transporte.update_transporte(transporte_id, transporte)
    return rpta

@router.delete("/delete_transporte/{transporte_id}")
async def delete_transporte(transporte_id: int):
    rpta = nuevo_transporte.delete_transporte(transporte_id)
    return rpta
