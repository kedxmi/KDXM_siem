# 🛰️ KDXM_SIEM

**KDXM_SIEM** — учебный проект.
Проект представляет собой прототип SIEM-системы, реализованной на Python.

---

## 🎯 Цели
- Получение практических навыков работы с событиями ИБ.  
- Разработка собственной SIEM-системы с хранением и визуализацией событий.  
- Демонстрация работы по выявлению типовых инцидентов ИБ.

---

## ⚙️ Функционал
- 📡 Отслеживание **3 типов событий**:
  1. Brute Force (многократные неудачные попытки авторизации);
  2. Suspicious File (обнаружение `экзешников`);
  3. HTTP Traffic (использование HTTP вместо HTTPS).
- 💾 Хранение событий в **SQLite**.
- 📊 Визуализация статистики (через консоль или matplotlib).
- 🚨 Генерация инцидентов и формирование отчёт.

---

## 🧩 Стек
- **Python 3.10+**
- **SQLite3**
- **Flask**
- **Matplotlib**
- **Watchdog** (мониторинг изменений файлов)
- **Requests**

---

## 🚀 Запуск

```bash
git clone https://github.com/kedxmi/KDXM_siem.git
cd KDXM_siem
python -m venv venv
source venv/bin/activate  # Linux
pip install -r requirements.txt
python siem.py
```
