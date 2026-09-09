from database.connection import get_connection


def buscar_local_e_fantasma(id_fantasma):
    sql = """
        SELECT f.id_lote, f.raridade,
               ps.id_spawn, ps.latitude, ps.longitude, ps.raio_captura
        FROM fantasma f
        JOIN ponto_spawn ps ON ps.id_lote = f.id_lote
        WHERE f.id_fantasma = %s;
    """

    with get_connection() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id_fantasma,))
            linha = cursor.fetchone()

    if linha is None:
        return None
    return {
        "id_lote": linha[0],
        "raridade": linha[1],
        "id_spawn": linha[2],
        "latitude": float(linha[3]),
        "longitude": float(linha[4]),
        "raio_captura": float(linha[5]),
    }


def inserir_captura(id_usuario, id_fantasma, id_spawn, latitude, longitude, distancia):
    sql ="""
        INSERT INTO captura (
            id_usuario, id_fantasma, id_spawn, latitude_usuario, longitude_usuario, distancia_metros
        )
        VALUES (%s, %s,%s, %s, %s, %s)
        RETURNING id_captura;
    """

    with get_connection() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id_usuario, id_fantasma, id_spawn, latitude, longitude, distancia))
            id_captura = cursor.fetchone()[0]

    return id_captura

def adicionar_a_colecao(id_usuario, id_fantasma):
    sql = """
        INSERT INTO colecao (id_usuario, id_fantasma, quantidade)
        VALUES (%s, %s, 1)
        ON CONFLICT (id_usuario, id_fantasma)
        DO UPDATE SET quantidade = colecao.quantidade + 1,
                      data_ultima_captura = CURRENT_TIMESTAMP;
    """
    with get_connection() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id_usuario, id_fantasma))