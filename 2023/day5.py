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
        filedata.append('')
    return filedata

def translate_values(data, mappings, destination):
    # 50 98 2 (destination, source, range)
    # 52 50 48
    # in: 79 -> out: 81
    # in: 98 -> out: 50

    output = []
    #print(f'=={destination}====================')
    for number in data:
        #print(f'number:{number}')
        found_number = False
        for mapping in mappings:
            dst, src, r = [int(n) for n in mapping]
            if src <= number < src + r:
                new_number = dst + (number - src)
                output.append(new_number)
                #print(f'new:{new_number}')
                found_number = True
                break
        if not found_number:
            #print(f'new:{number}')
            output.append(number)
    return output
    
def part_one(indata):
    # do stuff
    dest_mappings = []
    for line in indata:
        if 'seeds:' in line:
            # grab the initial seeds
            values = [[int(n) for n in line.split(':')[1].split()]]
        elif 'map:' in line:
            # new transforms .. unnecessary?
            destination = line.split('-')[-1].split()[0]
            dest_mappings = []
        elif len(line) > 0 and line[0].isdigit():
            # keep adding to the transform list
            dest, src, r_len = [int(n) for n in line.split()]
            dest_mappings.append([dest, src, r_len])
        else:
            # do actual work before next set of transforms
            if len(dest_mappings) > 0:
                values.append(translate_values(values[-1], dest_mappings, destination))
    return min(values[-1])

def part_two(indata):
    # do stuff again
    maps = {}
    dest_mappings = []
    for line in indata:
        if 'seeds:' in line:
            # grab the initial seeds - changed, in pairs now with
            # (start, range) behavior
            raw_values = [int(n) for n in line.split(':')[1].split()]
            values = [[raw_values[i], raw_values[i+1]] for i in range(0, len(raw_values), 2)]
        elif 'map:' in line:
            # new transforms .. unnecessary?
            destination = line.split('-')[-1].split()[0]
            dest_mappings = []
        elif len(line) > 0 and line[0].isdigit():
            # keep adding to the transform list
            dest, src, r_len = [int(n) for n in line.split()]
            dest_mappings.append([dest, src, r_len])
        else:
            # do actual work before next set of transforms
            if len(dest_mappings) > 0:
                values = []
                maps[destination] = dest_mappings
                input(maps[destination])


    for item in maps.items():
        input(item)


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

