from flask import Blueprint, render_template, request, redirect, url_for
from services.vacina_service import salvar_vacina, obter_vacinas
from services.vacina_service import obter_vacina, editar_vacina, remover_vacina

vacinas_bp = Blueprint("vacinas", __name__)


@vacinas_bp.route("/vacinas")
def inicio():
    vacinas = obter_vacinas()
    mensagem = request.args.get("mensagem", "")

    return render_template(
        "vacinas.html",
        vacinas=vacinas,
        mensagem=mensagem
    )


@vacinas_bp.route("/vacinas/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form.get("nome", "")
    fabricante = request.form.get("fabricante", "")
    total_doses = request.form.get("total_doses", "")

    try:
        salvar_vacina(nome, fabricante, total_doses)

        return redirect(
            url_for(
                "vacinas.inicio",
                mensagem="Vacina cadastrada com sucesso!"
            )
        )

    except ValueError as erro:
        return redirect(
            url_for("vacinas.inicio", mensagem=str(erro))
        )

    except Exception:
        return redirect(
            url_for(
                "vacinas.inicio",
                mensagem="Não foi possível cadastrar a vacina."
            )
        )


@vacinas_bp.route("/vacinas/editar/<int:id_vacina>", methods=["GET"])
def formulario_edicao(id_vacina):
    vacina = obter_vacina(id_vacina)

    if vacina is None:
        return redirect(
            url_for(
                "vacinas.inicio",
                mensagem="Vacina não encontrada."
            )
        )

    return render_template(
        "editar_vacinas.html",
        vacina=vacina
    )


@vacinas_bp.route("/vacinas/editar/<int:id_vacina>", methods=["POST"])
def salvar_edicao(id_vacina):
    nome = request.form.get("nome", "")
    fabricante = request.form.get("fabricante", "")
    total_doses = request.form.get("total_doses", "")

    try:
        editar_vacina(id_vacina, nome, fabricante, total_doses)

        return redirect(
            url_for(
                "vacinas.inicio",
                mensagem="Vacina alterada com sucesso!"
            )
        )

    except ValueError as erro:
        return redirect(
            url_for("vacinas.inicio", mensagem=str(erro))
        )

    except Exception:
        return redirect(
            url_for(
                "vacinas.inicio",
                mensagem="Não foi possível alterar a vacina."
            )
        )


@vacinas_bp.route("/vacinas/excluir/<int:id_vacina>", methods=["POST"])
def excluir(id_vacina):
    try:
        remover_vacina(id_vacina)

        return redirect(
            url_for(
                "vacinas.inicio",
                mensagem="Vacina excluída com sucesso!"
            )
        )

    except ValueError as erro:
        return redirect(
            url_for("vacinas.inicio", mensagem=str(erro))
        )

    except Exception:
        return redirect(
            url_for(
                "vacinas.inicio",
                mensagem="Não foi possível excluir a vacina. Verifique se existem aplicações vinculadas a ela."
            )
        )