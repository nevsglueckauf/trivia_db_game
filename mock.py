class Mock:
    
    def __init__(self):
        pass
    
    def get_question_bool(self):
        return {'type': 'boolean', 'difficulty': 'medium', 'category': 'History', 'question': 'Ottoman Empire was created in 1299.', 'correct_answer': 'True', 'incorrect_answers': ['False']}
    
    def get_question_multiple(self):
        return {'type': 'multiple', 'difficulty': 'medium', 'category': 'Entertainment: Video Games', 'question': 'What is the lowest amount of max health you can have in Team Fortress 2?', 'correct_answer': '70', 'incorrect_answers': ['100', '50', '95']}