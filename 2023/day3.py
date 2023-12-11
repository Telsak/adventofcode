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

def get_box_data(x, y, length, schematic, gear=0):
    # returns True if there is a valid symbol in a box around the number
    data = ''
    data += schematic[y-1][x-1:x+length+1]
    data += schematic[y][x-1:x+length+1]
    data += schematic[y+1][x-1:x+length+1]
    new_data = [_ for _ in data if not _.isdigit() and _ != '.']
    if gear:
        if '*' in data:
            pos = data.find('*')
            x = pos % (length+2) + x
            y = pos // (length+2) + y
            return True, (x, y)
        else:
            return False, (0, 0)
    else:
        return len(new_data) > 0

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

def part_two(schematic):
    # do stuff again
    ratios_sum = 0
    gears = {}
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
                    near_gear, coords = get_box_data(sx, sy, len(number), schematic, 1)
                    if near_gear:
                        if coords in gears:
                            gears[coords] += [number]
                        else:
                            gears[coords] = [number]
                    number = ''
    for coord, parts in gears.items():
        if len(parts) == 2:
            ratios_sum += (int(parts[0]) * int(parts[1]))

    return ratios_sum

start = time.time()

data = get_data()
#output = part_one(data)
output = part_two(data)

stop = time.time()

print(f'Körning tog: {stop - start:.4f} sekunder\n{output}')

