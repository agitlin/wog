import random
from secret import API_KEY
import freecurrencyapi as fca
import utils

def get_description():
    return "3. Currency Roulette - try and guess the value of a random amount in USD converted to ILS."


def get_money_interval(difficulty, amount):
    exchange_rate = get_exchange_rate()
    converted_value = amount * exchange_rate
    acceptable_range = 10 - difficulty
    lower_bound = converted_value - acceptable_range
    upper_bound = converted_value + acceptable_range
    return (lower_bound, upper_bound , converted_value)


def get_valid_client():
    client=fca.Client(API_KEY)
    if not client:
        utils.print_info("Invalid API key. Please check your key and try again.")
        exit()
    remaining_quota = client.status()['quotas']['month']['remaining']
    if remaining_quota == 0:
        utils.print_info("You have reached your monthly quota. Please try again next month.")
        exit()
    return client


def get_exchange_rate():
    client = get_valid_client()
    result=client.latest(currencies=["USD","ILS"])
    return result["data"]["ILS"]


def get_guess_from_user():
    return int(input("Enter your guess for the converted value in ILS: "))


def compare_results(difficulty, amount):
    lower_bound, upper_bound , exact = get_money_interval(difficulty, amount)
    guess = get_guess_from_user()
    utils.print_info(f"Exact conversion: {exact}")
    return lower_bound <= guess <= upper_bound
    

def play(difficulty):
    print("Welcome to the Currency Roulette Game!")
    print("Let's convert from USD to ILS.")
    print("The acceptable range depends on the game's difficulty level.")
    print("Let's get started! ")
    amount = random.randint(1, 100)
    print(" The amount to convert is: ", amount)
    result= compare_results(difficulty, amount)
    utils.print_result("Currency Roulette", result)
    return result
