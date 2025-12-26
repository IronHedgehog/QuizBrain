class QuizBrain:
    def __init__(self, questions: list):
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def do_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1} {current_question.question}, (True/False?)")
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer: str, correct_answer: str):
        if user_answer.strip().lower() == correct_answer.strip().lower():
            print("Correct!")
            self.score += 1
        else:
            print(f"WRONG ANSWER! ({user_answer})")
        print(f"correct answer: {correct_answer}")
        print(f"Your current score: {self.score}/{self.question_number}")
        print("\n")

    def get_score(self):
        return self.score, self.question_number
