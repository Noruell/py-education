import sqlite3


conn = sqlite3.connect("online.db")
cursor = conn.cursor()

cursor.execute("""--sql
            CREATE TABLE IF NOT EXISTS users ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
)""")

names = ['Максим', 'Ксюша', 'Саша', 'Света']
ages = [20, 18, 14, 10]

users = []
for i in range(len(names)):
    users.append((names[i], ages[i]))



cursor.executemany(
    "INSERT INTO users (name, age) VALUES (?, ?)",
    users
)
print(f"Добавленно {len(users)} пользователей")

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)


conn.commit()
conn.close()
