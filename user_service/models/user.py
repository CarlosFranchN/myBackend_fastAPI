from db_config import get_db_conn


def create_user(username,password):
    conn = None
    try:
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO usuarios (username, password)
            VALUES (%s, %s)
            RETURNING id
        """, (username, password))
        usuario_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        return {"id": usuario_id, "username": username}
    except Exception as e:
        if conn:
            conn.rollback()
        raise e
    finally:
        if conn:
            conn.close()
            
def get_all_users():
    conn = None
    try:
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute("SELECT id, username FROM usuarios;")
        rows = cur.fetchall()
        cur.close()
        return [{"id": row[0], "username": row[1]} for row in rows]
    finally:
        if conn:
            conn.close()
            
            