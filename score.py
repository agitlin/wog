
def get_score():
    try:
        with open('scores.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return 0
def add_score(difficulty):
    current_score = int(get_score())

    current_score += difficulty*3 + 5

    with open('scores.txt', 'w') as file:
        file.write(str(current_score))
    return current_score