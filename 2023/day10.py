'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day10.py ]   █
 █   [ Type ................................. Advent of Code 2023 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 15, 2023 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''
import numpy as np
import time
import sys
from collections import deque

def get_data(ns=0):
    day_file = sys.argv[0].split('.')[0]
    with open (f'.//input//{day_file}_input{ns * "_small"}', 'r') as file:
        filedata = []
        for line in file.readlines():
            line = line.translate(str.maketrans(p_trans[0], p_trans[1]))
            filedata.append(line.strip())
    return filedata

def display_maze(grid, path):
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if (r, c) in path:
                color = '\x1b[1;32;40m'
            else:
                color = '\x1b[1;30;40m'
            print(color + col + '\x1b[0m', end='')
        print()

def part_one(indata):
    # do stuff
    maze = np.array([[col for col in row] for row in indata])
    maze = np.pad(maze, pad_width=1, mode='constant', constant_values='.')
    visited = np.zeros(np.shape(maze))
    start_coords = np.where(maze == 'S')
    x, y = int(start_coords[0]), int(start_coords[1])
    nodes = deque()
    nodes.append((y, x, 0))
    path = {}
    path[nodes[0][:2]] = None
    moves = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
    
    while len(nodes) > 0:
        # travel both directions
        node = nodes.popleft()
        y, x, dist = node
        # if adjacent nodes in 
        if len(nodes) > 0 and (y, x) == (nodes[0][0], nodes[0][1]):
            return dist
        else:
            visited[y, x] = 1
            for move in moves.keys():
                dy, dx = y + moves[move][0], x + moves[move][1]
                if maze[dy, dx] in neighbors[maze[y, x]][move]:
                    if visited[dy, dx] == 0:
                        visited[dy, dx] = 1
                        nodes.append((dy, dx, dist+1))
                        if (dy, dx) not in path:
                            path[(dy, dx)] = node[:2]
                    else:
                        continue
    display_maze(maze, path)
    return dist, maze, path

def part_two(indata):
    # do stuff again
    count = 0
    _, maze, loop = part_one(indata)
    for r, row in enumerate(maze):
        for c, col in enumerate(row):
            if (r, c)  not in loop:
                maze[r, c] = '.'
    display_maze(maze, loop)
    return count, maze, loop

p_trans = ['|-LJ7F', '║═╚╝╗╔']

neighbors = {
        '║': {'U': '╗║╔S', 'R': '', 'D': '╚╝║S', 'L': ''},
        '═': {'U': '', 'R': '╗╝═S', 'D': '', 'L': '╔╚═S'},
        '╚': {'U': '╗╔║S', 'R': '╗═╝S', 'D': '', 'L': ''},
        '╝': {'U': '╗╔║S', 'R': '', 'D': '', 'L': '╔═╚S'},
        '╗': {'U': '', 'R': '', 'D': '╚╝║S', 'L': '╔═╚S'},
        '╔': {'U': '', 'R': '╗═╝S', 'D': '╚╝║S', 'L': ''},
        'S': {'U': '╗║╔', 'R': '╗╝═', 'D': '╚╝║', 'L': '╔═╚'}}

full_or_not = '--full' not in sys.argv
data = get_data(full_or_not)

# part one or two? part one is default
if '-p2' in sys.argv:
    print('== Running part two ==')
    start = time.time()
    output = part_two(data)[0]
else:
    print('== Running part one (use -p2 for part two) ==')
    start = time.time()
    output = part_one(data)[0]

stop = time.time()

print(f'Körning tog: {stop - start:.4f} sekunder\n{output}')

