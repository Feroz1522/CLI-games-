from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
for i in question_data['results']:
    q = i['question']
    a = i['correct_answer']
    question_bank.append(Question(q, a))


user = QuizBrain(question_bank)
while user.still_has_questions():
    user.next_quesiton()
print("\nYou have completed the quiz.")
print(f"well your final score is {user.score}/{user.question_number}")
