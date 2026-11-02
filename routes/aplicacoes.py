from flask import Blueprint, render_template, request, redirect, url_for

from services.aplicacao_service import salvar_aplicacao
from services.aplicacao_service import obter_aplicacoes
from services.aplicacao_service import obter_aplicacao
from services.aplicacao_service import editar_aplicacao
from services.aplicacao_service import remover_aplicacao

from services.pessoa_service import obter_pessoas
from services.vacina_service import obter_vacinas


aplicacoes_bp = Blueprint("aplicacoes", __name__)


@aplicacoes_bp.route("/aplicacoes")
def inicio():
    aplicacoes = obter_aplicacoes()
    pessoas = obter_pessoas()
    vacinas = obter_vacinas()
    mensagem = request.args.get("mensagem", "")

    return render_template(
        "aplicacoes.html",
        aplicacoes=aplicacoes,
        pessoas=pessoas,
        vacinas=vacinas,
        mensagem=mensagem
    )


@aplicacoes_bp.route("/aplicacoes/cadastrar", methods=["POST"])
def cadastrar():
    id_pessoa = request.form.get("id_pessoa", "")
    id_vacina = request.form.get("id_vacina", "")
    numero_dose = request.form.get("numero_dose", "")
    data_aplicacao = request.form.get("data_aplicacao", "")
    lote = request.form.get("lote", "")

    try:
        salvar_aplicacao(
            id_pessoa,
            id_vacina,
            numero_dose,
            data_aplicacao,
            lote
        )

        return redirect(
            url_for(
                "aplicacoes.inicio",
                mensagem="Aplicação cadastrada com sucesso!"
            )
        )

    except ValueError as erro:
        return redirect(
            url_for("aplicacoes.inicio", mensagem=str(erro))
        )

    except Exception:
        return redirect(
            url_for(
                "aplicacoes.inicio",
                mensagem="Não foi possível cadastrar a aplicação. Verifique os dados informados."
            )
        )


@aplicacoes_bp.route("/aplicacoes/editar/<int:id_aplicacao>", methods=["GET"])
def formulario_edicao(id_aplicacao):
    aplicacao = obter_aplicacao(id_aplicacao)

    if aplicacao is None:
        return redirect(
            url_for(
                "aplicacoes.inicio",
                mensagem="Aplicação não encontrada."
            )
        )

    pessoas = obter_pessoas()
    vacinas = obter_vacinas()

    return render_template(
        "editar_aplicacao.html",
        aplicacao=aplicacao,
        pessoas=pessoas,
        vacinas=vacinas
    )


@aplicacoes_bp.route("/aplicacoes/editar/<int:id_aplicacao>", methods=["POST"])
def salvar_edicao(id_aplicacao):
    id_pessoa = request.form.get("id_pessoa", "")
    id_vacina = request.form.get("id_vacina", "")
    numero_dose = request.form.get("numero_dose", "")
    data_aplicacao = request.form.get("data_aplicacao", "")
    lote = request.form.get("lote", "")

    try:
        editar_aplicacao(
            id_aplicacao,
            id_pessoa,
            id_vacina,
            numero_dose,
            data_aplicacao,
            lote
        )

        return redirect(
            url_for(
                "aplicacoes.inicio",
                mensagem="Aplicação alterada com sucesso!"
            )
        )

    except ValueError as erro:
        return redirect(
            url_for("aplicacoes.inicio", mensagem=str(erro))
        )

    except Exception:
        return redirect(
            url_for(
                "aplicacoes.inicio",
                mensagem="Não foi possível alterar a aplicação."
            )
        )


@aplicacoes_bp.route("/aplicacoes/excluir/<int:id_aplicacao>", methods=["POST"])
def excluir(id_aplicacao):
    try:
        remover_aplicacao(id_aplicacao)

        return redirect(
            url_for(
                "aplicacoes.inicio",
                mensagem="Aplicação excluída com sucesso!"
            )
        )

    except ValueError as erro:
        return redirect(
            url_for("aplicacoes.inicio", mensagem=str(erro))
        )

    except Exception:
        return redirect(
            url_for(
                "aplicacoes.inicio",
                mensagem="Não foi possível excluir a aplicação."
            )
        )