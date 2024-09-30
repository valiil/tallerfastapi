from fastapi import APIRouter, HTTPException
from controllers.atributo_usuario_controller import AtributoUsuarioController  # Cambiado a AtributoUsuarioController
from models.atributo_usuario_model import AtributoUsuario  # Cambiado a AtributoUsuario

router = APIRouter()

nuevo_atributo_usuario = AtributoUsuarioController()  # Cambiado a AtributoUsuarioController

@router.post("/create_atributo_usuario")  # Cambiado a create_atributo_usuario
async def create_atributo_usuario(atributo_usuario: AtributoUsuario):  # Cambiado a AtributoUsuario
    rpta = nuevo_atributo_usuario.create_atributo_usuario(atributo_usuario)  # Cambiado a create_atributo_usuario
    return rpta

@router.get("/get_atributo_usuario/{atributo_usuario_id}", response_model=AtributoUsuario)  # Cambiado a get_atributo_usuario
async def get_atributo_usuario(atributo_usuario_id: int):  # Cambiado a get_atributo_usuario
    rpta = nuevo_atributo_usuario.get_atributo_usuario(atributo_usuario_id)  # Cambiado a get_atributo_usuario
    return rpta

@router.get("/get_atributo_usuarios/")  # Cambiado a get_atributo_usuarios
async def get_atributo_usuarios():  # Cambiado a get_atributo_usuarios
    rpta = nuevo_atributo_usuario.get_atributo_usuarios()  # Cambiado a get_atributo_usuarios
    return rpta

@router.put("/update_atributo_usuario/{atributo_usuario_id}")  # Cambiado a update_atributo_usuario
async def update_atributo_usuario(atributo_usuario_id: int, atributo_usuario: AtributoUsuario):  # Cambiado a AtributoUsuario
    rpta = nuevo_atributo_usuario.update_atributo_usuario(atributo_usuario_id, atributo_usuario)  # Cambiado a update_atributo_usuario
    return rpta

@router.delete("/delete_atributo_usuario/{atributo_usuario_id}")  # Cambiado a delete_atributo_usuario
async def delete_atributo_usuario(atributo_usuario_id: int):  # Cambiado a delete_atributo_usuario
    rpta = nuevo_atributo_usuario.delete_atributo_usuario(atributo_usuario_id)  # Cambiado a delete_atributo_usuario
    return rpta
