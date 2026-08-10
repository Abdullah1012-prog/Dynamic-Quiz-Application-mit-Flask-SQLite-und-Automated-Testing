# ❓ Dynamic Quiz Application (Flask, SQLite & Pytest)

Eine dynamische, datenbankgestützte Webanwendung für Quiz-Fragen zu verschiedenen Themenbereichen (z. B. Informatik, Mathematik, Physik), entwickelt mit **Python (Flask)** und **SQLite**.

---

## 📌 Über das Projekt

Diese Anwendung ermöglicht es Nutzern, Quiz-Kategorien auszuwählen und zufällig generierte Fragen-Sets zu beantworten. Das Projekt beinhaltet eine serverseitige Auswertungslogik für Punkte und Antworten sowie eine automatisierte Testsuite mit **Pytest**.

### 🌟 Hauptmerkmale

- 🗄️ **SQLite-Datenbankanbindung:** Dynamisches Laden von Multiple-Choice-Fragen sortiert nach Kategorien und zufälliger Auswahl.
- 🎯 **Serverseitige Auswertung:** Präzise Berechnung des Punktestands und Gegenüberstellung von abgegebenen Nutzerantworten und korrekten Lösungen.
- 🧪 **Automatisierte Tests:** Vollständige Testabdeckung der Flask-Routen, Formularverarbeitungen und Datenbankzugriffe mittels Pytest.
- 📐 **Vielfältige Themen:** Unterstützt Fragen aus Informatik (Computer Science), Mathematik, Physik u. v. m.

---

## 🛠️ Technologien

- **Backend:** Python 3, Flask, CS50 SQL Library
- **Datenbank:** SQLite3
- **Testing:** Pytest
- **Frontend:** HTML5, CSS3, Jinja2 Templating

---

## 📂 Projektstruktur

```text
├── app.py              # Flask-Hauptanwendung & Routen-Logik (/index, /submit)
├── questions.db        # SQLite-Datenbank mit Kategorien & Fragen
├── test_app.py         # Pytest Testsuite für Routen & DB-Abfragen
├── requirements.txt    # Abhängigkeiten (Flask, Pytest, CS50)
└── templates/          # Jinja2-Templates (index.html, quiz.html, results.html)
