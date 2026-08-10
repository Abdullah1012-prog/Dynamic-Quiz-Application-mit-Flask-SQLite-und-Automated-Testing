from flask import Flask, render_template, request
from cs50 import SQL

app = Flask(__name__)
db = SQL("sqlite:///questions.db")


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        question_type = request.form.get("questionType")

        # Explicitly select 'rowid' along with all other columns (*)
        questions = db.execute(
            "SELECT * FROM questions WHERE questionType = ? ORDER BY RANDOM() LIMIT 20", question_type)
        return render_template("quiz.html", questions=questions)


@app.route("/submit", methods=["POST"])
def submit():
    score = 0
    results = []

    # Loop 20 times (once for each question slot)
    for i in range(1, 21):
        # Extract the question text and user's choice using our loops numbers
        question_text = request.form.get(f"question_text_{i}")
        user_answer = request.form.get(f"answer_{i}")

        if question_text and user_answer:
            # Look up the correct answer matching this specific question text string
            db_row = db.execute(
                "SELECT correct_answer FROM questions WHERE question = ?", question_text)

            if db_row:
                correct_answer = db_row[0]["correct_answer"]
                is_correct = (user_answer == correct_answer)

                if is_correct:
                    score += 1

                results.append({
                    "question": question_text,
                    "user_ans": user_answer,
                    "correct_ans": correct_answer,
                    "is_correct": is_correct
                })

    return render_template("results.html", score=score, total=20, results=results)
