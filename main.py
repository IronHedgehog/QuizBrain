from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def create_question_bank(data):
    """
       Convert a list of dictionaries into a list of Question objects.

       Args:
           data (List[Dict[str, str]]): List of dictionaries with keys 'text' and 'answer'.

       Returns:
           List[Question]: List of Question objects.
       """
    return [Question(item["text"], item["answer"]) for item in data]


question_bank = create_question_bank(question_data)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    question, correct_answer = quiz.next_question()
    user_answer = input(f"{question} (True/False): ")

    if quiz.check_answer(user_answer, correct_answer):
        print("Correct!")
    else:
        print(f"Wrong! Correct answer: {correct_answer}")

    score, total = quiz.get_score()
    print(f"Score: {score}/{total}\n")

final_score, total_questions = quiz.get_score()
print(f"Final result: {final_score}/{total_questions}")
