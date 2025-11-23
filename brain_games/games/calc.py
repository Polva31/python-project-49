#!/usr/bin/env python3
import random
import operator

def calculate_expression(num1, num2, operation):
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    return operations[operation](num1, num2)

def generate_round():
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    operation = random.choice(['+', '-', '*'])
    
    question = f"{num1} {operation} {num2}"
    correct_answer = str(calculate_expression(num1, num2, operation))
    
    return question, correct_answer
