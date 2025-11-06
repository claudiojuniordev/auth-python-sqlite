import bcrypt
from db.connection import get_connection
from datetime import datetime

def _user_exists_by_login(login: str) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM users WHERE login = ?", (login,))
    exists = cur.fetchone() is not None
    conn.close()
    return exists

def register_user(name: str, login: str, password: str) -> bool:
    """Retorna True se criado, False se login já existe."""
    if _user_exists_by_login(login):
        return False

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (name, login, password_hash, created_at) VALUES (?, ?, ?, ?)",
        (name, login, hashed, datetime.utcnow().isoformat())
    )
    conn.commit()
    conn.close()
    return True

def login_user(identifier: str, password: str) -> tuple[bool, str | None]:
    """Tenta logar por login OU name. Retorna (sucesso, nome_do_usuario).


    Ex: (True, "Claudio") ou (False, None)
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT name, password_hash FROM users WHERE login = ? OR name = ? LIMIT 1",
        (identifier, identifier)
    )
    row = cur.fetchone()
    conn.close()


    if row is None:
        return False, None


    stored_hash = row['password_hash'].encode('utf-8')
    ok = bcrypt.checkpw(password.encode('utf-8'), stored_hash)
    if ok:
        return True, row['name']
    return False, None

# Função utilitária para debug/desenvolvimento
def list_users(limit: int = 50):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, login, created_at FROM users LIMIT ?", (limit,))
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def delete_user(identifier: str | int) -> bool:
    """Exclui um usuário por id ou login.
    
    Args:
        identifier: ID (int) ou login (str) do usuário
    
    Returns:
        bool: True se um usuário foi excluído, False caso contrário
    """
    conn = get_connection()
    cur = conn.cursor()
    
    if isinstance(identifier, int) or (isinstance(identifier, str) and identifier.isdigit()):
        cur.execute("DELETE FROM users WHERE id = ?", (int(identifier),))
    else:
        cur.execute("DELETE FROM users WHERE login = ?", (str(identifier),))
    
    deleted = cur.rowcount > 0
    conn.commit()
    conn.close()
    return deleted