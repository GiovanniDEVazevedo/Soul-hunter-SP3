from repositories.repositorio_usuario import buscar_usuario_por_id, criar_usuario

def criar_usuario_service(nome, email, senha):
    return criar_usuario(nome, email, senha)
def buscar_usuario(id_usuario):
    return buscar_usuario_por_id(id_usuario)
