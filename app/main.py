from fastapi import FastAPI
from routes.usuario_routes import router as usuario_router
from routes.transporte_routes import router as transporte_router  # Mantenemos el modelo Transporte
from routes.perfil_routes import router as perfil_router  # Agregamos el nuevo router para Perfil
from routes.atributo_routes import router as atributo_router  # Agregamos el router para Atributo
from routes.atributo_usuario_routes import router as atributo_usuario_router  # Agregamos el router para Atributo Usuario
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    #"http://localhost.tiangolo.com",
    #"https://localhost.tiangolo.com",
    "http://localhost"
    #"http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuario_router)
app.include_router(transporte_router)  # Mantener el transporte
app.include_router(perfil_router)  # Incluir el perfil
app.include_router(atributo_router)  # Incluir el nuevo router para Atributo
app.include_router(atributo_usuario_router)  # Incluir el nuevo router para Atributo Usuario

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
