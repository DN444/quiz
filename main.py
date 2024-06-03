from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
q_bank=[]
for i in question_data:
    txt=i["text"]
    ans=i["answer"]
    new_q=Question(txt,ans)
    q_bank.append(new_q)
quiz=QuizBrain(q_bank)
while quiz.still_has_q():
    quiz.next_q()
print("You have completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.q_num}")