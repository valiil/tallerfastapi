import pandas as pd
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from controllers.carga_masiva_controller import CargaMasivaController  

router = APIRouter()
nueva_carga_masiva = CargaMasivaController()  

@router.post("/cargar_usuarios_masivo")
async def cargar_usuarios_masivo(file: UploadFile = File(...)):
    if file.content_type != 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
        raise HTTPException(status_code=400, detail="Archivo debe ser de tipo Excel (.xlsx)")
    
    try:
        # Cargar el archivo Excel usando Pandas
        df = pd.read_excel(file.file)

        # Validar si las columnas requeridas existen
        columnas_requeridas = ['usuario', 'contrasena', 'nombre', 'apellidos', 'documento', 'telefono', 'id_perfil']
        if not all(col in df.columns for col in columnas_requeridas):
            raise HTTPException(status_code=400, detail="El Excel no tiene las columnas requeridas")

        # Usar el controlador para cargar los usuarios
        resultado = nueva_carga_masiva.cargar_usuarios(file)
        return JSONResponse(content=resultado)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar usuarios: {e}")
