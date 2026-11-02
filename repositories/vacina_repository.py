from database.conexao import conectar


def cadastrar_vacina(nome, fabricante, total_doses):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            INSERT INTO vacinas (nome, fabricante, total_doses)
            VALUES (%s, %s, %s)
            """,
            (nome, fabricante, total_doses)
        )

        conexao.commit()

    finally:
        conexao.close()


def listar_vacinas():
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT id_vacina, nome, fabricante, total_doses
            FROM vacinas
            ORDER BY nome
            """
        )

        vacinas = cursor.fetchall()

        return vacinas

    finally:
        conexao.close()


def buscar_vacina(id_vacina):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT id_vacina, nome, fabricante, total_doses
            FROM vacinas
            WHERE id_vacina = %s
            """,
            (id_vacina,)
        )

        vacina = cursor.fetchone()

        return vacina

    finally:
        conexao.close()


def atualizar_vacina(id_vacina, nome, fabricante, total_doses):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            UPDATE vacinas
            SET nome = %s,
                fabricante = %s,
                total_doses = %s
            WHERE id_vacina = %s
            """,
            (nome, fabricante, total_doses, id_vacina)
        )

        conexao.commit()

    finally:
        conexao.close()


def excluir_vacina(id_vacina):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            DELETE FROM vacinas
            WHERE id_vacina = %s
            """,
            (id_vacina,)
        )

        conexao.commit()

    finally:
        conexao.close()