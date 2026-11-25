# Dynamic Quiz Application

A Flask-based quiz application that serves randomized questions from a SQLite database. Choose a category, answer a 20-question quiz, and review your score with answer-by-answer feedback.

## Features

- Three quiz categories: Computer, Math, and Physics
- Random selection of up to 20 questions from the selected category
- Multiple-choice questions with four answer options
- Results page showing the score and the correct answer for each question
- Automated tests with Pytest

## Requirements

- Python 3.7 or later
- pip
- The included `questions.db` SQLite database

## Setup

1. Clone the repository and enter its directory:

   ```bash
   git clone https://github.com/Abdullah1012-prog/Dynamic-Quiz-Application-mit-Flask-SQLite-und-Automated-Testing.git
   cd Dynamic-Quiz-Application-mit-Flask-SQLite-und-Automated-Testing
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

   On macOS or Linux:

   ```bash
   source venv/bin/activate
   ```

   On Windows PowerShell:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Run the application

Start the Flask development server:

```bash
python app.py
```

Open <http://127.0.0.1:5000/> in your browser, select a category, and submit your answers to see your results.

## Run the tests

```bash
pytest
```

For verbose test output:

```bash
pytest -v
```

## Project structure

```text
.
├── app.py                    # Flask routes and quiz submission logic
├── questions.db              # SQLite question database
├── requirements.txt          # Python dependencies
├── test_app.py               # Pytest tests
└── templates/
    ├── index.html            # Category selection page
    ├── layout.html           # Shared page layout
    ├── quiz.html             # Quiz questions and answer options
    └── results.html          # Score and answer feedback
```

See [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md) for additional setup and troubleshooting details.
