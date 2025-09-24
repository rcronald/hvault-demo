# Usar una imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios
COPY app.py requirements.txt index.html ./

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto de la app
EXPOSE 5000

# Definir variables de entorno (puedes ajustar los valores al construir la imagen)
ENV VAULT_URL='http:/ip-host:8200'
ENV VAULT_TOKEN='change-token'

# Comando para ejecutar la app
CMD ["python", "app.py"]