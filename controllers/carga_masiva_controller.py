import pandas as pd
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from config.db_config import get_db_connection


class CargaMasivaController:
    
    def cargar_usuarios(self, file: UploadFile):
        try:
            # Leer el archivo Excel con pandas
            df = pd.read_excel(file.file)

            # Validar que el Excel tiene las columnas correctas
            required_columns = ["usuario", "contrasena", "nombre", "apellidos", "documento", "telefono", "id_perfil"]
            if not all(col in df.columns for col in required_columns):
                raise HTTPException(status_code=400, detail="Formato del archivo incorrecto")

            # Establecer la conexión a la base de datos
            conn = get_db_connection()
            cursor = conn.cursor()

            # Insertar los usuarios uno a uno
            for _, row in df.iterrows():
                cursor.execute("""
                    INSERT INTO usuario (usuario, contrasena, nombre, apellidos, documento, telefono, id_perfil) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (
                    row['usuario'],
                    row['contrasena'],
                    row['nombre'],
                    row['apellidos'],
                    row['documento'],
                    row['telefono'],
                    row['id_perfil']
                ))

            # Confirmar la transacción
            conn.commit()

            return {"resultado": "Usuarios cargados exitosamente"}

        except mysql.connector.Error as err:
            if conn.is_connected():
                conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error en la base de datos: {err}")

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error interno del servidor: {e}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
