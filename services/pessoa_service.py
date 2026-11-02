from repositories.pessoa_repository import cadastrar_pessoa
from repositories.pessoa_repository import listar_pessoas
from repositories.pessoa_repository import buscar_pessoa
from repositories.pessoa_repository import atualizar_pessoa
from repositories.pessoa_repository import excluir_pessoa


def salvar_pessoa(nome, data_nascimento):
    nome = nome.strip()

    if nome == "":
        raise ValueError("Informe o nome da pessoa.")

    if data_nascimento == "":
        raise ValueError("Informe a data de nascimento.")

    cadastrar_pessoa(nome, data_nascimento)


def obter_pessoas():
    return listar_pessoas()


def obter_pessoa(id_pessoa):
    return buscar_pessoa(id_pessoa)


def editar_pessoa(id_pessoa, nome, data_nascimento):
    nome = nome.strip()

    if nome == "":
        raise ValueError("Informe o nome da pessoa.")

    if data_nascimento == "":
        raise ValueError("Informe a data de nascimento.")

    pessoa = buscar_pessoa(id_pessoa)

    if pessoa is None:
        raise ValueError("Pessoa não encontrada.")

    atualizar_pessoa(id_pessoa, nome, data_nascimento)


def remover_pessoa(id_pessoa):
    pessoa = buscar_pessoa(id_pessoa)

    if pessoa is None:
        raise ValueError("Pessoa não encontrada.")

    excluir_pessoa(id_pessoa)