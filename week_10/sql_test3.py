import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

def create_table(cursor):
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS productions (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   price INTEGER NOT NULL
                   )
                   """)

def add_product(cursor, name, price):
    cursor.execute("INSERT INTO productions (name, price) VALUES (?, ?)",
                   (name, price))
    
def get_all_products(cursor):
    cursor.execute("SELECT id, name, price FROM productions ORDER BY name")
    return cursor.fetchall()

def price_upd(cursor, name, new_price):
    cursor.execute("UPDATE productions SET price = ? WHERE name = ?",
                   (new_price, name))
    
def delete_product(cursor, name):
    cursor.execute("DELETE FROM productions WHERE name = ?",
                   (name, ))
    return cursor.rowcount

if __name__ == "__main__":
    conn = sqlite3.connect("productions.db")
    cursor = conn.cursor()

    create_table(cursor)

    add_product(cursor, "апельсин", 110)
    add_product(cursor, "клубника", 240)
    add_product(cursor, "банан", 90)
    conn.commit()

    print("Все товары:")
    for row in get_all_products(cursor):
        print(row)

    price_upd(cursor, "клубника", 200)
    conn.commit()

    print("После обновления:")
    for row in get_all_products(cursor):
        print(row)

    delete_product(cursor, "банан")
    conn.commit()

    print("После удаления:")
    for row in get_all_products(cursor):
        print(row)