#!/usr/bin/env python3
import random

def generate_round():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    length = 10
    progression = [start + step * i for i in range(length)]
    
    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    
    progression[hidden_index] = '..'
    question = ' '.join(str(x) for x in progression)
    
    return question, correct_answer
