from repositories.vacina_repository import cadastrar_vacina
from repositories.vacina_repository import listar_vacinas
from repositories.vacina_repository import buscar_vacina
from repositories.vacina_repository import atualizar_vacina
from repositories.vacina_repository import excluir_vacina


def salvar_vacina(nome, fabricante, total_doses):
    nome = nome.strip()
    fabricante = fabricante.strip()

    if nome == "":
        raise ValueError("Informe o nome da vacina.")

    if total_doses == "":
        raise ValueError("Informe a quantidade de doses.")

    try:
        total_doses = int(total_doses)
    except ValueError:
        raise ValueError("A quantidade de doses deve ser um número inteiro.")

    if total_doses <= 0:
        raise ValueError("A quantidade de doses deve ser maior que zero.")

    cadastrar_vacina(nome, fabricante, total_doses)


def obter_vacinas():
    return listar_vacinas()


def obter_vacina(id_vacina):
    return buscar_vacina(id_vacina)


def editar_vacina(id_vacina, nome, fabricante, total_doses):
    nome = nome.strip()
    fabricante = fabricante.strip()

    if nome == "":
        raise ValueError("Informe o nome da vacina.")

    if total_doses == "":
        raise ValueError("Informe a quantidade de doses.")

    try:
        total_doses = int(total_doses)
    except ValueError:
        raise ValueError("A quantidade de doses deve ser um número inteiro.")

    if total_doses <= 0:
        raise ValueError("A quantidade de doses deve ser maior que zero.")

    vacina = buscar_vacina(id_vacina)

    if vacina is None:
        raise ValueError("Vacina não encontrada.")

    atualizar_vacina(id_vacina, nome, fabricante, total_doses)


def remover_vacina(id_vacina):
    vacina = buscar_vacina(id_vacina)

    if vacina is None:
        raise ValueError("Vacina não encontrada.")

    excluir_vacina(id_vacina)