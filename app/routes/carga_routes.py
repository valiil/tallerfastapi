from fastapi import APIRouter, HTTPException
from controllers.carga_controller import CargaController  # Cambiado a CargaController
from models.carga_model import Carga  # Cambiado a Carga

router = APIRouter()

nuevo_carga = CargaController()  # Cambiado a CargaController

@router.post("/create_carga")  # Cambiado a create_carga
async def create_carga(carga: Carga):  # Cambiado a Carga
    rpta = nuevo_carga.create_carga(carga)  # Cambiado a create_carga
    return rpta

@router.get("/get_carga/{carga_id}", response_model=Carga)  # Cambiado a get_carga
async def get_carga(carga_id: int):  # Cambiado a get_carga
    rpta = nuevo_carga.get_carga(carga_id)  # Cambiado a get_carga
    return rpta

@router.get("/get_cargas/")  # Cambiado a get_cargas
async def get_cargas():  # Cambiado a get_cargas
    rpta = nuevo_carga.get_cargas()  # Cambiado a get_cargas
    return rpta

@router.put("/update_carga/{carga_id}")  # Cambiado a update_carga
async def update_carga(carga_id: int, carga: Carga):  # Cambiado a Carga
    rpta = nuevo_carga.update_carga(carga_id, carga)  # Cambiado a update_carga
    return rpta

@router.delete("/delete_carga/{carga_id}")  # Cambiado a delete_carga
async def delete_carga(carga_id: int):  # Cambiado a delete_carga
    rpta = nuevo_carga.delete_carga(carga_id)  # Cambiado a delete_carga
    return rpta
