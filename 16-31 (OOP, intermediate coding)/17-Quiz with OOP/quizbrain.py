class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.questions_list = list
        self.score = 0
    def is_next(self):
        return True if self.question_number < len(self.questions_list) else False
    def next_question(self):
       self.check_answer(input(f"Q.{self.question_number + 1}: {self.questions_list[self.question_number]}. (True/False) \n"))
       self.question_number += 1
    def check_answer(self, answer):
        if answer == self.questions_list[self.question_number].answer:
            print("Correct!")
            self.score += 1
        else :
            print("you suck!")
