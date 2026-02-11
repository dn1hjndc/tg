import sqlite3

# Создаем соединение
conn = sqlite3.connect('quiz.db')
cursor = conn.cursor()

# 1. Исправляем структуру таблицы: добавляем нужные колонки
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    score INTEGER DEFAULT 0
)
''')

# 2. Добавляем одну запись, где сразу есть и имя, и очки
# Используем параметры (?), чтобы избежать SQL-инъекций (хорошая привычка)
cursor.execute("INSERT INTO users (username, score) VALUES (?, ?)", ('player №1', 0))

# Сохраняем изменения
conn.commit()

# 3. Исправляем запрос: выбираем данные ИЗ ТАБЛИЦЫ users
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("Таблица users создана и наполнена данными:")
print(f"{'ID':<3} | {'Username':<15} | {'Score':<5}")
print("-" * 30)

for row in rows:
    # row[0] - id, row[1] - username, row[2] - score
    print(f"{row[0]:<3} | {row[1]:<15} | {row[2]:<5}")

# Закрываем соединение
conn.close()

print("\nБаза данных 'quiz.db' успешно обновлена!")