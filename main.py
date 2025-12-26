from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def create_question_bank(data):
    questions = []
    for item in data:
        questions.append(Question(item['text'], item['answer']))
    return questions


question_bank = create_question_bank(question_data)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.do_question()

score, total = quiz.get_score()
print(f"Your final score: {score}/{total}")
