from flask import Blueprint, jsonify, request

from services.servico_captura import captura_fantasma

captura = Blueprint("captura", __name__)


@captura.route("/captura", methods=["POST"])
def realizar_captura():
    corpo = request.get_json(silent=True) or {}

    resultado, status = captura_fantasma(
        id_usuario=corpo.get("id_usuario"),
        id_fantasma=corpo.get("id_fantasma"),
        latitude=corpo.get("latitude"),
        longitude=corpo.get("longitude"),
    )
    return jsonify(resultado), status