from services.gerador_fantasma import gerar_fantasma
from repositories.repositorio_fantasma import (
    buscar_fantasma_por_id,
    salvar_fantasma,
    vincular_fantasma_a_lote,
)
from repositories.repositorio_spawn import buscar_casa_principal


def gerar_e_salvar_fantasma(seed=None):
    fantasma = gerar_fantasma(seed)
    id_fantasma = salvar_fantasma(fantasma)
    fantasma["id_fantasma"] = id_fantasma
    return fantasma


def investigar_casa():
    casa = buscar_casa_principal()
    fantasma = gerar_e_salvar_fantasma()

    if casa is not None:
        vincular_fantasma_a_lote(fantasma["id_fantasma"], casa["id_lote"])
        fantasma["id_lote"] = casa["id_lote"]

    return fantasma


def buscar_fantasma(id_fantasma):
    return buscar_fantasma_por_id(id_fantasma) 