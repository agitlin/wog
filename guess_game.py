import random
import utils

def get_description():
    return "1. Guess Game - guess a number and see if you are right."


def generate_number(difficulty):
    return random.randint(0, difficulty)


def get_guess_from_user(difficulty):
    return int(input(f"Enter a number between 0 and {difficulty}: "))   


def compare_results(secret_number, guess):
    return secret_number == guess
    

def play(difficulty):
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    result = compare_results(secret_number, guess)
    utils.print_result("Guess Game", result)
    return result