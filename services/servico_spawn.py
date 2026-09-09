from repositories.repositorio_spawn import criar_spawn, listar_spawns_com_fantasma

def criar_ponto_spawn(latitude, longitude, id_lote):
    return criar_spawn(latitude, longitude, id_lote)

def listar_spawns():
    return listar_spawns_com_fantasma()