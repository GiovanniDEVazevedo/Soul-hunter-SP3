import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

from app import app

cliente = app.test_client()


def test_post_cria_fantasma_201():
    resposta = cliente.post("/fantasma", json={"seed": 4242})
    dados = resposta.get_json()

    assert resposta.status_code == 201
    assert dados["seed"] == 4242
    assert isinstance(dados["id_fantasma"], int)
    assert dados["raridade"] in {"COMUM", "RARO", "EPICO", "LENDARIO"}


def test_post_sem_corpo_sorteia_seed():
    resposta = cliente.post("/fantasma")
    dados = resposta.get_json()

    assert resposta.status_code == 201
    assert isinstance(dados["seed"], int)


def test_get_fantasma_existente_200():
    post = cliente.post("/fantasma", json={"seed": 9999})
    id_fantasma = post.get_json()["id_fantasma"]

    resposta = cliente.get(f"/fantasma/{id_fantasma}")

    assert resposta.status_code == 200
    assert resposta.get_json()["id_fantasma"] == id_fantasma


def test_get_fantasma_inexistente_404():
    resposta = cliente.get("/fantasma/999999999")

    assert resposta.status_code == 404
    assert resposta.get_json()["message"] == "fantasma nao encontrado"


def test_get_fantasma_id_nao_numerico_404():
    resposta = cliente.get("/fantasma/abc")

    assert resposta.status_code == 404