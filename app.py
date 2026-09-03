from flask import Flask, jsonify
from database.connection import get_connection

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Soul Up API funcionando!"
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


if __name__ == "__main__":
    app.run(debug=True)