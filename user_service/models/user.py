from db_config import get_db_conn
from service.auth import get_password_hash



def create_user(username, password):
    conn = None
    
    try:
        if not username or not password:
            raise ValueError("Username e password são obrigatórios")
        hashed_password = get_password_hash(password)
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO "Users" (username, password)
            VALUES (%s, %s)
            RETURNING id
        """, (username, hashed_password))
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
            
def get_tables_from_db():
    conn = get_db_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT table_name
        FROM information_schema.tables 
        WHERE table_schema = 'public';
    """)
    tables = cur.fetchall()

    cur.close()
    conn.close()

    return [table[0] for table in tables]
            
            