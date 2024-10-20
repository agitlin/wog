
from simple_term_menu import TerminalMenu
import memory_game
import guess_game
import currency_roulette_game
import utils


def welcome(username="Nobody"):
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey")


def welcome():
    username = input("Enter your username: ")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey")


def get_input(message, min, max):
    while True:
        value = input(f'{message} [{min}-{max}]: ')
        if validate_numeric_value_in_range(value, min, max):
            return value
        else:
            print(f"Invalid input. Please enter a number between {min} and {max}")

def start_play():
    print("Please choose a game to play:")
    options = [ guess_game.get_description(), memory_game.get_description(), currency_roulette_game.get_description()]
    terminal_menu = TerminalMenu(options)
    game_choice = terminal_menu.show()
    print("Enter the difficulty level")
    options = ["1", "2", "3", "4", "5"]
    terminal_menu = TerminalMenu(options)
    difficulty_level = terminal_menu.show()+1
    
    print(f"game choice: {game_choice}, difficulty level: {difficulty_level}")
    if game_choice == 0:
        result = guess_game.play(int(difficulty_level))
    elif game_choice == 1:
        result = memory_game.play(int(difficulty_level))
    elif game_choice == 2:
        result = currency_roulette_game.play(int(difficulty_level))
    utils.screen_cleaner()
    score= result* int(difficulty_level)
    utils.print_info(f"Thank you for playing. Your score is: {score}")
    