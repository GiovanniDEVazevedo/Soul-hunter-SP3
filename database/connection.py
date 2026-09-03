import os
import psycopg
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()


def get_connection():
    """
    Cria e retorna uma conexão com o banco PostgreSQL.
    """

    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise ValueError("DATABASE_URL não encontrada no arquivo .env")

    return psycopg.connect(database_url)