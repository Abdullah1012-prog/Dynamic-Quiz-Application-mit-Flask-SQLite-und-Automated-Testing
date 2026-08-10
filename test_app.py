import pytest
from app import app, db

@pytest.fixture
def client():
    # Configure Flask app for testing mode
    app.config["TESTING"] = True

    # Create a test client browser link
    with app.test_client() as client:
        yield client

# Test 1: Check if the homepage loads correctly
def test_homepage_load(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Select a question type:" in response.data

# Test 2: Check if picking a type loads the quiz page with options
def test_quiz_generation(client):
    # Simulate selecting the computer quiz option
    response = client.post("/", data={"questionType": "computer"})
    assert response.status_code == 200
    # Make sure form elements and options exist on the target quiz page
    assert b"Submit Quiz" in response.data or b"Submit Answers" in response.data

# Test 3: Check database question retrieval logic
def test_database_query():
    # Direct database test to verify 20 items pull down safely
    questions = db.execute(
        "SELECT * FROM questions WHERE questionType = ? LIMIT 20",
        "computer"
    )
    assert len(questions) == 20
    assert "question" in questions[0]
    assert "correct_answer" in questions[0]
