# Classes representing entities for Trivia DB Game
# AUTHOR: Sven Schrodt<sven.schrodt@schrodt.club
# SINCE: 2025-05-16
#
# Question - representing single trivia game question
import random
from typing import Any, Self,  Dict, List, Optional, Sequence, Tuple, Union

class Question:
    
    # valid indices (keys in this case)
    __idc = ['type', 'difficulty', 'category', 'question', 'correct_answer', 'incorrect_answers']
    dta: dict
    given_answer:str
    result:bool
    
    def __init__(self, dta:dict):
        self.dta = dta
        self.dta['answers'] = self.dta['incorrect_answers']
        self.dta['answers'].append(self.dta['correct_answer'])
        random.shuffle(self.dta['answers']) # get questions in a ranomized order
        
    def answer(self, answer:str) -> Self:
        answer = self.__sanitize_answer(answer)
        if answer not in self.dta['answers']:
             raise ValueError(f'Value {answer} is not a possible answer!')
        self.given_answer = answer
        return self
    
    def solve(self):
        self.result = (self.correct_answer == self.given_answer)    
        
    def __getattr__(self, key):
        self.__sanitize_key(key)
        
        return self.dta[key]
        
         
    
    def __sanitize_key(self, key:str):
        if key not in self.__idc:
            raise IndexError(f'Key {key} does not exist')
        
    def __sanitize_answer(self, input):
        return str(input)
        
        