import os

from flask import Flask, jsonify
from flask_cors import CORS
from database.connection import get_connection
from routes.capturas import captura
from routes.fantasma import fantasma
from routes.spawn import spawn
from routes.usuarios import usuario


def criar_app():
    app = Flask(__name__)

    origens_permitidas = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
    CORS(app, origins=origens_permitidas)

    app.register_blueprint(captura)
    app.register_blueprint(fantasma)
    app.register_blueprint(spawn)
    app.register_blueprint(usuario)

    @app.route("/")
    def home():
        return jsonify({
            "message": "Soul Hunter API funcionando!"
        })

    @app.route("/health")
    def health():
        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT 1")
                    resultado = cursor.fetchone()

            return jsonify({
                "status": "online",
                "database": "connected",
                "test": resultado[0]
            })

        except Exception as erro:
            return jsonify({
                "status": "error",
                "database": "disconnected",
                "error": str(erro)
            }), 500

    return app


app = criar_app()


if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG", "false").lower() == "true")