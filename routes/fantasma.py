from flask import Blueprint, jsonify, request

from services.servico_fantasma import (
    buscar_fantasma,
    gerar_e_salvar_fantasma,
    investigar_casa,
)

fantasma = Blueprint("fantasma", __name__)


@fantasma.route("/fantasma", methods=["POST"])
def criar_fantasma():
    corpo = request.get_json(silent=True) or {}
    fantasma = gerar_e_salvar_fantasma(seed=corpo.get("seed"))
    return jsonify(fantasma), 201


@fantasma.route("/casa/investigar", methods=["POST"])
def investigar():
    return jsonify(investigar_casa()), 201
@fantasma.route("/fantasma/<int:id_fantasma>", methods=["GET"])
def obter_fantasma(id_fantasma):
    fantasma_encontrado =buscar_fantasma(id_fantasma)

    if fantasma_encontrado is None:
        return jsonify({"message": "fantasma nao encontrado"}), 404
    return jsonify(fantasma_encontrado)