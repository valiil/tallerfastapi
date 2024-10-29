from fastapi import APIRouter, HTTPException
from controllers.atributo_controller import AtributoController  
from models.atributo_model import Atributo  

router = APIRouter()

nuevo_atributo = AtributoController()  

@router.post("/create_atributo")  
async def create_atributo(atributo: Atributo):  
    rpta = nuevo_atributo.create_atributo(atributo)  
    return rpta

@router.get("/get_atributo/{atributo_id}", response_model=Atributo)  
async def get_atributo(atributo_id: int):  
    rpta = nuevo_atributo.get_atributo(atributo_id)  
    return rpta

@router.get("/get_atributos/")  
async def get_atributos():  
    rpta = nuevo_atributo.get_atributos()  
    return rpta

@router.put("/update_atributo/{atributo_id}")  
async def update_atributo(atributo_id: int, atributo: Atributo):  
    rpta = nuevo_atributo.update_atributo(atributo_id, atributo)  
    return rpta

@router.delete("/delete_atributo/{atributo_id}") 
async def delete_atributo(atributo_id: int):  
    rpta = nuevo_atributo.delete_atributo(atributo_id) 
    return rpta

