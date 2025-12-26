class Question:
    """Model class for a single quiz question."""
    def __init__(self, question: str, answer: str):
        """
                Initialize a new question.

                Args:
                    question (str): The text of the question.
                    answer (str): The correct answer ('True' or 'False').
                """
        self.question = question
        self.answer = answer
