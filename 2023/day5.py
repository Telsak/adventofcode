'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ day5.py ]   █
 █   [ Type ................................. Advent of Code 2022 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 12, 2023 ]             █
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

def generate_map(destination, source, r_len):
    local_map = {}
    for i in range(source, source + r_len):
        local_map[i] = destination + i
    return local_map
    
def part_one(indata):
    # do stuff
    maps = {}
    locations = []
    for line in indata:
        if 'seeds:' in line:
            source = 'seeds'
            maps[source] = [int(n) for n in line.split(':')[1].split()]
        elif 'map:' in line:
            destination = line.split('-')[-1].split()[0]
        elif len(line) > 0 and line[0].isdigit():
            dest, src, r_len = [int(n) for n in line.split()]
            if destination in maps:
                maps[destination].update(generate_map(dest, src, r_len))
            else:
                maps[destination] = generate_map(dest, src, r_len)
    return maps

def part_two(indata):
    # do stuff again
    return

full_or_not = '--full' not in sys.argv
data = get_data(full_or_not)

# part one or two? part one is default
if '-p2' not in sys.argv:
    print('== Running part one (use -p2 for part two) ==')
    start = time.time()
    output = part_one(data)
else:
    print('== Running part two ==')
    start = time.time()
    output = part_two(data)

stop = time.time()

print(f'Körning tog: {stop - start:.4f} sekunder\n{output}')

