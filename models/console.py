from config.conexao import get_connection
class ConsoleModel:
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, nome, ano, empresa, historia FROM consoles")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_by_id(console_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, nome, ano, empresa, historia FROM consoles WHERE id = %s", (console_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result


@staticmethod
def insert(dados):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO noticias (nome, ano, empresa, historia) VALUES (%s, %s, %s, %s)"
    valores = (dados.get('nome'), dados.get('ano'), dados.get('empresa'), dados.get('historia'))
    cursor.execute(sql, valores)
    conn.commit()
    last_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return last_id

@staticmethod
def update(console_id, dados):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE consoles set nome=%s, ano=%s, empresa%s, historia=%s WHERE id=%s"
    valores = (dados.get('nome'), dados.get('ano'), dados.get('historia'), console_id)
    cursor.execute(sql, valores)
    conn.commit()
    rowcount = cursor.rowcount
    cursor.close()
    conn.close()
    return rowcount > 0

@staticmethod
def delete(console_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM consoles WHERE id = %s"
    valores = (console_id,)
    cursor.execute(sql, valores)
    conn.commit()
    rowcount = cursor.rowcount
    cursor.close()
    conn.close()
    return rowcount > 0