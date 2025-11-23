#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.calc import generate_round

def main():
    description = 'What is the result of the expression?'
    run_game(generate_round, description)

if __name__ == "__main__":
    main()
