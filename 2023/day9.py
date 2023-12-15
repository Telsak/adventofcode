'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ day9.py ]   █
 █   [ Type ................................. Advent of Code 2023 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 15, 2023 ]             █
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

def expand_history(h):
    # create the next line, the diff of the initial history values
    # and do this for every subsequent line
    return [h[i+1]-h[i] for i in range(len(h)-1)]

def predict_history(h):
    for i in range(len(h)-1, -1, -1):
        if i > 0:
            h[i-1][-1] = h[i][-1] + h[i-1][-2]
    return h

    
def display_grid(h):
    h = predict_history(h)
    print(250 * '=')
    for line in h:
        print(f"{''.join(str(value).center(10) for value in line): ^250}")
    print('==== value out:', h[0][-1], '====================')
    return h[0][-1]


def part_one(indata):
    # do stuff
    histories = []
    sum_values = 0
    for line in indata:
        history = [[int(x) for x in line.split()]]
        while not all(value == 0 for value in history[-1]):
            history.append(expand_history(history[-1]))
        histories.append(history)

    for history in histories:
        for line in history:
            line.append(0)

    for history in histories:
        sum_values += display_grid(history)
    

    return sum_values

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

