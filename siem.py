
import sqlite3

# Создание или подключение к базе данных
conn = sqlite3.connect('siem.db')
cursor = conn.cursor()

# Таблица для событий
cursor.execute('''
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    description TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()
print("[+] Database initialized.")
