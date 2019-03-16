import sys

maze_file = sys.argv[-1]

def get_maze(f):
    maze = []
    file = open(f, "r")
    a = file.readline().strip()
    while a != "":
        a = list(a)
        maze.append(a)
        a = file.readline().strip()
    return maze


def is_dead_end(maze, x, y):
    if maze[y][x + 1] == "*" and maze[y-1][x] == "*" and maze[y][x - 1] == "*":
        return True
    elif maze[y - 1][x] == "*" and maze[y][x-1] == "*" and \
            maze[y + 1][x] == "*":
        return True
    elif maze[y][x - 1] == "*" and maze[y + 1][x] == "*" and \
            maze[y][x + 1] == "*":
        return True
    elif maze[y + 1][x] == "*" and maze[y][x + 1] == "*" and \
            maze[y - 1][x] == "*":
        return True
    else:
        return False


def fill_maze(maze):
    for y in range(1, len(maze)-1):
            for x in range(1, len(maze[y])-1):
                if is_dead_end(maze, x, y):
                    maze[y][x] = '*'
    return maze


def turn_back_maze(maze):
    o_maze = ""
    for line in maze:
        a = "".join(line)
        o_maze += a + "\n"
    return o_maze


def finalize_maze(maze):
    a = 0
    while a < 10000:
        fill_maze(maze)
        a += 1
    return maze


print(fill_maze(get_maze(maze_file)))
