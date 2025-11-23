import random


def generate_progression(length, start, step):
    """Генерирует арифметическую прогрессию"""
    return [start + i * step for i in range(length)]


def play_progression_game():
    print("Welcome to the Brain Progression Game!")
    print("What number is missing in the progression?")
    
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    
    correct_answers = 0
    rounds = 3
    
    for _ in range(rounds):
        # Генерируем случайные параметры прогрессии
        length = random.randint(5, 10)  # Длина от 5 до 10 чисел
        start = random.randint(1, 20)
        step = random.randint(1, 10)
        hidden_index = random.randint(0, length - 1)  # Случайная позиция для скрытия
        
        progression = generate_progression(length, start, step)
        
        # Сохраняем правильный ответ
        correct_answer = progression[hidden_index]
        
        # Создаем прогрессию с точкой вместо скрытого числа
        progression_with_gap = progression.copy()
        progression_with_gap[hidden_index] = ".."
        
        # Формируем строку вопроса
        question_str = " ".join(map(str, progression_with_gap))
        print(f"Question: {question_str}")
        
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


if __name__ == "__main__":
    play_progression_game()

def main():
    play_progression_game()
