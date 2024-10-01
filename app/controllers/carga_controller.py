import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.carga_model import Carga  # Asegúrate de que este modelo exista
from fastapi.encoders import jsonable_encoder

class CargaController:
        
    def create_carga(self, carga: Carga):   
        try:
            # Establecer la conexión con la base de datos
            conn = get_db_connection()
            cursor = conn.cursor()
            
            # Insertar la nueva carga en la base de datos
            cursor.execute(""" 
                INSERT INTO carga (peso, largo, ancho, alto, descripcion, fecha_recogida, fecha_entrega, estado_actual, origen, destino, ubicacion, tipo, id_perfil) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                carga.peso,
                carga.largo,
                carga.ancho,
                carga.alto,
                carga.descripcion,
                carga.fecha_recogida,
                carga.fecha_entrega,
                carga.estado_actual,
                carga.origen,
                carga.destino,
                carga.ubicacion,
                carga.tipo,
                carga.id_perfil
            ))

            # Confirmar la transacción
            conn.commit()
            
            # Devolver un mensaje de éxito
            return {"resultado": "Carga creada exitosamente"}

        except mysql.connector.Error as err:
            # Imprimir el error en la consola para depurar
            print(f"Error en la base de datos: {err}")
            
            # Si la conexión está activa, hacer rollback de la transacción
            if conn.is_connected():
                conn.rollback()
            
            # Lanzar una excepción HTTP con detalles del error
            raise HTTPException(status_code=500, detail=f"Error al crear la carga en la base de datos: {err}")

        except Exception as e:
            # Captura cualquier otra excepción no manejada y lanza un error 500 con el mensaje del error
            print(f"Error desconocido: {e}")
            raise HTTPException(status_code=500, detail=f"Error interno del servidor: {e}")

        finally:
            # Asegurarse de cerrar la conexión si está activa
            if conn.is_connected():
                cursor.close()
                conn.close()

        
    def get_carga(self, carga_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM carga WHERE id = %s", (carga_id,))
            result = cursor.fetchone()
            payload = [] 
            content = {} 
            
            if result:
                content = {
                    'id': int(result[0]),
                    'peso': float(result[1]),
                    'largo': float(result[2]),
                    'ancho': float(result[3]),
                    'alto': float(result[4]),
                    'descripcion': result[5],
                    'fecha_recogida': result[6],
                    'fecha_entrega': result[7],
                    'estado_actual': result[8],
                    'origen': result[9],
                    'destino': result[10],
                    'ubicacion': result[11],
                    'tipo': result[12],
                    'id_perfil': int(result[13])
                }
                payload.append(content)

                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Carga no encontrada")  
                
        except mysql.connector.Error as err:
            if conn.is_connected():
                conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error en la base de datos: {err}")

        finally:
            if conn.is_connected():
                conn.close()

    def get_cargas(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM carga")
            result = cursor.fetchall()
            
            if not result:
                raise HTTPException(status_code=404, detail="Cargas no encontradas")
            
            payload = []
            for data in result:
                content = {
                    'id': data[0],
                    'peso': float(data[1]),
                    'largo': float(data[2]),
                    'ancho': float(data[3]),
                    'alto': float(data[4]),
                    'descripcion': data[5],
                    'fecha_recogida': data[6],
                    'fecha_entrega': data[7],
                    'estado_actual': data[8],
                    'origen': data[9],
                    'destino': data[10],
                    'ubicacion': data[11],
                    'tipo': data[12],
                    'id_perfil': int(data[13])
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

    def update_carga(self, carga_id: int, carga: Carga):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(""" 
                UPDATE carga 
                SET peso = %s, largo = %s, ancho = %s, alto = %s, descripcion = %s, fecha_recogida = %s, fecha_entrega = %s, estado_actual = %s, origen = %s, destino = %s, ubicacion = %s, tipo = %s, id_perfil = %s
                WHERE id = %s
            """, (
                carga.peso,
                carga.largo,
                carga.ancho,
                carga.alto,
                carga.descripcion,
                carga.fecha_recogida,
                carga.fecha_entrega,
                carga.estado_actual,
                carga.origen,
                carga.destino,
                carga.ubicacion,
                carga.tipo,
                carga.id_perfil,
                carga_id
            ))

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Carga no encontrada")

            return {"resultado": "Carga actualizada exitosamente"}

        except mysql.connector.Error as err:
            print(f"Error en la base de datos: {err}")
            if conn.is_connected():
                conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error al actualizar la carga en la base de datos: {err}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def delete_carga(self, carga_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM carga WHERE id = %s", (carga_id,))

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Carga no encontrada")

            return {"resultado": "Carga eliminada exitosamente"}

        except mysql.connector.Error as err:
            print(f"Error en la base de datos: {err}")
            if conn.is_connected():
                conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error al eliminar la carga en la base de datos: {err}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# carga_controller = CargaController()  # Actualiza esta línea si es necesario
