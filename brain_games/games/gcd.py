#!/usr/bin/env python3
import random


def find_gcd(a, b):
    """Find Greatest Common Divisor using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a


def generate_round():
    """Generate a round for GCD game."""
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    
    question = f"{num1} {num2}"
    correct_answer = str(find_gcd(num1, num2))
    
    return question, correct_answer
