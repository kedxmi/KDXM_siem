import sqlite3
import random
import time
from datetime import datetime

# Создаем БД
conn = sqlite3.connect("db/siem.db")  # база создастся автоматически
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    description TEXT,
    timestamp TEXT
)
""")
conn.commit()

print("[+] Database initialized (db/siem.db)")


# Генератор событий
def generate_event():
    """Создает случайное событие"""
    events = [
        ("Brute Force", "3+ неудачных попыток входа подряд"),
        ("Suspicious File", "Обнаружен .exe в каталоге документов"),
        ("HTTP Traffic", "Передача данных по HTTP вместо HTTPS")
    ]
    return random.choice(events)


# Добавление события в базу
def insert_event(event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO events (type, description, timestamp) VALUES (?, ?, ?)",
                   (event[0], event[1], timestamp))
    conn.commit()


# Цикл имитации инцидентов
def simulate_events(count=10, delay=1.5):
    print("[*] Starting event generation...\n")
    for i in range(count):
        event = generate_event()
        insert_event(event)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Detected: {event[0]} — {event[1]}")
        time.sleep(delay)
    print("\n[+] Simulation complete.\n")


# Отчёт по отработке
def generate_report():
    print("[] Security Report:\n")
    cursor.execute("SELECT type, COUNT(*) FROM events GROUP BY type")
    rows = cursor.fetchall()
    for row in rows:
        print(f" - {row[0]}: {row[1]} событий")
    print("\n[✓] Report generated successfully.")


# Точка входа
if __name__ == "__main__":
    simulate_events(count=10, delay=1)
    generate_report()
    conn.close()
