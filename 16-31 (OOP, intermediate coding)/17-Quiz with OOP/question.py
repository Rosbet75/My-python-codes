class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def __str__(self):
        return self.question + " " + self.answer


new_q = Question("asdfasdf", "False")
print(new_q)