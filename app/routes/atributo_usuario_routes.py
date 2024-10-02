from fastapi import APIRouter, HTTPException
from app.controllers.atributo_usuario_controller import AtributoUsuarioController  
from app.models.atributo_usuario_model import AtributoUsuario  

router = APIRouter()

nuevo_atributo_usuario = AtributoUsuarioController()  

@router.post("/create_atributo_usuario")  
async def create_atributo_usuario(atributo_usuario: AtributoUsuario):  
    rpta = nuevo_atributo_usuario.create_atributo_usuario(atributo_usuario)  
    return rpta

@router.get("/get_atributo_usuario/{atributo_usuario_id}", response_model=AtributoUsuario)  
async def get_atributo_usuario(atributo_usuario_id: int):  
    rpta = nuevo_atributo_usuario.get_atributo_usuario(atributo_usuario_id)  
    return rpta

@router.get("/get_atributo_usuarios/")  
async def get_atributo_usuarios():  
    rpta = nuevo_atributo_usuario.get_atributo_usuarios()  
    return rpta

@router.put("/update_atributo_usuario/{atributo_usuario_id}")  
async def update_atributo_usuario(atributo_usuario_id: int, atributo_usuario: AtributoUsuario):  
    rpta = nuevo_atributo_usuario.update_atributo_usuario(atributo_usuario_id, atributo_usuario)  
    return rpta

@router.delete("/delete_atributo_usuario/{atributo_usuario_id}")  
async def delete_atributo_usuario(atributo_usuario_id: int):  
    rpta = nuevo_atributo_usuario.delete_atributo_usuario(atributo_usuario_id)  
    return rpta
