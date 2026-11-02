from flask import Flask
from dotenv import load_dotenv
from database.conexao import conectar

from routes.pessoas import pessoas_bp
from routes.vacinas import vacinas_bp
from routes.aplicacoes import aplicacoes_bp

load_dotenv()

app = Flask(__name__)

app.register_blueprint(pessoas_bp)
app.register_blueprint(vacinas_bp)
app.register_blueprint(aplicacoes_bp)

@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/db-test")
def testar_banco():
    conexao = None

    try:
        conexao = conectar()

        return {
            "status": "ok",
            "mensagem": "Conexão com PostgreSQL realizada com sucesso!"
        }

    except Exception as erro:
        app.logger.exception("Erro ao conectar ao banco Neon")
        return {
        "status": "erro",
        "mensagem": "Não foi possível conectar ao banco de dados."
    }, 500

    finally:
        if conexao is not None:
            conexao.close()


import os

if __name__ == "__main__":
    porta = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=porta, debug=False)