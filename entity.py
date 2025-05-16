# Classes representing entities for Trivia DB Game
# AUTHOR: Sven Schrodt<sven.schrodt@schrodt.club
# SINCE: 2025-05-16
#
# Question - representing single trivia game question
import random

class Question:
    # valid indices (keys in this case)
    idc = ['type', 'difficulty', 'category', 'question', 'correct_answer', 'incorrect_answers']
    dta: dict
    
    
    def __init__(self, dta:dict):
        self.dta = dta
        self.dta['answers'] = self.dta['incorrect_answers']
        self.dta['answers'].append(self.dta['correct_answer'])
        random.shuffle(self.dta['answers'])
        
        