
from database.conexao import conectar


def cadastrar_pessoa(nome, data_nascimento):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            INSERT INTO pessoas (nome, data_nascimento)
            VALUES (%s, %s)
            """,
            (nome, data_nascimento)
        )

        conexao.commit()

    finally:
        conexao.close()


def listar_pessoas():
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT id_pessoa, nome, data_nascimento
            FROM pessoas
            ORDER BY nome
            """
        )

        pessoas = cursor.fetchall()

        return pessoas

    finally:
        conexao.close()

def buscar_pessoa(id_pessoa):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT id_pessoa, nome, data_nascimento
            FROM pessoas
            WHERE id_pessoa = %s
            """,
            (id_pessoa,)
        )

        pessoa = cursor.fetchone()

        return pessoa

    finally:
        conexao.close()


def atualizar_pessoa(id_pessoa, nome, data_nascimento):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            UPDATE pessoas
            SET nome = %s, data_nascimento = %s
            WHERE id_pessoa = %s
            """,
            (nome, data_nascimento, id_pessoa)
        )

        conexao.commit()

    finally:
        conexao.close()


def excluir_pessoa(id_pessoa):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            DELETE FROM pessoas
            WHERE id_pessoa = %s
            """,
            (id_pessoa,)
        )

        conexao.commit()

    finally:
        conexao.close()