def welcome(username="Nobody"):
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey")


def welcome():
    username = input("Enter your username: ")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey")

def validate_numeric_value_in_range(value, min, max):
    if value.isdigit():
        if int(value) >= min and int(value) <= max:
            return True
    return False

def get_input(message, min, max):
    while True:
        value = input(f'{message} [{min}-{max}]: ')
        if validate_numeric_value_in_range(value, min, max):
            return value
        else:
            print(f"Invalid input. Please enter a number between {min} and {max}")

def start_play():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.")
    print("2. Guess Game - guess a number and see if you chose like the computer.")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    game_choice = get_input("Enter the number of the game you want to play " , 1, 3)
    
    difficulty_level = get_input("Enter the difficulty level", 1, 5)
    
    print(f"game choice: {game_choice}, difficulty level: {difficulty_level}")
