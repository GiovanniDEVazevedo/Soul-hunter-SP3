"""
Seed de demonstracao do Soul Hunter.

Cria um lote, vincula fantasmas a ele e espalha pontos de spawn
da casa assombrada. Idempotente por design: antes de criar,
apaga os dados de demonstracao antigos.

Uso:
    python seed.py
"""

from database.connection import get_connection
from services.servico_fantasma import gerar_e_salvar_fantasma
from services.servico_spawn import criar_ponto_spawn

SEEDS_FANTASMAS = (111, 222, 333)

SPAWNS = [
    (-23.5595600, -46.7311900),   # USP Butanta
    (-23.5610000, -46.7290000),
    (-23.5581000, -46.7332000),
    (-23.5630000, -46.7285000),
]


def limpar_dados_demonstracao():
    with get_connection() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("TRUNCATE captura, colecao, fantasma, ponto_spawn, lote_geracao RESTART IDENTITY CASCADE")


def criar_lote(nome):
    with get_connection() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO lote_geracao (nome, quantidade_maxima)
                VALUES (%s, %s)
                RETURNING id_lote;
                """,
                (nome, len(SEEDS_FANTASMAS)),
            )
            return cursor.fetchone()[0]


def vincular_fantasma_a_lote(id_fantasma, id_lote):
    with get_connection() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                "UPDATE fantasma SET id_lote = %s WHERE id_fantasma = %s",
                (id_lote, id_fantasma),
            )


def popular_seed():
    print("Limpando dados antigos...")
    limpar_dados_demonstracao()

    id_lote = criar_lote("Lote Demonstracao Leaflet")
    print(f"Lote criado: id {id_lote}")

    for seed in SEEDS_FANTASMAS:
        fantasma = gerar_e_salvar_fantasma(seed=seed)
        vincular_fantasma_a_lote(fantasma["id_fantasma"], id_lote)
        print(f"Fantasma seed {seed} ({fantasma['raridade']}) vinculado ao lote.")

    for latitude, longitude in SPAWNS:
        criado = criar_ponto_spawn(latitude, longitude, id_lote)
        print(f"Spawn criado: id {criado['id_spawn']} ({latitude}, {longitude})")

    print("Seed concluido.")


if __name__ == "__main__":
    popular_seed()