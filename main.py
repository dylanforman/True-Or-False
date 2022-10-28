from data import question_data
import question_model
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question['text']
    answer = question['answer']
    question = question_model.Question(text, answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}.")
