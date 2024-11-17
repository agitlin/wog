import random
import time
import utils

def get_description():
    return "2. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back."
    
def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(difficulty)]

def get_list_from_user(difficulty):
    return [int(input("Enter a number: ")) for _ in range(difficulty)]

def is_list_equal(list1, list2):
    return list1 == list2

def play(difficulty):
    sequence = generate_sequence(difficulty)
    utils.print_info(f"Memorize the sequence: {sequence}")
    time.sleep(1)
    utils.screen_cleaner()
    utils.print_info("And now recreate the sequence:")
    user_list = get_list_from_user(difficulty)
    utils.print_info ( f"The original sequence was: {sequence}")
    result=  is_list_equal(sequence, user_list)
    utils.print_info(f"Your sequence: {user_list}")
    utils.print_result("Memory Game", result)
    return result
