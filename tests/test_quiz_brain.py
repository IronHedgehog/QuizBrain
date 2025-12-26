from quiz_brain import QuizBrain
from question_model import Question


def test_check_answer_correct():
    q = Question("Test question?", "True")
    quiz = QuizBrain([q])

    result = quiz.check_answer("true", "True")
    assert result is True
    assert quiz.score == 1


def test_check_answer_incorrect():
    q = Question("Test question?", "True")
    quiz = QuizBrain([q])

    result = quiz.check_answer("false", "True")
    assert result is False
    assert quiz.score == 0
