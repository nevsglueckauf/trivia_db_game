# Main python script running app 
# AUTHOR: Sven Schrodt<sven.schrodt@schrodt.club
# SINCE: 2025-05-16
from trivia import Trivia
from entity import Question
from mock import Mock
import app 
#from app import App

t = Trivia()
m = Mock()
game = app.App()
#foo = app.Runner()
#print(str(True),str(False))
#exit(5363)
#data = t.get_questions_raw(1)

#print(data['results'][0])
data = m.get_question_multiple()
#data= m.get_question_bool()
#exit(666)
#print(t.response_code)
q1 = Question(data)
q1.answer(100)
game.runner.render(q1)
#print(q1.correct_answer)
#print(type(q1.correct_answer), type(q1.given_answer))
#print(q1.correct_answer == q1.given_answer)

q1.solve()
print(q1.result)

# print(q1.dta['answers'])
#print(type(q1.dta['incorrect_answers']), q1.dta['incorrect_answers'])
