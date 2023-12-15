'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ day8.py ]   █
 █   [ Type ................................. Advent of Code 2023 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 14, 2023 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

import time
import sys

def get_data(ns=0):
    day_file = sys.argv[0].split('.')[0]
    with open (f'.//input//{day_file}_input{ns * "_small"}', 'r') as file:
        filedata = [line.strip() for line in file.readlines()]
    return filedata

def traverse_map(moves, move_map):
    steps = 0
    sl = len(moves)
    position = 'AAA'
    while position != 'ZZZ':
        dir = moves[steps % sl]
        print(f'({position}) - Step {steps} moving {dir} to {move_map[position][dir]}')
        position = move_map[position][dir]
        steps += 1
    return steps

def part_one(indata):
    # do stuff
    move_map = {}
    for line in indata:
        if len(line) > 0 and '=' not in line:
            instructions = line
        elif '=' in line:
            destination, move = line.split(' = ')
            move = move.strip('()').split(', ')
            move_map[destination] = {'L': move[0], 'R': move[1]}
    return traverse_map(instructions, move_map)

def part_two(indata):
    # do stuff again
    return

full_or_not = '--full' not in sys.argv
data = get_data(full_or_not)

# part one or two? part one is default
if '-p2' in sys.argv:
    print('== Running part two ==')
    start = time.time()
    output = part_two(data)
else:
    print('== Running part one (use -p2 for part two) ==')
    start = time.time()
    output = part_one(data)

stop = time.time()

print(f'Körning tog: {stop - start:.4f} sekunder\n{output}')

