import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.usuario_model import Usuario
from fastapi.encoders import jsonable_encoder

class UsuarioController:
        
    def create_usuario(self, usuario: Usuario):   
        try:
            # Establecer la conexión con la base de datos
            conn = get_db_connection()
            cursor = conn.cursor()
            
            # Insertar el nuevo usuario en la base de datos
            cursor.execute("""
                INSERT INTO usuario (usuario, contrasena, nombre, apellidos, documento, telefono, id_perfil) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                usuario.usuario,
                usuario.contrasena,
                usuario.nombre,
                usuario.apellido,
                usuario.documento,
                usuario.telefono,
                usuario.id_perfil
            ))

            # Confirmar la transacción
            conn.commit()
            
            # Devolver un mensaje de éxito
            return {"resultado": "Usuario creado exitosamente"}

        except mysql.connector.Error as err:
            # Imprimir el error en la consola para depurar
            print(f"Error en la base de datos: {err}")
            
            # Si la conexión está activa, hacer rollback de la transacción
            if conn.is_connected():
                conn.rollback()
            
            # Lanzar una excepción HTTP con detalles del error
            raise HTTPException(status_code=500, detail=f"Error al crear el usuario en la base de datos: {err}")

        except Exception as e:
            # Captura cualquier otra excepción no manejada y lanza un error 500 con el mensaje del error
            print(f"Error desconocido: {e}")
            raise HTTPException(status_code=500, detail=f"Error interno del servidor: {e}")

        finally:
            # Asegurarse de cerrar la conexión si está activa
            if conn.is_connected():
                cursor.close()
                conn.close()

        

    def get_usuario(self, usuario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE id = %s", (usuario_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'usuario':result[1],
                    'contrasena':result[2],
                    'nombre':result[3],
                    'apellido':result[4],
                    'documento':result[5],
                    'telefono':result[6],
                    'id_perfil':int(result[7])    
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
             return  json_data
            else:
                raise HTTPException(status_code=404, detail="User not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def get_usuarios(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario")
            result = cursor.fetchall()
            
            if not result:
                raise HTTPException(status_code=404, detail="User not found")
            
            payload = []
            for data in result:
                content = {
                    'id': data[0],
                    'usuario': data[1],
                    'contrasena': data[2],
                    'nombre': data[3],
                    'apellido': data[4],
                    'documento': data[5],
                    'telefono': data[6],
                    'id_perfil': data[7]
                }
                payload.append(content)
            
            json_data = jsonable_encoder(payload)
            return {"resultado": json_data}
        
        except mysql.connector.Error as err:
            print(f"Error en la base de datos: {err}")
            conn.rollback()
            raise HTTPException(status_code=500, detail=f"Database error: {err}")  # Devuelve el error al cliente
        
        finally:
            if conn.is_connected():
                conn.close()


    def update_usuario(self, usuario_id: int, usuario: Usuario):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE usuario 
                SET usuario = %s, contrasena = %s, nombre = %s, apellidos = %s, documento = %s, telefono = %s, id_perfil = %s
                WHERE id = %s
            """, (
                usuario.usuario,
                usuario.contrasena,
                usuario.nombre,
                usuario.apellido,
                usuario.documento,
                usuario.telefono,
                usuario.id_perfil,
                usuario_id
            ))

            conn.commit()

            
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="User not found")


            return {"resultado": "Usuario actualizado exitosamente"}

        except mysql.connector.Error as err:
            print(f"Error en la base de datos: {err}")
            if conn.is_connected():
                conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error al actualizar el usuario en la base de datos: {err}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def delete_usuario(self, usuario_id: int):
        try:
            
            conn = get_db_connection()
            cursor = conn.cursor()

            
            cursor.execute("DELETE FROM usuario WHERE id = %s", (usuario_id,))

            
            conn.commit()

            
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="User not found")

            
            return {"resultado": "Usuario eliminado exitosamente"}

        except mysql.connector.Error as err:
            print(f"Error en la base de datos: {err}")
            if conn.is_connected():
                conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error al eliminar el usuario en la base de datos: {err}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()


    
    
       

##user_controller = UserController()
