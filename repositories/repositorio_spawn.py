from database.connection import get_connection


def buscar_casa_principal():
    sql = """
        SELECT id_spawn, id_lote, latitude, longitude, raio_captura
        FROM ponto_spawn
        WHERE ativo = TRUE
        ORDER BY id_spawn
        LIMIT 1;
    """

    with get_connection() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql)
            linha = cursor.fetchone()

    if linha is None:
        return None

    return {
        "id_spawn": linha[0],
        "id_lote": linha[1],
        "latitude": float(linha[2]),
        "longitude": float(linha[3]),
        "raio_captura": float(linha[4]),
    }

def criar_spawn(latitude, longitude, id_lote, raio_captura=100.0):
    sql = """
        INSERT INTO ponto_spawn (latitude, longitude, id_lote, raio_captura)
        VALUES (%s, %s, %s, %s)
        RETURNING id_spawn, latitude, longitude;

    """
    with get_connection() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (latitude, longitude, id_lote, raio_captura))
            id_spawn, lat_lida, long_lida = cursor.fetchone()

    return {
        "id_spawn": id_spawn,
        "latitude": lat_lida,
        "longitude": long_lida,
    }
def listar_spawns_com_fantasma():
    sql = """
        SELECT ps.id_spawn, ps.latitude, ps.longitude,
               f.seed, f.raridade, f.corpo, f.olho, f.boca, f.acessorios, f.aura, f.efeito
        FROM ponto_spawn ps
        JOIN fantasma f ON f.id_lote = ps.id_lote
        WHERE ps.ativo = TRUE
    """

    with get_connection() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql)
            linhas = cursor.fetchall()


    return [
        {
            "id_spawn": linha[0],
            "latitude": float(linha[1]),
            "longitude": float(linha[2]),
            "fantasma": {
                "seed": linha[3],
                "raridade": linha[4],
                "corpo": linha[5],
                "olho": linha[6],
                "boca": linha[7],
                "acessorios": linha[8],
                "aura": linha[9],
                "efeito": linha[10],
            },
        }
        for linha in linhas
    ]