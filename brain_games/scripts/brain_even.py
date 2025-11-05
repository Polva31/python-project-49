#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.even import generate_round

def main():
    description = "Answer yes if number even, else answer no"
    run_game(generate_round, description)

if __name__ == "__main__":
    main()
