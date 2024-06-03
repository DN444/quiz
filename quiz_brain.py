class QuizBrain:
    def __init__(self,q_list):
        self.q_num=0
        self.q_list=q_list
        self.score=0
    def still_has_q(self):
        return self.q_num<len(self.q_list)
    def next_q(self):
        current_q=self.q_list[self.q_num]
        self.q_num+=1
        user_ans=input(f"Q.{self.q_num}: {current_q.text} (True/False): ")
        self.check_ans(user_ans,current_q.answer)
    def check_ans(self,user_ans,correct_ans):
        if user_ans.lower()==correct_ans.lower():
            self.score+=1
            print("Right answer!")
        else:
            print("Wrong.")
            print(f"The correct answer was: {correct_ans}")
        print(f"Your current score is: {self.score}/{self.q_num}")
        print("\n")