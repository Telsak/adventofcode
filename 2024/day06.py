'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day06.py ]   █
 █   [ Type ................................. Advent of Code 2024 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 06, 2024 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

import time
import sys
from collections import defaultdict as dd

def get_data(ns=0):
  day_file = sys.argv[0].split('.')[0]
  with open (f'.//input//{day_file}_input{ns * "_small"}', 'r') as file:
    filedata = [line.strip() for line in file.readlines()]
  return filedata
    
def print_grid(array, visits):
  for i in range(len(array)):
    for j in range(len(array[0])):
      if [i, j] in visits:
        print('X', end='')
      elif array[i][j] == '^':
        print('.', end='')
      else:
        print(array[i][j], end='')
    print()
  print()

def part_one(indata):
  # do stuff
  hmap = dd(int)
  height = len(indata)
  width = len(indata[0])
  directions = [[-1,0],[0,1],[1,0],[0,-1]]
  for y in range(height):
    for x in range(width):
      if indata[y][x] == '^':
        # set the starting pos
        pos = [y, x]
        di = 0

  visits = [pos]
  hmap[f'{y}.{x}'] = 1
  while (0 <= pos[0] < width) and (0 <= pos[1] < height):
    my, mx = pos[0] + directions[di][0], pos[1] + directions[di][1]
    if 0 <= my <= height and 0 <= mx <= width:
      try:
        indata[my][mx]
      except:
        pos = [my, mx]
        visits.append(pos)
        break
      if indata[my][mx] == '#':
        di = (di + 1) % 4
      else:
        pos = [my, mx]
        visits.append(pos)
        hmap[f'{my}.{mx}'] = 1
        # print_grid(indata, visits)
    else:
      break
  return len(hmap)

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

