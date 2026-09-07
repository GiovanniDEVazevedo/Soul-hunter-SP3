from services.gerador_fantasma import gerar_fantasma
from repositories.repositorio_fantasma import salvar_fantasma, buscar_fantasma_por_id

def gerar_e_salvar_fantasma(seed=None):
    fantasma = gerar_fantasma(seed)
    id_fantasma = salvar_fantasma(fantasma)
    fantasma["id_fantasma"] = id_fantasma
    return fantasma
def buscar_fantasma(id_fantasma):
    return buscar_fantasma_por_id(id_fantasma) 