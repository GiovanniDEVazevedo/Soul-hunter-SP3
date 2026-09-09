from collections import Counter

from services.gerador_fantasma import gerar_fantasma

RARIDADES = {"COMUM", "RARO", "EPICO", "LENDARIO"}


def _validar_fantasma(f):
    assert set(f.keys()) == {"seed", "raridade", "partes"}
    assert 0 <= f["seed"] < 2**32
    assert f["raridade"] in RARIDADES
    for parte in ("corpo", "olho", "boca"):
        assert parte in f["partes"]


def test_gerar_100_fantasmas_sem_erro():
    for _ in range(100):
        _validar_fantasma(gerar_fantasma())


def test_gerar_1000_fantasmas_sem_erro():
    fantasmas = [gerar_fantasma() for _ in range(1000)]
    assert len(fantasmas) == 1000
    for f in fantasmas:
        _validar_fantasma(f)


def test_distribuicao_de_raridade_em_1000():
    contagem = Counter(gerar_fantasma()["raridade"] for _ in range(1000))
    assert contagem["COMUM"] > contagem["RARO"] > contagem["EPICO"] > contagem["LENDARIO"]
    assert contagem["LENDARIO"] > 0


def test_seeds_repetidas_em_1000():
    seeds = [gerar_fantasma()["seed"] for _ in range(1000)]
    duplicadas = len(seeds) - len(set(seeds))
    assert duplicadas < 5


def test_combinacoes_de_partes_chegam_ao_limite_do_pool():
    fantasmas = [gerar_fantasma() for _ in range(10000)]
    configs = set()
    for f in fantasmas:
        partes_hashaveis = tuple(
            (chave, tuple(valor) if isinstance(valor, list) else valor)
            for chave, valor in f["partes"].items()
        )
        configs.add((f["raridade"], partes_hashaveis))
    print(f"\nINFO - 10.000 gerados, {len(configs)} combinações distintas")
    assert len(configs) > 100
    assert len(configs) < len(fantasmas)