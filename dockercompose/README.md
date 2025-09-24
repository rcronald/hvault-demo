# 🚀 Vault Docker Setup

Este repositorio proporciona una configuración básica para HashiCorp Vault utilizando Docker Compose. Incluye un archivo `docker-compose.yml` para levantar el servicio de Vault y un script de inicialización (`vault-init.sh`) para configurar Vault después de que se haya iniciado.

## 🛠 Requisitos

- Docker
- Docker Compose
- [Vault CLI](https://www.vaultproject.io/downloads) (para interactuar con Vault desde tu máquina local)

## 📂 Estructura del Proyecto
- `docker-compose.yml`: Archivo de configuración de Docker Compose.
- `vault-init.sh`: Script de inicialización para Vault.
- `config/congif.json` : json con la configuración básica de Vault

## ⚙️ Configuración y Ejecución
1. **Clona el repositorio:**

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```
2. **Asegúrate de que el script de inicialización tenga permisos de ejecución:**
   
   ```bash
    chmod +x vault-init.sh
   ```

3. **Inicia los servicios con Docker Compose:**

   ```bash
    docker compose up -d
   ```
   Esto levantará el contenedor de Vault y ejecutará el script de inicialización.

4. **Verifica que los contenedores están en funcionamiento:**
   ```bash
    docker compose ps
   ```



## 🗂 Comandos Básicos de Vault

Aquí hay algunos comandos básicos para interactuar con Vault:

1. **Verificar el estado de Vault:**

   ```bash
   vault status
   ```
2. **Listar todos los secretos en un path:**

   ```bash
   vault kv list rds
   ```

3. **Leer un secreto específico:**

   ```bash
   vault kv get rds/mysql/user
   ```

4. **Escribir un secreto:**

   ```bash
   vault kv put rds/mysql/user username="mypassword123"
   ```

5. **Eliminar un secreto:**
   ```bash
   vault kv delete rds/mysql/user
   ```

6. **Ver los logs del contenedor:**
   ```bash
   docker-compose logs vault
   ```

7. **Entrar al contenedor de Vault:**
   ```bash
    docker exec -it vault sh
   ```

## 🔄 Destruir los Contenedores

   ```bash
    docker compose down
   ```

## 📚 Notas Adicionales

- Asegúrate de que el archivo `vault-init.sh` esté configurado correctamente para inicializar y configurar Vault según tus necesidades.
- Modifica el archivo `docker-compose.yml` según sea necesario para ajustar la configuración del contenedor de Vault.

Para más detalles sobre cómo usar Vault, consulta la [documentación oficial de HashiCorp Vault](https://www.vaultproject.io/docs).
