import sys
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

from repositories.repositorio_fantasma import (
    buscar_fantasma_por_id,
    salvar_fantasma,
)
from services.gerador_fantasma import gerar_fantasma


@pytest.fixture
def fantasma_qualquer():
    return gerar_fantasma()


def test_salvar_fantasma_retorna_id_inteiro(fantasma_qualquer):
    id_fantasma = salvar_fantasma(fantasma_qualquer)
    assert isinstance(id_fantasma, int)
    assert id_fantasma > 0


def test_ciclo_salvar_e_buscar(fantasma_qualquer):
    id_fantasma = salvar_fantasma(fantasma_qualquer)
    fantasma = buscar_fantasma_por_id(id_fantasma)

    assert fantasma is not None
    assert fantasma["id_fantasma"] == id_fantasma
    assert fantasma["seed"] == fantasma_qualquer["seed"]
    assert fantasma["raridade"] == fantasma_qualquer["raridade"]
    assert fantasma["corpo"] == fantasma_qualquer["partes"]["corpo"]
    assert fantasma["olho"] == fantasma_qualquer["partes"]["olho"]
    assert fantasma["boca"] == fantasma_qualquer["partes"]["boca"]


def test_ciclo_salvar_e_buscar_com_acessorios():
    fantasma = gerar_fantasma()
    while fantasma["raridade"] != "EPICO":
        fantasma = gerar_fantasma()

    id_fantasma = salvar_fantasma(fantasma)
    fantasma_lido = buscar_fantasma_por_id(id_fantasma)

    assert fantasma_lido is not None
    assert fantasma_lido["acessorios"] == fantasma["partes"]["acessorios"]
    assert isinstance(fantasma_lido["acessorios"], list)


def test_buscar_id_inexistente_retorna_none():
    assert buscar_fantasma_por_id(999_999_999) is None