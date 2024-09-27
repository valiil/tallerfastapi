from fastapi import APIRouter, HTTPException
from controllers.usuario_controller import *
from models.usuario_model import Usuario

router = APIRouter()

nuevo_usuario = UsuarioController()


@router.post("/create_usuario")
async def create_usuario(usuario: Usuario):
    rpta = nuevo_usuario.create_usuario(Usuario)
    return rpta


@router.get("/get_ususario/{usuario_id}",response_model=Usuario)
async def get_usuario(usuario_id: int):
    rpta = nuevo_usuario.get_usuario(usuario_id)
    return rpta

@router.get("/get_usuarios/")
async def get_usuarios():
    rpta = nuevo_usuario.get_usuarios()
    return rpta