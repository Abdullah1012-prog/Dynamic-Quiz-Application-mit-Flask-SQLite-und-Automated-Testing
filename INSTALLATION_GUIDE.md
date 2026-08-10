# 📥 Installation Guide - Dynamic Quiz Application

This guide will walk you through setting up the Dynamic Quiz Application (Flask, SQLite & Pytest) on your local machine.

---

## ✅ Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.7 or higher** - Download from [python.org](https://www.python.org/downloads/)
- **pip** (Python Package Manager) - Usually comes with Python
- **Git** - For cloning the repository (optional)
- **Text Editor or IDE** - VS Code, PyCharm, or similar (recommended)

### Verify Your Python Installation

Open your terminal/command prompt and run:

```bash
python --version
# or
python3 --version
```

You should see a version number like `Python 3.9.x` or higher.

---

## 🚀 Step-by-Step Installation

### 1. Clone the Repository

Choose one of the following methods:

#### Option A: Using Git
```bash
git clone https://github.com/Abdullah1012-prog/Dynamic-Quiz-Application-mit-Flask-SQLite-und-Automated-Testing.git
cd Dynamic-Quiz-Application-mit-Flask-SQLite-und-Automated-Testing
```

#### Option B: Download ZIP
- Visit the repository on GitHub
- Click the green "Code" button
- Select "Download ZIP"
- Extract the folder and navigate into it using your terminal

---

### 2. Create a Virtual Environment (Recommended)

Creating a virtual environment isolates your project dependencies and prevents conflicts with other Python projects.

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows (Command Prompt):
```bash
python -m venv venv
venv\Scripts\activate
```

#### On Windows (PowerShell):
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Note:** After activation, your terminal prompt should show `(venv)` at the beginning.

---

### 3. Install Dependencies

With your virtual environment activated, install all required packages:

```bash
pip install -r requirements.txt
```

This command installs:
- **Flask** - Web framework for building the application
- **Pytest** - Testing framework for running automated tests
- **CS50 SQL Library** - Simplified SQLite interface

You can verify the installations with:
```bash
pip list
```

---

### 4. Verify the Database

The application uses a SQLite database file (`questions.db`) to store quiz questions. Ensure this file exists in the project root directory.

```bash
# List files in the current directory
ls -la  # macOS/Linux
dir     # Windows
```

You should see `questions.db` in the directory listing.

---

## ▶️ Running the Application

### 1. Start the Flask Development Server

```bash
python app.py
```

You should see output similar to:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: off
```

### 2. Access the Application

Open your web browser and navigate to:
```
http://127.0.0.1:5000/
```

or

```
http://localhost:5000/
```

The quiz application should now be running!

---

## 🧪 Running Tests

The project includes automated tests using Pytest. To run all tests:

```bash
pytest
```

For more verbose output with details about each test:
```bash
pytest -v
```

To run tests with coverage information:
```bash
pytest --cov=.
```

Expected test output:
```
collected X items
test_app.py::test_index PASSED
test_app.py::test_submit PASSED
...
```

---

## 📂 Project Structure

```
Dynamic-Quiz-Application-mit-Flask-SQLite-und-Automated-Testing/
├── app.py                    # Main Flask application and routes
├── questions.db              # SQLite database with quiz questions
├── requirements.txt          # Python package dependencies
├── test_app.py               # Pytest test suite
├── README.md                 # Project overview and features
├── INSTALLATION_GUIDE.md     # This file
└── templates/                # HTML templates (Jinja2)
    ├── index.html            # Home/category selection page
    ├── quiz.html             # Quiz questions page
    └── results.html          # Results and score display page
```

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### Issue: `ModuleNotFoundError: No module named 'flask'`
**Solution:** Ensure your virtual environment is activated and run `pip install -r requirements.txt` again.

#### Issue: `No such file or directory: 'questions.db'`
**Solution:** Verify the database file exists in the project root. If missing, contact the repository maintainer or check the database setup instructions.

#### Issue: `Port 5000 already in use`
**Solution:** Either:
- Stop the application using that port, or
- Run Flask on a different port:
  ```bash
  python -m flask run --port 5001
  ```

#### Issue: `ModuleNotFoundError: No module named 'cs50'`
**Solution:** The CS50 library should be included in `requirements.txt`. Try reinstalling:
  ```bash
  pip install --upgrade pip
  pip install cs50
  ```

#### Issue: Tests fail with database errors
**Solution:** Ensure the `questions.db` file exists and is properly formatted. Check that the database is not corrupted.

---

## 🛑 Stopping the Application

To stop the Flask development server, press **Ctrl+C** (or **Cmd+C** on macOS) in your terminal.

To deactivate the virtual environment:
```bash
deactivate
```

---

## 📋 Requirements Summary

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | Latest | Web framework |
| Pytest | Latest | Testing framework |
| CS50 | Latest | SQLite database interface |
| Python | 3.7+ | Runtime |
| SQLite3 | Bundled | Database engine |

---

## 📖 Next Steps

1. **Explore the Application:** Navigate through the quiz categories and try taking a quiz.
2. **Review the Code:** Check `app.py` to understand the routing and database queries.
3. **Run Tests:** Execute `pytest -v` to see all test cases.
4. **Modify & Extend:** Customize the templates in the `templates/` folder or add new features.

---

## ❓ Need Help?

- Check the main [README.md](./README.md) for project details
- Review the code comments in `app.py` and `test_app.py`
- Visit the [Flask Documentation](https://flask.palletsprojects.com/)
- Check [Pytest Documentation](https://docs.pytest.org/)

---

## 📝 License

Refer to the repository's LICENSE file (if applicable) for licensing information.

---

**Happy Learning & Testing! 🎉**
