'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ day6.py ]   █
 █   [ Type ................................. Advent of Code 2023 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 13, 2023 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''
import numpy as np
import math
import time
import sys

def get_data(ns=0):
    day_file = sys.argv[0].split('.')[0]
    with open (f'.//input//{day_file}_input{ns * "_small"}', 'r') as file:
        filedata = [line.strip() for line in file.readlines()]
    return filedata
    
def find_roots(race):
    # avoid checking every single possible ms variation, this can be solved
    # with a formula: (T-n)*n = D
    # this will give us the upper and lower bounds of how long you can
    # hold the button to still get a winning score
    race_time = int(race[0])
    race_distance = int(race[1])

    roots = sorted(np.roots([1, -race_time, race_distance]))
    roots[0] = math.floor(roots[0])
    roots[1] = math.ceil(roots[1])
    return roots[1] - roots[0] - 1

def part_one(indata):
    # do stuff
    product = 1
    for line in indata:
        if 'Time:' in line:
            times = line.split(':')[1].split()
        elif 'Distance:' in line:
            distances = line.split(':')[1].split()
    races = zip(times, distances)
    found_roots = [find_roots(race) for race in races]
    for ways_to_win in found_roots:
        product *= ways_to_win
    return product

def part_two(indata):
    # do stuff again
    product = 1
    for line in indata:
        if 'Time:' in line:
            times = [line.split(':')[1].replace(' ','')]
        elif 'Distance:' in line:
            distances = [line.split(':')[1].replace(' ','')]
    races = zip(times, distances)
    found_roots = [find_roots(race) for race in races]
    for ways_to_win in found_roots:
        product *= ways_to_win
    return product

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

