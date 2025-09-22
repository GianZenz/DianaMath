# Database models are defined in the main app.py file
# This file exists for import compatibility
from app import User, Progress, Achievement

# Additional exercise model for future use
class Exercise:
    def __init__(self, question, options, correct_answer, explanation=None):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.explanation = explanation