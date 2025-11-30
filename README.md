# 🛰️ KDXM_SIEM

**KDXM_SIEM** is an educational project — a prototype SIEM system implemented in Python.
It provides basic event collection, storage, analysis, and visualization capabilities.

---

## 🎯 Goals

* Gain hands-on experience working with security events.
* Build a custom SIEM-like system with event storage and visualization.
* Demonstrate detection of common cybersecurity incidents.

---

## ⚙️ Features

### 📡 Monitored Event Types

* **Brute Force** — multiple failed authentication attempts
* **Suspicious File** — detection of executable files (.exe)
* **HTTP Traffic** — detection of HTTP usage instead of HTTPS

### 🗄️ Storage

* All events are saved in a **SQLite** database.

### 📊 Visualization

* Statistics displayed via:

  * Console output
  * Graphs powered by **Matplotlib**

### 🚨 Incident Handling

* Automatic incident generation
* Report creation

### 🧩 Technology Stack

* Python **3.10+**
* SQLite3
* Flask
* Matplotlib
* Watchdog (file monitoring)
* Requests

---

## 🚀 Installation & Run

```bash
git clone https://github.com/kedxmi/KDXM_siem.git
cd KDXM_siem

python -m venv venv
source venv/bin/activate  # Linux / macOS
# OR: venv\Scripts\activate  # Windows

pip install -r requirements.txt

python siem.py
```
