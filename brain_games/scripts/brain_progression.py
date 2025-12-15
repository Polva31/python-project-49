#!/usr/bin/env python3
from brain_games.engine import run
from brain_games.games.progression import generate_round

def main():
    description = "What number is missing in the progression?"
    run(generate_round, description)

if __name__ == "__main__":
    main()
