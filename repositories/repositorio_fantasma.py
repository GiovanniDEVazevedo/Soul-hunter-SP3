from database.connection import get_connection
import json

def salvar_fantasma(dados):
    sql = """
        INSERT INTO fantasma (
            seed, raridade, corpo, olho, boca, acessorios, aura, efeito
        )
        VALUES (%s, %s, %s, %s, %s, %s::jsonb, %s, %s)
        RETURNING id_fantasma;
    """
    partes = dados["partes"]

    parametros = (
        dados["seed"],
        dados["raridade"],
        partes.get("corpo"),
        partes.get("olho"),
        partes.get("boca"),
        json.dumps(partes.get("acessorios")),
        partes.get("aura"),
        partes.get("efeito"),
    )
    with get_connection() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, parametros)
            id_fantasma = cursor.fetchone()[0]
    return id_fantasma
def vincular_fantasma_a_lote(id_fantasma, id_lote):
    sql = """
        UPDATE fantasma
        SET id_lote = %s
        WHERE id_fantasma = %s;
    """

    with get_connection() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id_lote, id_fantasma))


def buscar_fantasma_por_id(id_fantasma):
    sql = """
        SELECT id_fantasma, seed, raridade, corpo, olho, boca, acessorios, aura, efeito
        FROM fantasma
        WHERE id_fantasma = %s; 
"""
    with get_connection() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id_fantasma,))
            linha = cursor.fetchone()
    if linha is None:
        return None
    return {
        "id_fantasma": linha[0],
        "seed": linha[1],
        "raridade": linha[2],
        "corpo": linha[3],
        "olho": linha[4],
        "boca": linha[5],
        "acessorios": linha[6],
        "aura": linha[7],
        "efeito": linha[8],
    }