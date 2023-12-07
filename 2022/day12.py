'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day12.py ]   █
 █   [ Type ................................. Advent of Code 2022 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 20, 2022 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''
import time, os
from collections import deque

def get_data(ns=0):
    with open (f'.//input//day12_input{ns * "_small"}', 'r') as file:
        filedata = [line.strip() for line in file.readlines()]
    return filedata

def get_start(values, part):
    start = {1: 'S', 2: 'E'}

    for ri, row in enumerate(values):
        for ci, col in enumerate(row):
            if values[ri][ci] == start[part]:
                return (ri, ci), (len(values), len(values[0]))

def solve(data, start, rc, part):
    # create a visited array matching the search area, init to False
    visited = [[False] * len(data[0]) for _ in range(len(data))]
    nodes = deque()
    # node syntax: y, x, distance from start
    nodes.append((start[0], start[1], 0))
    directions = [(0,1), (-1,0), (0,-1), (1, 0)]
    path = {}
    path[nodes[0][:2]] = None
    print(path)
    
    while len(nodes) > 0:
        # find neighbor nodes to this cell unless we are at exit
        node = nodes.popleft()
        y, x, dist = node[0], node[1], node[2]

        visited[y][x] = True
        win = {1: 'E', 2: 'a'}
        if data[y][x] == win[part]:
            print(win[part])
            print(f'Exit found at: {y, x}')
            parent = (y, x)
            cleanpath = []
            cleanpath.append(path[parent])
            while path[parent] != None:
                parent = path[parent]
                if path[parent] == None:
                    continue
                else:
                    cleanpath.append(path[parent])
            return dist, cleanpath
        
        if data[y][x] == 'S':
            here = 'a'
        elif data[y][x] == 'E':
            here = 'z'
        else:
            here = data[y][x]
        for dir in directions:
            dy, dx = y + dir[0], x + dir[1]
            if 0 <= dy <= rc[0]-1 and 0 <= dx <= rc[1]-1:
                # valid cell to examine
                if data[dy][dx] == 'S':
                    there = 'a'
                elif data[dy][dx] == 'E':
                    there = 'z'
                else:
                    there = data[dy][dx]
                if part == 1:
                    if visited[dy][dx] == False and ord(there) - ord(here) < 2:
                        visited[dy][dx] = True
                        nodes.append((dy, dx, node[2]+1))
                        ninfo = (dy, dx)
                        if ninfo not in path:
                            path[ninfo] = node[:2]
                    else:
                        continue
                else:
                    if visited[dy][dx] == False and (ord(here) < ord(there) or 0 <= ord(here) - ord(there) <= 1):
                        visited[dy][dx] = True
                        nodes.append((dy, dx, node[2]+1))
                        ninfo = (dy, dx)
                        if ninfo not in path:
                            path[ninfo] = node[:2]
                    else:
                        continue
            else:
                continue
        #print(nodes)
        #print_maze(data, (y, x), dist)
        #print('--------------------------------\n')
        #input()

def print_maze(data, coord, distance, draw=False, path=''):
    os.system('clear')
    info = f'[Step: {distance+1}]'
    l = '═'
    print(f'╔══{info}{l*(len(data[0])-len(info)-4)}══╗')
    for ri, row in enumerate(data):
        print('║', end='')
        for ci, col in enumerate(row):
            chr = '\033[31m#\033[0m' if (ri, ci) == coord else col
            if draw:
                if (ri, ci) in path[:distance]:
                    chr = '\033[31m#\033[0m'
            print(chr, end='')
        print('║')
    print(f'╚{l*(len(data[0]))}╝')

def part_one(data):
    # do stuff
    start, rc = get_start(data, 1)
    distance, path = solve(data, start, rc, 1)
    path.reverse()
    print_maze(data, (-1,-1), 0, False)
    print('\033[s', end='')
    for i, step in enumerate(path):
        print(f'\033[0;4H[Step: {i}]')
        print(f'\033[31m\033[{step[0]+2};{step[1]+2}H#\033[0m')
        time.sleep(0.05)
    print('\033[u', end='')
    return distance

def part_two(data):
    # do stuff again
    start, rc = get_start(data, 2)
    distance, path = solve(data, start, rc, 2)
    path.reverse()
    print_maze(data, (-1,-1), 0, False)
    print('\033[s', end='')
    for i, step in enumerate(path):
        print(f'\033[0;4H[Step: {i}]')
        print(f'\033[31m\033[{step[0]+2};{step[1]+2}H#\033[0m')
        time.sleep(0.01)
    print('\033[u', end='')
    return distance

start = time.time()

data = get_data()
output = part_one(data)
#output = part_two(data)

stop = time.time()

print(f'Körning tog: {stop - start:.4f} sekunder\n{output}')

