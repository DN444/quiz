class Question:
    def __init__(self,tex,ans):
        self.text=tex
        self.answer=ans
    def __str__(self):
        return f"Q: {self.text}\nA: {self.answer}"