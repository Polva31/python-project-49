#!/usr/bin/env python3
import random

def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

def generate_round():
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    question = str(number)
    return question, correct_answer
