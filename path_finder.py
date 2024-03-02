# importing modules
import curses
from curses import wrapper
import queue
import time
# Define the maze and set the 'passed' flag to False
passed = False
maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["O", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

# Function to print the maze with optional path highlighting


def print_maze(maze, stdscr, path=[]):
    # Initialize color pairs for blue and red
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    # Iterate through the maze and print each cell
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            # Highlight the path cells in red
            if (i, j) in path:
                stdscr.addstr(i, j*2, 'X', RED)
            else:
                stdscr.addstr(i, j*2, value, BLUE)
    stdscr.refresh()

# Recursive function to navigate through the maze


def go(i, j, stdscr):
    global maze
    global passed
    try:
        o1 = maze[i+1][j]
        if o1 == 'X':
            passed = True
        if o1 == ' ' and not passed:
            maze[i+1][j] = 'O'
            print_maze(stdscr)
            time.sleep(0.1)
            go(i+1, j, stdscr)
    except:
        pass
    try:
        o2 = maze[i-1][j]
        if o2 == 'X':
            passed = True
        if o2 == ' ' and not passed:
            maze[i-1][j] = 'O'
            print_maze(stdscr)
            time.sleep(0.1)
            go(i-1, j, stdscr)
    except:
        pass
    try:
        o3 = maze[i][j+1]
        if o3 == 'X':
            passed = True
        if o3 == ' ' and not passed:
            maze[i][j+1] = 'O'
            print_maze(stdscr)
            time.sleep(0.1)
            go(i, j+1, stdscr)
    except:
        pass
    try:
        o4 = maze[i][j-1]
        if o4 == 'X':
            passed = True
        if o4 == ' ' and not passed:
            maze[i][j-1] = 'O'
            print_maze(stdscr)
            time.sleep(0.1)
            go(i, j-1, stdscr)
    except:
        pass

# Find the starting position in the maze


def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None

# Find the path from 'O' to 'X' using breadth-first search


def find_path(maze, stdscr):
    start = 'O'
    end = 'X'
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))
    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos
        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()
        if maze[row][col] == end:
            return path
        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            r, c = neighbor
            if maze[r][c] == '#':
                continue
            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)
    # If no path is found, print a message and return None
    print("Finding path has failed.")
    return None

# Find neighboring cells of a given cell


def find_neighbors(maze, row, col):
    neighbors = []
    if row > 0:  # Up
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):  # Down
        neighbors.append((row + 1, col))
    if col > 0:  # Left
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):  # Right
        neighbors.append((row, col + 1))

    return neighbors

# Main function to initialize curses and start the program


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    # go(2, 0, stdscr)

    if find_path(maze, stdscr) is not None:
        stdscr.addstr(len(maze), 0, "Path found to the X.")
    else:
        stdscr.addstr(len(maze), 0, "There is no path to the X.")
    stdscr.getch()


# Run the program using curses wrapper
wrapper(main)
