import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "contacts.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT
            )
        """)

def add_contact(name, phone, email):
    with get_connection() as conn:
        cursor = conn.cursor()
        # Проверка, есть ли уже такой контакт
        cursor.execute("SELECT id FROM contacts WHERE name = ?", (name,))
        if cursor.fetchone():
            return False, f"Контакт с именем '{name}' уже существует"
        
        cursor.execute(
            "INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)",
            (name, phone, email)
        )
        return True, f"Контакт '{name}' добавлен"

def get_all_contacts():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, phone, email FROM contacts ORDER BY name")
        return cursor.fetchall()

def find_contacts_by_name(name):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, name, phone, email FROM contacts WHERE name LIKE ?",
            (f"%{name}%",)
        )
        return cursor.fetchall()

def update_phone(name, new_phone):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE contacts SET phone = ? WHERE name = ?",
            (new_phone, name)
        )
        return cursor.rowcount  # количество обновлённых строк

def delete_contact(name):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contacts WHERE name = ?", (name,))
        return cursor.rowcount  # количество удалённых строк
    
