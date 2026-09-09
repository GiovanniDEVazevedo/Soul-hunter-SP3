from collections import Counter

from services.rarity_service import sortear_raridade

RARIDADES = {"COMUM", "RARO", "EPICO", "LENDARIO"}


def test_raridade_sempre_valida():
    for _ in range(1000):
        assert sortear_raridade() in RARIDADES


def test_todas_as_raridades_aparecem():
    contagem = Counter(sortear_raridade() for _ in range(10000))
    for raridade in RARIDADES:
        assert contagem[raridade] > 0


def test_distribuicao_respeita_ordem_de_probabilidade():
    contagem = Counter(sortear_raridade() for _ in range(20000))
    assert contagem["COMUM"] > contagem["RARO"] > contagem["EPICO"] > contagem["LENDARIO"]