import pytest

from data.fantasma_part import sortear_partes

RARIDADES = ["COMUM", "RARO", "EPICO", "LENDARIO"]


def test_partes_basicas_sempre_presentes():
    for raridade in RARIDADES:
        partes = sortear_partes(raridade)
        assert "corpo" in partes
        assert "olho" in partes
        assert "boca" in partes


def test_acessorios_sempre_lista_quando_presente():
    for raridade in ["RARO", "EPICO", "LENDARIO"]:
        partes = sortear_partes(raridade)
        assert isinstance(partes["acessorios"], list)


def test_comum_nao_tem_acessorios_nem_aura_nem_efeito():
    partes = sortear_partes("COMUM")
    assert "acessorios" not in partes
    assert "aura" not in partes
    assert "efeito" not in partes


def test_raro_tem_um_acessorio():
    partes = sortear_partes("RARO")
    assert len(partes["acessorios"]) == 1
    assert "aura" not in partes
    assert "efeito" not in partes


def test_epico_tem_dois_acessorios_e_aura():
    partes = sortear_partes("EPICO")
    assert len(partes["acessorios"]) == 2
    assert "aura" in partes
    assert "efeito" not in partes


def test_lendario_tem_tudo():
    partes = sortear_partes("LENDARIO")
    assert len(partes["acessorios"]) == 2
    assert "aura" in partes
    assert "efeito" in partes


def test_valores_sao_identificadores_validos():
    partes = sortear_partes("LENDARIO")
    for chave, valor in partes.items():
        if isinstance(valor, list):
            for item in valor:
                assert isinstance(item, str) and item
        else:
            assert isinstance(valor, str) and valor