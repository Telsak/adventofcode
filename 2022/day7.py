'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  RELEASE INFO  ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ day7.py ]   █
 █   [ Type ................................. Advent of Code 2022 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 08, 2022 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''
from collections import defaultdict as dd

def dir_struct(output):
    level = -1
    path = []
    dirsizes = dd(int)
    for line in output:
        if line.startswith('$ cd'):
            dir = line.split()[-1]
            if dir == '..':
                path.pop()
                level -= 1
            else:
                path.append(dir)
                level += 1
#                print(f'{level*"  "}- {dir} (dir)')
        elif line.startswith('$ ls'):
            continue
        else:
            size, _ = line.split()
            if size.isdigit():
                size = int(size)
#                print(f'{(level+1)*"  "}- {_} (file), size={size}')
                for i in range(len(path)):
                    dirsizes['/'.join(path[:i+1])] += size
    return dirsizes

def get_sizes(dirsizes):
    maxsize = 100000
    total = 0
    for key, value in dirsizes.items():
        if value <= maxsize:
            total += value
    return total

def del_dir(dirsizes):
    TOTAL = 70000000
    REQUIRED = 30000000
    used_space = dirsizes['/']
    free_space = TOTAL - used_space
    space_needed = REQUIRED - free_space
    el_dirs = []
    for key, value in dirsizes.items():
        if value > space_needed:
            el_dirs.append(value)
    return min(el_dirs)
    

def part_one(data):
    # do stuff
    stuff = dir_struct(data)
    print(get_sizes(stuff))
    return

def part_two(data):
    # do stuff again
    stuff = dir_struct(data)
    print(del_dir(stuff))
    return

with open (r'./input/day7_input', 'r') as file:
    filedata = [line.strip() for line in file.readlines()]

part_one(filedata)
part_two(filedata)


