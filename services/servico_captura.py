from repositories.repositorio_captura import adicionar_a_colecao, buscar_local_e_fantasma, inserir_captura
from repositories.repositorio_usuario import (
    atualizar_pontos_e_nivel,
    buscar_usuario_por_id,
)
from services.geo import distancia_haversine

PONTOS_POR_CAPITURA = {
    "COMUM": 10,
    "RARO": 25,
    "EPICO": 50,
    "LENDARIO": 100,

}
RAIO_CAPTURA_PADRAO = 100.0
MAXIMO_PONTOS_NIVEL = 100

def captura_fantasma(id_usuario, id_fantasma, latitude, longitude):
    dados = buscar_local_e_fantasma(id_fantasma)

    if dados is None:
        return{"erro": "fantasma nao encontrado"}, 404
    usuario = buscar_usuario_por_id(id_usuario)
    if usuario is None:
        return {"erro": "usuario nao encontrado"}, 404

    distancia = distancia_haversine(
        latitude, longitude, dados["latitude"], dados["longitude"]
    )
    if distancia > dados["raio_captura"]:
        return {
            "erro": "fora do alcance",
            "distancia_metros" : round(distancia, 2),
        },400

    id_captura = inserir_captura(
        id_usuario, id_fantasma, dados["id_spawn"], latitude, longitude, distancia
    )
    adicionar_a_colecao(id_usuario, id_fantasma)

    pontos = PONTOS_POR_CAPITURA[dados["raridade"]]
    novos_pontos = usuario["pontos"] + pontos
    novo_nivel = novos_pontos // MAXIMO_PONTOS_NIVEL + 1

    atualizar_pontos_e_nivel(id_usuario, novos_pontos, novo_nivel)

    return {
        "id_captura": id_captura,
        "fantasma": {
            "id_fantasma": id_fantasma,
            "raridade": dados["raridade"],
        },
        "distancia_metros": round(distancia, 2),
        "pontos_ganhos": pontos,
        "pontos_totais": novos_pontos,
        "nivel": novo_nivel,
    }, 201