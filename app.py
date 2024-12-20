
from simple_term_menu import TerminalMenu
import games.memory_game as memory_game
import games.guess_game as guess_game
import games.currency_roulette_game as currency_roulette_game
import utils
import score
import time


def welcome(username="Nobody"):
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey")


def welcome():
    username = input("Enter your username: ")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey")


def start_play():
    print("Please choose a game to play. Use arrows to choose and Enter to confirm:")
    options = [ guess_game.get_description(), memory_game.get_description(), currency_roulette_game.get_description()]
    terminal_menu = TerminalMenu(options)
    game_choice = terminal_menu.show()
    print("Enter the difficulty level. Use arrows to choose and Enter to confirm:")
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
    time.sleep(2)
    utils.screen_cleaner()
    if result:
        updated_score = score.add_score(int(difficulty_level))
        utils.print_info(f"Your score is : {updated_score}")
    