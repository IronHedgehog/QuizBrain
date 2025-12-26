QuizBrain – Python Quiz Game 🎮🐍

QuizBrain is a small Python True/False quiz game that demonstrates:
Basic OOP (classes, methods, type hints)
Quiz logic and score tracking
Unit tests with pytest and CI/CD via GitHub Actions

🚀 How to Run the Game
python main.py

Example session:
Q1: Is Python fun? (True/False?) True
Correct! ✅
Q2: The Earth is flat? (True/False?) False
Correct! ✅
Your final score: 2/3

🧪 How to Run Tests
pytest -v

Tests cover all QuizBrain methods: next_question(), check_answer(), still_has_questions(), get_score().

CI automatically runs tests on every push or pull request.

📂 Project Structure
Quiz-Game/
│
├─ main.py                # Main quiz runner
├─ quiz_brain.py          # QuizBrain class
├─ question_model.py      # Question class
├─ data.py                # Question data
├─ tests/
│   └─ test_quiz_brain.py # Unit tests
└─ README.md              # This file
