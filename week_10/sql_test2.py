import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

def create_table(cursor):
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS products (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   price INTEGER NOT NULL
                )
    """)

def add_product(cursor, name, price):
    cursor.execute(
        "INSERT INTO products (name, price) VALUES (?, ?)", (name, price)
)
    
def get_all_products(cursor):
    cursor.execute("SELECT id, name, price FROM products ORDER BY name")
    return cursor.fetchall()

def update_price(cursor, name, new_price):
    cursor.execute("UPDATE products SET price = ? WHERE name = ?",
                   (new_price, name)
                   )

def delete_product(cursor, name):
    cursor.execute("DELETE FROM products WHERE name = ?",
                   (name, )
                   )
    return cursor.rowcount

if __name__ == "__main__":
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    
    create_table(cursor)
    
    add_product(cursor, "яблоки", 100)
    add_product(cursor, "бананы", 80)
    add_product(cursor, "апельсины", 120)
    conn.commit()
    
    print("Все товары:")
    for row in get_all_products(cursor):
        print(row)
    
    update_price(cursor, "бананы", 90)
    conn.commit()
    
    print("\nПосле обновления:")
    for row in get_all_products(cursor):
        print(row)
    
    delete_product(cursor, "апельсины")
    conn.commit()
    
    print("\nПосле удаления:")
    for row in get_all_products(cursor):
        print(row)
    
    conn.close()