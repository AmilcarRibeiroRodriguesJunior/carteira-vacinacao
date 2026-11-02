from database.conexao import conectar


def cadastrar_aplicacao(id_pessoa, id_vacina, numero_dose, data_aplicacao, lote):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            INSERT INTO aplicacoes (
                id_pessoa,
                id_vacina,
                numero_dose,
                data_aplicacao,
                lote
            )
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                id_pessoa,
                id_vacina,
                numero_dose,
                data_aplicacao,
                lote
            )
        )

        conexao.commit()

    finally:
        conexao.close()


def listar_aplicacoes():
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT
                a.id_aplicacao,
                p.nome,
                v.nome,
                a.numero_dose,
                a.data_aplicacao,
                a.lote
            FROM aplicacoes a
            INNER JOIN pessoas p
                ON a.id_pessoa = p.id_pessoa
            INNER JOIN vacinas v
                ON a.id_vacina = v.id_vacina
            ORDER BY a.data_aplicacao DESC
            """
        )

        aplicacoes = cursor.fetchall()

        return aplicacoes

    finally:
        conexao.close()


def buscar_aplicacao(id_aplicacao):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT
                id_aplicacao,
                id_pessoa,
                id_vacina,
                numero_dose,
                data_aplicacao,
                lote
            FROM aplicacoes
            WHERE id_aplicacao = %s
            """,
            (id_aplicacao,)
        )

        aplicacao = cursor.fetchone()

        return aplicacao

    finally:
        conexao.close()


def atualizar_aplicacao(
    id_aplicacao,
    id_pessoa,
    id_vacina,
    numero_dose,
    data_aplicacao,
    lote
):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            UPDATE aplicacoes
            SET
                id_pessoa = %s,
                id_vacina = %s,
                numero_dose = %s,
                data_aplicacao = %s,
                lote = %s
            WHERE id_aplicacao = %s
            """,
            (
                id_pessoa,
                id_vacina,
                numero_dose,
                data_aplicacao,
                lote,
                id_aplicacao
            )
        )

        conexao.commit()

    finally:
        conexao.close()


def excluir_aplicacao(id_aplicacao):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            DELETE FROM aplicacoes
            WHERE id_aplicacao = %s
            """,
            (id_aplicacao,)
        )

        conexao.commit()

    finally:
        conexao.close()