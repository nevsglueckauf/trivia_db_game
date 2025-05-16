# Main python script running app 
# AUTHOR: Sven Schrodt<sven.schrodt@schrodt.club
# SINCE: 2025-05-16
from trivia import Trivia
from entity import Question
from mock import Mock
t = Trivia()
m = Mock()

mylist = ["apple", "banana", "cherry", 'ajkjsd']


print(mylist) 

exit(3)
#data = t.get_questions_raw(1)

#print(data['results'][0])
data = m.get_question_multiple()
print(data)

#exit(666)
#print(t.response_code)
q1 = Question(data)
print(q1.dta['answers'])
#print(type(q1.dta['incorrect_answers']), q1.dta['incorrect_answers'])
