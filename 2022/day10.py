'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  RELEASE INFO  ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day10.py ]   █
 █   [ Type ................................. Advent of Code 2022 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 19, 2022 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

import time
 
def get_data(ns=0): 
    with open (f'.//input//day10_input{ns * "_small"}', 'r') as file:
        filedata = [line.strip() for line in file.readlines()]
    return filedata 
    
def signal_strength(cycle, start, stop, step):
    return sum([cycle[x] * x for x in range(start, len(cycle)+1, step)])

def part_one(data):
    x, c = 1, 1
    cycle = [x]
    for row in data:
        if 'noop' in row:
            cycle += [x]
            c+=1
        else:
            v = row.split()[1]
            for i in range(2):
                cycle += [x]
                c+=1
            x += int(v)
    
    return signal_strength(cycle, 20, 221, 40)

def draw_crt(row):
    for i, val in enumerate(row):
        if val in [i-1, i, i+1]:
            print('#', end='')
        else:
            print('.', end='')
    print()

def part_two(data):
    # do stuff again
    x, c = 1, 1
    cycle = [x]
    for row in data:
        if 'noop' in row:
            cycle += [x]
            c+=1
        else:
            v = row.split()[1]
            for i in range(2):
                cycle += [x]
                c+=1
            x += int(v)
    for i in range(1, len(cycle), 40):
        draw_crt(cycle[i:i+40])
    return
    

start = time.time()

data = get_data(False)
#output = part_one(data)
output = part_two(data)

stop = time.time()

print(f'Körning tog: {stop - start:.4f} sekunder\n{output}')

