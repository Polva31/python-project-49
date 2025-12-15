#!/usr/bin/env python3
from brain_games.engine import run
from brain_games.games.calc import generate_round

def main():
    description = 'What is the result of the expression?'
    run(generate_round, description)

if __name__ == "__main__":
    main()
