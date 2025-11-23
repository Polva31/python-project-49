#!/usr/bin/env python3
import random


def is_prime(number):
    """Check if number is prime"""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def play_prime_game():
    print('Welcome to the Brain Prime Game!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    
    correct_answers = 0
    rounds = 3
    
    for _ in range(rounds):
        number = random.randint(1, 100)
        correct_answer = "yes" if is_prime(number) else "no"
        
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
    play_prime_game()

if __name__ == "__main__":
    main()
