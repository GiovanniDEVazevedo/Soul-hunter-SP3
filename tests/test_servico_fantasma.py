import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

from services.servico_fantasma import buscar_fantasma, gerar_e_salvar_fantasma


def test_gerar_e_salvar_devolve_chaves_completas():
    fantasma = gerar_e_salvar_fantasma()

    assert isinstance(fantasma["id_fantasma"], int)
    assert fantasma["id_fantasma"] > 0
    assert isinstance(fantasma["seed"], int)
    assert fantasma["raridade"] in {"COMUM", "RARO", "EPICO", "LENDARIO"}
    assert "corpo" in fantasma["partes"]
    assert "olho" in fantasma["partes"]
    assert "boca" in fantasma["partes"]


def test_gerar_e_salvar_respeita_seed_fornecida():
    fantasma = gerar_e_salvar_fantasma(seed=42)
    assert fantasma["seed"] == 42


def test_fantasma_gerado_e_buscar_recuperam_o_mesmo():
    fantasma = gerar_e_salvar_fantasma(seed=777)
    recuperado = buscar_fantasma(fantasma["id_fantasma"])

    assert recuperado is not None
    assert recuperado["id_fantasma"] == fantasma["id_fantasma"]
    assert recuperado["seed"] == 777


def test_buscar_id_inexistente_devolve_none():
    assert buscar_fantasma(999_999_999) is None