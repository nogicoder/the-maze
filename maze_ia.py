#!/usr/bin/env python3
# import sys module for communication protocol
import sys
# import functions from function.py file
from function import get_map, get_graph, IA_deployment, \
                     BFS, get_IA_position, get_enemy_list

# read the first output
maze_input = sys.stdin.readline()
# set condition of the loop in order not to freeze the computer
while maze_input != "":
    if "HELLO" in maze_input:
        sys.stdout.write("I AM an IA\n\n")  # reply to the program
    elif "YOU ARE" in maze_input:
        sys.stdout.write("OK\n\n")
        IA_badge = maze_input[len("YOU ARE ")]  # get the symbol for each IA
    elif "MAZE" in maze_input:
        # get the map from the output
        map = get_map()
        # get the start position of IA
        start = get_IA_position(map, IA_badge)
        # get the symbol of other IAs
        enemy_list = get_enemy_list(map, IA_badge)
        # turn maze into graph
        graph = get_graph(map, enemy_list)
        # make move based on the path returned by the algorithm
        IA_deployment(BFS(map, enemy_list, graph, start), graph, start)
    # read the subsequent output of the program to continue the loop
    maze_input = sys.stdin.readline()
