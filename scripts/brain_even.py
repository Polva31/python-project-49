#!/usr/bin/env python3
import random


def is_even(number):
    """Check if number is even"""
    return number % 2 == 0


def play_even_game():
    print("Welcome to the Brain Even Game!")
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    
    correct_answers = 0
    rounds = 3
    
    for _ in range(rounds):
        number = random.randint(1, 100)
        correct_answer = "yes" if is_even(number) else "no"
        
        print(f"Question: {number}")
        user_answer = input("Your answer: ").lower()
        
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    
    if correct_answers == rounds:
        print(f"Congratulations, {name}!")


def main():
    play_even_game()

if __name__ == "__main__":
    main()
