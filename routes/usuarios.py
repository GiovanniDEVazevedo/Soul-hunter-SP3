from flask import Blueprint, jsonify, request

from services.servico_usuario import buscar_usuario, criar_usuario_service

usuario = Blueprint("usuario", __name__)


@usuario.route("/usuario", methods=["POST"])
def cadastrar_usuario():
    corpo = request.get_json(silent=True) or {}
    novo_usuario = criar_usuario_service(
        nome=corpo.get("nome"),
        email=corpo.get("email"),
        senha=corpo.get("senha"),
    )
    return jsonify(novo_usuario), 201


@usuario.route("/usuario/<int:id_usuario>", methods=["GET"])
def obter_usuario(id_usuario):
    dados_usuario = buscar_usuario(id_usuario)

    if dados_usuario is None:
        return jsonify({"message": "usuario nao encontrado"}), 404
    return jsonify(dados_usuario)

