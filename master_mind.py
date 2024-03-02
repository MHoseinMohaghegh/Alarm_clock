# import random module
import random
# List of possible colors for the code
COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']

# Number of attempts allowed and length of the secret code
TRIES = 10
CODE_LENGTH = 4

# Function to generate a random secret code


def generate_code():
    """Generate a random secret code."""
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    return code

# Function to get user input for a code guess


def guess_code():
    """Get user input for a code guess."""
    while True:
        guess = input("Guess: ").upper().split(" ")
        if len(guess) != CODE_LENGTH:
            print(f'You must guess {CODE_LENGTH} colors.')
            continue
        for color in guess:
            if color not in COLORS:
                print(f'Invalid color: {color}. Try again.')
                break
        else:
            break
    return guess

# Function to check the guessed code against the real code


def check_code(guess, real_code):
    """Check the guessed code against the real code."""
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    # Count occurrences of each color in the real code
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    # Check for correct positions and update color counts
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    # Check for incorrect positions and update color counts
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

# Main game function


def game():
    """Mastermind game logic."""
    print(f'''Welcome to mastermind, you have {TRIES} tries to guess the code.
The valid colors are''', *COLORS)

    # Generate a secret code
    code = generate_code()

    # Allow the player to make guesses within the specified number of tries
    for attempt in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        # Check if the player has guessed the code correctly
        if correct_pos == CODE_LENGTH:
            print(f'You guessed the code in {attempt} tries!')
            break

        # Provide feedback on the current guess
        print(f'Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}')

    else:
        print('You ran out of tries, the code was:', *code)


# Execute the game when the script is run
if __name__ == '__main__':
    game()
