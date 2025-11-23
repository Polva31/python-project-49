#!/usr/bin/env python3
import math
import random


def find_gcd(a, b):
    """Find the greatest common divisor of two numbers"""
    return math.gcd(a, b)


def play_gcd_game():
    print("Welcome to the Brain GCD Game!")
    print("Find the greatest common divisor of given numbers.")
    
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    
    correct_answers = 0
    rounds = 3
    
    for _ in range(rounds):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        correct_answer = find_gcd(num1, num2)
        
        print(f"Question: {num1} {num2}")
        user_answer = input("Your answer: ")
        
        try:
            if int(user_answer) == correct_answer:
                print("Correct!")
                correct_answers += 1
            else:
                print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
                break
        except ValueError:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            break
    
    if correct_answers == rounds:
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")


def main():
    play_gcd_game()

if __name__ == "__main__":
    main()
