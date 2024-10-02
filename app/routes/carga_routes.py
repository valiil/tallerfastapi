from fastapi import APIRouter, HTTPException
from app.controllers.carga_controller import CargaController  
from app.models.carga_model import Carga  

router = APIRouter()

nuevo_carga = CargaController()  

@router.post("/create_carga")  
async def create_carga(carga: Carga):  
    rpta = nuevo_carga.create_carga(carga)  
    return rpta

@router.get("/get_carga/{carga_id}", response_model=Carga)  
async def get_carga(carga_id: int):  
    rpta = nuevo_carga.get_carga(carga_id)  
    return rpta

@router.get("/get_cargas/")  
async def get_cargas():  
    rpta = nuevo_carga.get_cargas()  
    return rpta

@router.put("/update_carga/{carga_id}")  
async def update_carga(carga_id: int, carga: Carga):  
    rpta = nuevo_carga.update_carga(carga_id, carga)  

@router.delete("/delete_carga/{carga_id}")  
async def delete_carga(carga_id: int):  
    rpta = nuevo_carga.delete_carga(carga_id)  
    return rpta
