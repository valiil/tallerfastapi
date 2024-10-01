import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.atributo_usuario_model import AtributoUsuario  # Asegúrate de que este modelo exista
from fastapi.encoders import jsonable_encoder

class AtributoUsuarioController:
        
    def create_atributo_usuario(self, atributo_usuario: AtributoUsuario):   
        try:
            # Establecer la conexión con la base de datos
            conn = get_db_connection()
            cursor = conn.cursor()
            
            # Insertar el nuevo atributo de usuario en la base de datos
            cursor.execute(""" 
                INSERT INTO atributo_usuario (id_usuario, id_atributo, valor, descripcion) 
                VALUES (%s, %s, %s, %s)
            """, (
                atributo_usuario.id_usuario,
                atributo_usuario.id_atributo,
                atributo_usuario.valor,
                atributo_usuario.descripcion
            ))

            # Confirmar la transacción
            conn.commit()
            
            # Devolver un mensaje de éxito
            return {"resultado": "Atributo de usuario creado exitosamente"}

        except mysql.connector.Error as err:
            # Imprimir el error en la consola para depurar
            print(f"Error en la base de datos: {err}")
            
            # Si la conexión está activa, hacer rollback de la transacción
            if conn.is_connected():
                conn.rollback()
            
            # Lanzar una excepción HTTP con detalles del error
            raise HTTPException(status_code=500, detail=f"Error al crear el atributo de usuario en la base de datos: {err}")

        except Exception as e:
            # Captura cualquier otra excepción no manejada y lanza un error 500 con el mensaje del error
            print(f"Error desconocido: {e}")
            raise HTTPException(status_code=500, detail=f"Error interno del servidor: {e}")

        finally:
            # Asegurarse de cerrar la conexión si está activa
            if conn.is_connected():
                cursor.close()
                conn.close()

    def get_atributo_usuario(self, atributo_usuario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributo_usuario WHERE id = %s", (atributo_usuario_id,))
            result = cursor.fetchone()
            payload = [] 
            content = {} 
            
            if result:
                content = {
                    'id': int(result[0]),
                    'id_usuario': int(result[1]),
                    'id_atributo': int(result[2]),
                    'valor': result[3],
                    'descripcion': result[4]
                }
                payload.append(content)

                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Atributo de usuario no encontrado")  
                
        except mysql.connector.Error as err:
            if conn.is_connected():
                conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error en la base de datos: {err}")

        finally:
            if conn.is_connected():
                conn.close()

    def get_atributo_usuarios(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributo_usuario")
            result = cursor.fetchall()
            
            if not result:
                raise HTTPException(status_code=404, detail="Atributos de usuario no encontrados")
            
            payload = []
            for data in result:
                content = {
                    'id': data[0],
                    'id_usuario': int(data[1]),
                    'id_atributo': int(data[2]),
                    'valor': data[3],
                    'descripcion': data[4]
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

    def update_atributo_usuario(self, atributo_usuario_id: int, atributo_usuario: AtributoUsuario):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(""" 
                UPDATE atributo_usuario 
                SET id_usuario = %s, id_atributo = %s, valor = %s, descripcion = %s
                WHERE id = %s
            """, (
                atributo_usuario.id_usuario,
                atributo_usuario.id_atributo,
                atributo_usuario.valor,
                atributo_usuario.descripcion,
                atributo_usuario_id
            ))

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Atributo de usuario no encontrado")

            return {"resultado": "Atributo de usuario actualizado exitosamente"}

        except mysql.connector.Error as err:
            print(f"Error en la base de datos: {err}")
            if conn.is_connected():
                conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error al actualizar el atributo de usuario en la base de datos: {err}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def delete_atributo_usuario(self, atributo_usuario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM atributo_usuario WHERE id = %s", (atributo_usuario_id,))

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Atributo de usuario no encontrado")

            return {"resultado": "Atributo de usuario eliminado exitosamente"}

        except mysql.connector.Error as err:
            print(f"Error en la base de datos: {err}")
            if conn.is_connected():
                conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error al eliminar el atributo de usuario en la base de datos: {err}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# atributo_usuario_controller = AtributoUsuarioController()  # Actualiza esta línea si es necesario
