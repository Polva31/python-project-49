#!/usr/bin/env python3
from brain_games.engine import run
from brain_games.games.prime import generate_round

def main():
    description = "Answer yes if given number is prime. Otherwise answer no."
    run(generate_round, description)

if __name__ == "__main__":
    main()
