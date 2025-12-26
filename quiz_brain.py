class QuizBrain:
    """Class that manages the quiz logic."""
    def __init__(self, questions: list):
        """
               Initialize the quiz.

               Args:
                   questions (list[Question]): List of Question objects.
               """
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def still_has_questions(self) -> bool:
        """
               Check if there are still questions left in the quiz.

               Returns:
                   bool: True if there are questions left, False otherwise.
               """
        return self.question_number < len(self.question_list)

    def next_question(self) -> tuple[str, str]:
        """
               Show the current question to the user and get their answer via input.
               After the answer, check it with check_answer.
               """
        current = self.question_list[self.question_number]
        self.question_number += 1
        return current.question, current.answer

    def check_answer(self, user_answer: str, correct_answer: str) -> bool:
        """
                Check the user's answer.

                Args:
                    user_answer (str): Answer provided by the user.
                    correct_answer (str): Correct answer.

                Returns:
                    bool: True if the answer is correct, False otherwise.
                """
        is_correct = user_answer.strip().lower() == correct_answer.lower()
        if is_correct:
            self.score += 1
        return is_correct

    def get_score(self) -> tuple[int, int]:
        """
               Return the final score of the user.

               Returns:
                   str: Final score as a string.
               """
        return self.score, self.question_number
