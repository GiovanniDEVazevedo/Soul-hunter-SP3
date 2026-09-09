import hashlib
import os

from database.connection import get_connection

def criar_usuario(nome, email, senha):
    sal = os.urandom(16)
    hash_senha = hashlib.pbkdf2_hmac("sha256", senha.encode("utf-8"), sal, 100_000)

    sql = """
            INSERT INTO usuario (nome, email, senha_hash)
            VALUES (%s, %s, %s)
            RETURNING id_usuario, nome, email, pontos, nivel;
    """
    with get_connection() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (nome, email, sal.hex() + ":" + hash_senha.hex()))
            id_usuario, nome_lido, email_lido, pontos, nivel = cursor.fetchone()
    return {
        "id_usuario": id_usuario,
        "nome": nome_lido,
        "email": email_lido,
        "pontos": pontos,
        "nivel": nivel,
    }

def atualizar_pontos_e_nivel(id_usuario, pontos, nivel):
    sql = """
        UPDATE usuario
        SET pontos = %s, nivel = %s
        WHERE id_usuario = %s;
    """

    with get_connection() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (pontos, nivel, id_usuario))


def buscar_usuario_por_id(id_usuario):
    sql = """
        SELECT id_usuario, nome, email, pontos, nivel
        FROM usuario
        WHERE id_usuario = %s;
    """
    with get_connection() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id_usuario,))
            linha = cursor.fetchone()
    if linha is None:
        return None

    return {
        "id_usuario": linha[0],
        "nome": linha[1],
        "email": linha[2],
        "pontos": linha[3],
        "nivel": linha[4],
    }