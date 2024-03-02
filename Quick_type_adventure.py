# Import necessary modules
import curses
from curses import wrapper
import time
import random

# Function to display the start screen


def start_screen(stdscr):
    """Display the start screen with instructions."""
    stdscr.clear()
    stdscr.addstr('Welcome to the Speed Typing Test!')
    stdscr.addstr('\nPress any key to begin!')
    stdscr.refresh()
    stdscr.getkey()

# Function to display the target text and user input


def display_text(stdscr, target, current, wpm):
    """Display the target text and user input on the screen."""
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f'WPM: {wpm}')
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)

# Function to load a random text from a file


def load_text():
    """Load a random text from a file."""
    with open('text.txt', 'r') as f:
        lines = f.readlines()
        return random.choice(lines).strip()

# Function to conduct the speed typing test


def wpm_test(stdscr):
    """Conduct the speed typing test."""
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    # Main loop for the typing test
    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        # Check if the user has completed the target text
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        # Handle user input including backspace
        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

# Main function to initialize curses and run the program


def main(stdscr):
    """Main function to run the speed typing test."""
    # Initialize color pairs
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    # Display the start screen and conduct the typing test
    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(
            2, 0, 'You completed the text! Press any key to continue(press \"Esc\" to exit).')
        key = stdscr.getkey()

        # Check if the user wants to exit the program
        if ord(key) == 27:
            break


# Run the program using curses wrapper
wrapper(main)
