from repositories.aplicacao_repository import cadastrar_aplicacao
from repositories.aplicacao_repository import listar_aplicacoes
from repositories.aplicacao_repository import buscar_aplicacao
from repositories.aplicacao_repository import atualizar_aplicacao
from repositories.aplicacao_repository import excluir_aplicacao

from repositories.vacina_repository import buscar_vacina


def salvar_aplicacao(
    id_pessoa,
    id_vacina,
    numero_dose,
    data_aplicacao,
    lote
):
    if id_pessoa == "":
        raise ValueError("Selecione uma pessoa.")

    if id_vacina == "":
        raise ValueError("Selecione uma vacina.")

    if numero_dose == "":
        raise ValueError("Informe o número da dose.")

    if data_aplicacao == "":
        raise ValueError("Informe a data da aplicação.")

    lote = lote.strip()

    if lote == "":
        raise ValueError("Informe o lote da vacina.")

    try:
        id_pessoa = int(id_pessoa)
        id_vacina = int(id_vacina)
        numero_dose = int(numero_dose)
    except ValueError:
        raise ValueError(
            "Os IDs e o número da dose devem ser números inteiros."
        )

    if numero_dose <= 0:
        raise ValueError("O número da dose deve ser maior que zero.")

    vacina = buscar_vacina(id_vacina)

    if vacina is None:
        raise ValueError("Vacina não encontrada.")

    total_doses = vacina[3]

    if numero_dose > total_doses:
        raise ValueError(
            "O número da dose não pode ser maior que o total de doses da vacina."
        )

    cadastrar_aplicacao(
        id_pessoa,
        id_vacina,
        numero_dose,
        data_aplicacao,
        lote
    )


def obter_aplicacoes():
    return listar_aplicacoes()


def obter_aplicacao(id_aplicacao):
    return buscar_aplicacao(id_aplicacao)


def editar_aplicacao(
    id_aplicacao,
    id_pessoa,
    id_vacina,
    numero_dose,
    data_aplicacao,
    lote
):
    if id_pessoa == "":
        raise ValueError("Selecione uma pessoa.")

    if id_vacina == "":
        raise ValueError("Selecione uma vacina.")

    if numero_dose == "":
        raise ValueError("Informe o número da dose.")

    if data_aplicacao == "":
        raise ValueError("Informe a data da aplicação.")

    lote = lote.strip()

    if lote == "":
        raise ValueError("Informe o lote da vacina.")

    try:
        id_pessoa = int(id_pessoa)
        id_vacina = int(id_vacina)
        numero_dose = int(numero_dose)
    except ValueError:
        raise ValueError(
            "Os IDs e o número da dose devem ser números inteiros."
        )

    if numero_dose <= 0:
        raise ValueError("O número da dose deve ser maior que zero.")

    vacina = buscar_vacina(id_vacina)

    if vacina is None:
        raise ValueError("Vacina não encontrada.")

    total_doses = vacina[3]

    if numero_dose > total_doses:
        raise ValueError(
            "O número da dose não pode ser maior que o total de doses da vacina."
        )

    aplicacao = buscar_aplicacao(id_aplicacao)

    if aplicacao is None:
        raise ValueError("Aplicação não encontrada.")

    atualizar_aplicacao(
        id_aplicacao,
        id_pessoa,
        id_vacina,
        numero_dose,
        data_aplicacao,
        lote
    )


def remover_aplicacao(id_aplicacao):
    aplicacao = buscar_aplicacao(id_aplicacao)

    if aplicacao is None:
        raise ValueError("Aplicação não encontrada.")

    excluir_aplicacao(id_aplicacao)