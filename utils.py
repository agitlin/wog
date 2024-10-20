from rich.console import Console

SCORES_FILE_NAME = "scores.txt"
console =Console()

def screen_cleaner():
    console.clear()

def print_info( message):
    console.print(message, style="bold blue")

def print_result(game_name, result):
    style = "bold green" if result else "bold red"
    message = f"{game_name} - {'You Won' if result else 'You Lost'}"
    console.print(message, style=style)
