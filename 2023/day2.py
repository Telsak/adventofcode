'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ day2.py ]   █
 █   [ Type ................................. Advent of Code 2023 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 05, 2023 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

import time
import sys
from functools import reduce

def get_data(ns=0):
    day_file = sys.argv[0].split('.')[0]
    with open (f'.//input//{day_file}_input{ns * "_small"}', 'r') as file:
        filedata = [line.strip() for line in file.readlines()]
    return filedata
    
def match_set(bag, line):
    cubes = {'red': 0, 'green': 0, 'blue': 0}
    newbag = bag.copy()
    line = line.split(',')
    for cube in line:
        n, c = cube.strip().split()
        cubes[c] += int(n)
    for k, v in newbag.items():
        if cubes[k] > newbag[k]:
            # more cubes than exist
            return False
    # if no errors, the set was a success
    return True

def minimum_cubes(line):
    cubes = {'red': 0, 'green': 0, 'blue': 0}
    sets = line.split(';')
    for cube in sets:
        for cube in cube.split(','):
            n, c = cube.strip().split()
            if int(n) > cubes[c]:
                cubes[c] = int(n)
    n_cubes = [v for k, v in cubes.items() if v > 0]
    return reduce(lambda a, b: a * b, n_cubes)

def match(bag, line):
    for game_set in line.split(';'):
        if match_set(bag, game_set) == False:
            return False
    return True

def part_one(lines: list) -> int:
    # bags of cubes
    print('part one')
    rgb = {'red': 12, 'green': 13, 'blue': 14}
    list_id = 0
    for record in lines:
        record = record.split(':')
        id = int(record[0].split()[1])
        list_id += (match(rgb, record[1]) * id)
    return list_id

def part_two(lines):
    # do stuff again
    print('part two')
    sum_power = 0
    for record in lines:
        record = record.split(':')[1]
        sum_power += minimum_cubes(record)
    return sum_power

start = time.time()

data = get_data()
output = part_two(data)
#output = part_one(data)

stop = time.time()

print(f'Körning tog: {stop - start:.4f} sekunder\n{output}')

