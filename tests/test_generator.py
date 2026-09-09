import pytest

from services.gerador_fantasma import gerar_fantasma

RARIDADES = {"COMUM", "RARO", "EPICO", "LENDARIO"}

SEED_MAX = 2**32


def test_sem_seed_retorna_objeto_completo():
    fantasma = gerar_fantasma()
    assert set(fantasma.keys()) == {"seed", "raridade", "partes"}


def test_sem_seed_gera_seed_valida():
    fantasma = gerar_fantasma()
    assert isinstance(fantasma["seed"], int)
    assert 0 <= fantasma["seed"] < SEED_MAX


def test_raridade_retornada_e_valida():
    fantasma = gerar_fantasma()
    assert fantasma["raridade"] in RARIDADES


def test_partes_sempre_com_base():
    fantasma = gerar_fantasma()
    for parte in ("corpo", "olho", "boca"):
        assert parte in fantasma["partes"]


def test_mesma_seed_gera_mesmo_fantasma():
    f1 = gerar_fantasma(seed=42)
    f2 = gerar_fantasma(seed=42)
    assert f1 == f2


def test_seed_fornecida_e_mantida_no_retorno():
    f = gerar_fantasma(seed=12345)
    assert f["seed"] == 12345


def test_seed_invalida_levanta_erro():
    with pytest.raises(ValueError):
        gerar_fantasma(seed="abc")


def test_seed_fora_do_intervalo_levanta_erro():
    with pytest.raises(ValueError):
        gerar_fantasma(seed=2**32)
    with pytest.raises(ValueError):
        gerar_fantasma(seed=-1)


def test_limite_superior_e_valid_aceito():
    f = gerar_fantasma(seed=2**32 - 1)
    assert f["seed"] == 2**32 - 1


def test_limite_inferior_e_valido_aceito():
    f = gerar_fantasma(seed=0)
    assert f["seed"] == 0