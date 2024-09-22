from dotenv import load_dotenv
import logging
import pymysql

import sys
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configurar el logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Función para obtener la configuración de la base de datos
def get_db_config():
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_port = int(os.getenv('DB_PORT', 3309))  # Convertir a entero y usar puerto 3306 por defecto si no está definido
    db_name = os.getenv('DB_NAME')
    db_password = os.getenv('DB_PASSWORD')

    return {
        'host': db_host,
        'user': db_user,
        'port': db_port,
        'database': db_name,
        'password': db_password
    }

# Función para conectarse a la base de datos
def connect_to_db():
    config = get_db_config()
    try:
        connection = pymysql.connect(
            host=config['host'],
            user=config['user'],
            password=config['password'],
            database=config['database'],
            port=config['port'],
            connect_timeout=5
        )
        logger.info("SUCCESS: Connection to MySQL instance succeeded")
        return connection
    except pymysql.MySQLError as e:
        logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
        logger.error(e)
        sys.exit(1)
