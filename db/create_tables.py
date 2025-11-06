from .connection import get_connection
import datetime


CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    login TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TEXT NOT NULL
)
"""

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CREATE_USERS_TABLE)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Tabelas criadas (ou já existentes).")