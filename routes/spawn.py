from flask import Blueprint, jsonify

from services.servico_spawn import listar_spawns

spawn = Blueprint("spawn", __name__)

@spawn.route("/spawn", methods=["GET"])
def obter_spawns():
    return jsonify(listar_spawns())