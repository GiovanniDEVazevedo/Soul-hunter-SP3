import sys
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

from app import app

cliente = app.test_client()
SUFIXO = str(int(time.time()))


def test_cadastrar_usuario_201():
    resposta = cliente.post(
        "/usuario",
        json={"nome": "Luna", "email": f"luna{SUFIXO}@teste.com", "senha": "segredo123"},
    )
    dados = resposta.get_json()

    assert resposta.status_code == 201
    assert isinstance(dados["id_usuario"], int)
    assert dados["nome"] == "Luna"
    assert "senha_hash" not in dados
    assert dados["pontos"] == 0
    assert dados["nivel"] == 1


def test_buscar_usuario_existente_200():
    post = cliente.post(
        "/usuario",
        json={"nome": "Rin", "email": f"rin{SUFIXO}@teste.com", "senha": "segredo456"},
    )
    id_usuario = post.get_json()["id_usuario"]

    resposta = cliente.get(f"/usuario/{id_usuario}")

    assert resposta.status_code == 200
    assert resposta.get_json()["email"] == f"rin{SUFIXO}@teste.com"


def test_buscar_usuario_inexistente_404():
    resposta = cliente.get("/usuario/999999999")

    assert resposta.status_code == 404
    assert resposta.get_json()["message"] == "usuario nao encontrado"