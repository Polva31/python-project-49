#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.gcd import generate_round


def main():
    description = 'Find the greatest common divisor of given numbers.'
    run_game(generate_round, description)


if __name__ == '__main__':
    main()
