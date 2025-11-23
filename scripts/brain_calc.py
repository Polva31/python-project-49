#!/usr/bin/env python3
import random


def calculate(num1, num2, operation):
    """Perform calculation based on operation"""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    else:
        return None


def play_calc_game():
    print("Welcome to the Brain Calc Game!")
    print("What is the result of the expression?")
    
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    
    correct_answers = 0
    rounds = 3
    operations = ['+', '-', '*']
    
    for _ in range(rounds):
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        operation = random.choice(operations)
        correct_answer = calculate(num1, num2, operation)
        
        print(f"Question: {num1} {operation} {num2}")
        user_answer = input("Your answer: ")
        
        try:
            if int(user_answer) == correct_answer:
                print("Correct!")
                correct_answers += 1
            else:
                print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
                print(f"Let's try again, {name}!")
                break
        except ValueError:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    
    if correct_answers == rounds:
        print(f"Congratulations, {name}!")


def main():
    play_calc_game()

if __name__ == "__main__":
    main()
