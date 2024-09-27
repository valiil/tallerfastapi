import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.usuario_model import Usuario
from fastapi.encoders import jsonable_encoder

class UsuarioController:
        
    def create_usuario(self, usuario: Usuario):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (usuario,contrasena,nombre,apellido,documento,telefono,id_perfil) VALUES (%s, %s, %s, %s, %s ,%s,%s)", (usuario.usuario, usuario.contrasena, usuario.nombre, usuario.apellido, usuario.documento, usuario.telefono, usuario.id_perfil))
            conn.commit()
            conn.close()
            return {"resultado": "Usuario creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_usuario(self, usuario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE id = %s", (usuario_id,))
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
            cursor.execute("SELECT * FROM usuarios")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'usuario':data[1],
                    'contrasena':data[2],
                    'nombre':data[3],
                    'apellido':data[4],
                    'documento':data[5],
                    'telefono':data[6],
                    'id_perfil':data[7]    
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="User not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    
       

##user_controller = UserController()