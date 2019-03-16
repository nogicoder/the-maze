# import sys module for protocol and collections module for the queue
import sys
import collections


# get the map from the maze's output
def get_map():
    import sys
    map = []
    while True:
        map_line = sys.stdin.readline().strip()
        if map_line != "":
            map.append(map_line)
        else:
            break
    return map


# get the list of symbol of other IAs
def get_enemy_list(map, IA_badge):
    enemy_list = []
    for row in range(1, len(map) - 1):
        for col in range(1, len(map[row]) - 1):
            if map[row][col] not in ("#", " ", "map", "\n", "o", "!",
               IA_badge):
                enemy_list.append(map[row][col])
    return enemy_list


"""turn map into a dictionary with keys are the current node and
values are adjacent nodes that fulfill conditions
"""


def get_graph(map, enemy_list):
    graph = {(col, row): [] for row in range(1, len(map)) for col in
             range(1, len(map[row])) if map[row][col] != "#"}
    for col, row in graph.keys():
        if map[row][col + 1] != "#" and map[row][col + 1] not in enemy_list:
            graph[(col, row)].append(("MOVE RIGHT\n", (col + 1, row)))
        if map[row][col - 1] != "#" and map[row][col - 1] not in enemy_list:
            graph[(col, row)].append(("MOVE LEFT\n", (col - 1, row)))
        if map[row + 1][col] != "#" and map[row + 1][col] not in enemy_list:
            graph[(col, row)].append(("MOVE DOWN\n", (col, row + 1)))
        if map[row - 1][col] != "#" and map[row - 1][col] not in enemy_list:
            graph[(col, row)].append(("MOVE UP\n", (col, row - 1)))
    return graph


# get the co-ordination of the IA
def get_IA_position(map, IA_badge):
    for row in range(1, len(map) - 1):
        for col in range(1, len(map[row]) - 1):
            if map[row][col] == IA_badge:
                return (col, row)


# Return path to the resource through Breadth-First Search Algorithm
def BFS(map, enemy_list, graph, start):
    queue = collections.deque([("", start)])
    visited = set()
    while queue:
        path, current_node = queue.popleft()
        col = current_node[0]
        row = current_node[1]
        if map[row][col] == "!":
            return path
        elif map[row][col] == "o":
            return path
        if current_node in visited:
            continue
        visited.add(current_node)
        for direction, adjacent_node in graph[current_node]:
            queue.append((path + direction, adjacent_node))


"""get possible move when all paths to the resource is blocked by other IAs
(when BFS() return None)
"""


def get_possible_move(graph, start):
    path = ""
    for direction, adjacent_node in graph[start]:
        path += direction
    return path


# send move to the maze based on the path returned from the BFS algorithm
def IA_deployment(path, graph, start):
    if path is not None:
        move = path.split("\n")
        sys.stdout.write(move[0] + "\n\n")
    elif path is None:
        random_path = get_random_move(graph, start)
        move = random_path.split("\n")
        sys.stdout.write(move[0] + "\n\n")
