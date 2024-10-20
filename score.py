def add_score(difficulty):
    try:
        with open('scores.txt', 'r') as file:
            current_score = int(file.read())
    except FileNotFoundError:
        current_score = 0

    current_score += difficulty*3 + 5

    with open('scores.txt', 'w') as file:
        file.write(str(current_score))
    return current_score