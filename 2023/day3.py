'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ day3.py ]   █
 █   [ Type ................................. Advent of Code 2023 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 07, 2023 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

import time
import sys

def get_data(ns=0):
    day_file = sys.argv[0].split('.')[0]
    with open (f'.//input//{day_file}_input{ns * "_small"}', 'r') as file:
        filedata = ['.' + line.strip() + '.' for line in file.readlines()]
    filedata.insert(0, '.' * len(filedata[1]))
    filedata.append('.' * len(filedata[1]))
    return filedata

def get_box_data(x, y, length, schematic):
    # returns True if there is a valid symbol in a box around the number
    data = ''
    data += schematic[y-1][x-1:x+length+1]
    data += schematic[y][x-1:x+length+1]
    data += schematic[y+1][x-1:x+length+1]
    newdata = [x for x in data if not x.isdigit() and x != '.']
    return len(newdata) > 0

def part_one(schematic):
    # do stuff
    parts_sum = 0
    sx, sy = 0, 0
    number = ''

    for y, line in enumerate(schematic):
        for x, pos in enumerate(line):
            if pos.isdigit():
                if number == '':
                    sy = y
                    sx = x
                number += pos
            else:
                if number != '':
                    parts_sum += get_box_data(sx, sy, len(number), schematic) * int(number)
                    number = ''
    return parts_sum

def part_two():
    # do stuff again
    return

start = time.time()

data = get_data()
output = part_one(data)

stop = time.time()

print(f'Körning tog: {stop - start:.4f} sekunder\n{output}')

