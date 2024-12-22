from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a bank of questions
questions_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    questions_bank.append(new_question)

# Start the quiz
quiz = QuizBrain(questions_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{len(questions_bank)}")
