from flask import Blueprint, render_template, request, redirect, url_for
from services.pessoa_service import salvar_pessoa, obter_pessoas
from services.pessoa_service import obter_pessoa, editar_pessoa, remover_pessoa

pessoas_bp = Blueprint("pessoas", __name__)


@pessoas_bp.route("/")
def inicio():
    pessoas = obter_pessoas()
    mensagem = request.args.get("mensagem", "")

    return render_template(
        "index.html",
        pessoas=pessoas,
        mensagem=mensagem
    )


@pessoas_bp.route("/pessoas/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form.get("nome", "")
    data_nascimento = request.form.get("data_nascimento", "")

    try:
        salvar_pessoa(nome, data_nascimento)

        return redirect(
            url_for(
                "pessoas.inicio",
                mensagem="Pessoa cadastrada com sucesso!"
            )
        )

    except ValueError as erro:
        return redirect(
            url_for("pessoas.inicio", mensagem=str(erro))
        )

    except Exception:
        return redirect(
            url_for(
                "pessoas.inicio",
                mensagem="Não foi possível cadastrar a pessoa."
            )
        )


@pessoas_bp.route("/pessoas/editar/<int:id_pessoa>", methods=["GET"])
def formulario_edicao(id_pessoa):
    pessoa = obter_pessoa(id_pessoa)

    if pessoa is None:
        return redirect(
            url_for(
                "pessoas.inicio",
                mensagem="Pessoa não encontrada."
            )
        )

    return render_template(
        "editar_pessoa.html",
        pessoa=pessoa
    )


@pessoas_bp.route("/pessoas/editar/<int:id_pessoa>", methods=["POST"])
def salvar_edicao(id_pessoa):
    nome = request.form.get("nome", "")
    data_nascimento = request.form.get("data_nascimento", "")

    try:
        editar_pessoa(id_pessoa, nome, data_nascimento)

        return redirect(
            url_for(
                "pessoas.inicio",
                mensagem="Pessoa alterada com sucesso!"
            )
        )

    except ValueError as erro:
        return redirect(
            url_for("pessoas.inicio", mensagem=str(erro))
        )

    except Exception:
        return redirect(
            url_for(
                "pessoas.inicio",
                mensagem="Não foi possível alterar a pessoa."
            )
        )


@pessoas_bp.route("/pessoas/excluir/<int:id_pessoa>", methods=["POST"])
def excluir(id_pessoa):
    try:
        remover_pessoa(id_pessoa)

        return redirect(
            url_for(
                "pessoas.inicio",
                mensagem="Pessoa excluída com sucesso!"
            )
        )

    except ValueError as erro:
        return redirect(
            url_for("pessoas.inicio", mensagem=str(erro))
        )

    except Exception:
        return redirect(
            url_for(
                "pessoas.inicio",
                mensagem="Não foi possível excluir a pessoa. Verifique se existem aplicações de vacinas vinculadas a ela."
            )
        )