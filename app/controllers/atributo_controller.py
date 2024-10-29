import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.atributo_model import Atributo  
from fastapi.encoders import jsonable_encoder

class AtributoController:
        
    def create_atributo(self, atributo: Atributo):   
        try:
            # Establecer la conexión con la base de datos
            conn = get_db_connection()
            cursor = conn.cursor()
            
            # Insertar el nuevo atributo en la base de datos
            cursor.execute(""" 
                INSERT INTO atributo (nombre, descripcion) 
                VALUES (%s, %s)
            """, (
                atributo.nombre,
                atributo.descripcion
            ))

            # Confirmar la transacción
            conn.commit()
            
            # Devolver un mensaje de éxito
            return {"resultado": "Atributo creado exitosamente"}

        except mysql.connector.Error as err:
            # Imprimir el error en la consola para depurar
            print(f"Error en la base de datos: {err}")
            
            # Si la conexión está activa, hacer rollback de la transacción
            if conn.is_connected():
                conn.rollback()
            
            # Lanzar una excepción HTTP con detalles del error
            raise HTTPException(status_code=500, detail=f"Error al crear el atributo en la base de datos: {err}")

        except Exception as e:
            # Captura cualquier otra excepción no manejada y lanza un error 500 con el mensaje del error
            print(f"Error desconocido: {e}")
            raise HTTPException(status_code=500, detail=f"Error interno del servidor: {e}")

        finally:
            # Asegurarse de cerrar la conexión si está activa
            if conn.is_connected():
                cursor.close()
                conn.close()

    def get_atributo(self, atributo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributo WHERE id = %s", (atributo_id,))
            result = cursor.fetchone()
            payload = [] 
            content = {} 
            
            if result:
                content = {
                    'id': int(result[0]),
                    'nombre': result[1],
                    'descripcion': result[2]
                }
                payload.append(content)

                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Atributo no encontrado")  
                
        except mysql.connector.Error as err:
            if conn.is_connected():
                conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error en la base de datos: {err}")

        finally:
            if conn.is_connected():
                conn.close()

    def get_atributos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributo")
            result = cursor.fetchall()
            
            if not result:
                raise HTTPException(status_code=404, detail="Atributos no encontrados")
            
            payload = []
            for data in result:
                content = {
                    'id': data[0],
                    'nombre': data[1],
                    'descripcion': data[2]
                }
                payload.append(content)
            
            json_data = jsonable_encoder(payload)
            return {"resultado": json_data}
        
        except mysql.connector.Error as err:
            print(f"Error en la base de datos: {err}")
            if conn.is_connected():
                conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error de base de datos: {err}")  # Devuelve el error al cliente
        
        finally:
            if conn.is_connected():
                conn.close()

    def update_atributo(self, atributo_id: int, atributo: Atributo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(""" 
                UPDATE atributo 
                SET nombre = %s, descripcion = %s
                WHERE id = %s
            """, (
                atributo.nombre,
                atributo.descripcion,
                atributo_id
            ))

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Atributo no encontrado")

            return {"resultado": "Atributo actualizado exitosamente"}

        except mysql.connector.Error as err:
            print(f"Error en la base de datos: {err}")
            if conn.is_connected():
                conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error al actualizar el atributo en la base de datos: {err}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def delete_atributo(self, atributo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM atributo WHERE id = %s", (atributo_id,))

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Atributo no encontrado")

            return {"resultado": "Atributo eliminado exitosamente"}

        except mysql.connector.Error as err:
            print(f"Error en la base de datos: {err}")
            if conn.is_connected():
                conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error al eliminar el atributo en la base de datos: {err}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# atributo_controller = AtributoController()  
