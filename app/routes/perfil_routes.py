from fastapi import APIRouter, HTTPException
from app.controllers.perfil_controller import PerfilController
from app.models.perfil_model import Perfil

router = APIRouter()

nuevo_perfil = PerfilController()


@router.post("/create_perfil")
async def create_perfil(perfil: Perfil):
    rpta = nuevo_perfil.create_perfil(perfil)
    return rpta


@router.get("/get_perfil/{perfil_id}", response_model=Perfil)
async def get_perfil(perfil_id: int):
    rpta = nuevo_perfil.get_perfil(perfil_id)
    return rpta

@router.get("/get_perfiles/")
async def get_perfiles():
    rpta = nuevo_perfil.get_perfiles()
    return rpta

@router.put("/update_perfil/{perfil_id}")
async def update_perfil(perfil_id: int, perfil: Perfil):
    rpta = nuevo_perfil.update_perfil(perfil_id, perfil)
    return rpta

@router.delete("/delete_perfil/{perfil_id}")
async def delete_perfil(perfil_id: int):
    rpta = nuevo_perfil.delete_perfil(perfil_id)
    return rpta
