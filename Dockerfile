# Usamos una imagen oficial de Python como base
FROM python:3.10-slim

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos los archivos requeridos a la imagen
COPY requirements.txt .

# Instalamos las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código de la aplicación
COPY . .

# Exponemos el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["python", "app.py"]
