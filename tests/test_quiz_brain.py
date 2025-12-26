import pytest
from quiz_brain import QuizBrain
from question_model import Question

# ----------------------------
# Fixtures for reusable quiz objects
# ----------------------------
@pytest.fixture
def single_question_quiz():
    """
    Fixture providing a QuizBrain instance with a single question.
    """
    q = Question("Is Python fun?", "True")
    quiz = QuizBrain([q])
    return quiz, q

@pytest.fixture
def two_questions_quiz():
    """
    Fixture providing a QuizBrain instance with two questions.
    """
    q1 = Question("Q1?", "True")
    q2 = Question("Q2?", "False")
    quiz = QuizBrain([q1, q2])
    return quiz, [q1, q2]

# ----------------------------
# Tests for check_answer method
# ----------------------------
def test_check_answer_correct(single_question_quiz):
    """
    Test that check_answer returns True for a correct answer
    and increments the quiz score.
    """
    quiz, q = single_question_quiz
    result = quiz.check_answer("true", q.answer)
    assert result is True
    score, _ = quiz.get_score()
    assert score == 1

def test_check_answer_incorrect(single_question_quiz):
    """
    Test that check_answer returns False for an incorrect answer
    and does not increment the quiz score.
    """
    quiz, q = single_question_quiz
    result = quiz.check_answer("false", q.answer)
    assert result is False
    score, _ = quiz.get_score()
    assert score == 0

# ----------------------------
# Tests for still_has_questions method
# ----------------------------
def test_still_has_questions(two_questions_quiz):
    """
    Test that still_has_questions returns True when there are remaining questions
    and False when all questions have been answered.
    """
    quiz, questions = two_questions_quiz
    assert quiz.still_has_questions() is True

    # Take first question
    quiz.next_question()
    assert quiz.still_has_questions() is True

    # Take second question
    quiz.next_question()
    assert quiz.still_has_questions() is False

# ----------------------------
# Test next_question method
# ----------------------------
def test_next_question(single_question_quiz):
    """
    Test that next_question returns the correct question and answer tuple.
    """
    quiz, q = single_question_quiz
    question_text, correct_answer = quiz.next_question()
    assert question_text == q.question
    assert correct_answer == q.answer

# ----------------------------
# Test get_score method after multiple answers
# ----------------------------
def test_multiple_answers():
    """
    Test a quiz with multiple questions, including correct and incorrect answers,
    verifying both score and total number of questions answered.
    """
    q1 = Question("Q1?", "True")
    q2 = Question("Q2?", "False")
    q3 = Question("Q3?", "True")
    quiz = QuizBrain([q1, q2, q3])

    # Simulate answers
    quiz.check_answer("true", q1.answer)  # correct
    quiz.check_answer("true", q2.answer)  # incorrect
    quiz.check_answer("true", q3.answer)  # correct

    score, total = quiz.get_score()
    assert score == 2
    assert total == 3
