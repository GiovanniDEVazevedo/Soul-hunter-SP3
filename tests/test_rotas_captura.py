import sys
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

from app import app
from repositories.repositorio_captura import buscar_local_e_fantasma

cliente = app.test_client()
SUFIXO = str(int(time.time()))


def test_fluxo_completo_investigar_e_capturar():
    r = cliente.post(
        "/usuario",
        json={"nome": "Caca", "email": f"caca{SUFIXO}@teste.com", "senha": "segredo"},
    )
    id_usuario = r.get_json()["id_usuario"]

    r = cliente.post("/casa/investigar")
    assert r.status_code == 201
    fantasma = r.get_json()

    local = buscar_local_e_fantasma(fantasma["id_fantasma"])
    assert local is not None

    r = cliente.post(
        "/captura",
        json={
            "id_usuario": id_usuario,
            "id_fantasma": fantasma["id_fantasma"],
            "latitude": local["latitude"],
            "longitude": local["longitude"],
        },
    )
    dados = r.get_json()

    assert r.status_code == 201
    assert isinstance(dados["id_captura"], int)
    assert dados["fantasma"]["id_fantasma"] == fantasma["id_fantasma"]
    assert dados["pontos_ganhos"] > 0
    assert dados["pontos_totais"] == dados["pontos_ganhos"]
    assert dados["nivel"] == 1


def test_captura_fora_do_alcance_retorna_400():
    r = cliente.post(
        "/usuario",
        json={"nome": "Longe", "email": f"longe{SUFIXO}@teste.com", "senha": "segredo"},
    )
    id_usuario = r.get_json()["id_usuario"]

    r = cliente.post("/casa/investigar")
    fantasma = r.get_json()

    r = cliente.post(
        "/captura",
        json={
            "id_usuario": id_usuario,
            "id_fantasma": fantasma["id_fantasma"],
            "latitude": 35.67,
            "longitude": 139.65,
        },
    )

    assert r.status_code == 400
    assert r.get_json()["erro"] == "fora do alcance"


def test_captura_duplicada_soma_na_colecao():
    r = cliente.post(
        "/usuario",
        json={"nome": "Repete", "email": f"repete{SUFIXO}@teste.com", "senha": "segredo"},
    )
    id_usuario = r.get_json()["id_usuario"]

    r = cliente.post("/casa/investigar")
    fantasma = r.get_json()
    local = buscar_local_e_fantasma(fantasma["id_fantasma"])

    corpo = {
        "id_usuario": id_usuario,
        "id_fantasma": fantasma["id_fantasma"],
        "latitude": local["latitude"],
        "longitude": local["longitude"],
    }

    r1 = cliente.post("/captura", json=corpo)
    r2 = cliente.post("/captura", json=corpo)

    assert r1.status_code == 201
    assert r2.status_code == 201
    assert r2.get_json()["pontos_totais"] == 2 * r1.get_json()["pontos_ganhos"]