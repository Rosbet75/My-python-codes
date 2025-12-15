from question import Question
from data import question_data
from quizbrain import QuizBrain
question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

brain = QuizBrain(question_bank)

while brain.is_next():
    brain.next_question()

print(f"Your final score is: {brain.score}/{len(brain.questions_list)}")
if brain.score > 5:
    print("You win!")
else:
    print("You absoutely suck at this")