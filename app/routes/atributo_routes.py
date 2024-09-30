from fastapi import APIRouter, HTTPException
from controllers.atributo_controller import AtributoController  # Cambiado a AtributoController
from models.atributo_model import Atributo  # Cambiado a Atributo

router = APIRouter()

nuevo_atributo = AtributoController()  # Cambiado a AtributoController

@router.post("/create_atributo")  # Cambiado a create_atributo
async def create_atributo(atributo: Atributo):  # Cambiado a Atributo
    rpta = nuevo_atributo.create_atributo(atributo)  # Cambiado a create_atributo
    return rpta

@router.get("/get_atributo/{atributo_id}", response_model=Atributo)  # Cambiado a get_atributo
async def get_atributo(atributo_id: int):  # Cambiado a get_atributo
    rpta = nuevo_atributo.get_atributo(atributo_id)  # Cambiado a get_atributo
    return rpta

@router.get("/get_atributos/")  # Cambiado a get_atributos
async def get_atributos():  # Cambiado a get_atributos
    rpta = nuevo_atributo.get_atributos()  # Cambiado a get_atributos
    return rpta

@router.put("/update_atributo/{atributo_id}")  # Cambiado a update_atributo
async def update_atributo(atributo_id: int, atributo: Atributo):  # Cambiado a Atributo
    rpta = nuevo_atributo.update_atributo(atributo_id, atributo)  # Cambiado a update_atributo
    return rpta

@router.delete("/delete_atributo/{atributo_id}")  # Cambiado a delete_atributo
async def delete_atributo(atributo_id: int):  # Cambiado a delete_atributo
    rpta = nuevo_atributo.delete_atributo(atributo_id)  # Cambiado a delete_atributo
    return rpta

