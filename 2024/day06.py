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
from aoc_utils import get_data_f
import copy

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

def get_guard_xy(indata):
  for y in range(len(indata)):
    for x in range(len(indata[0])):
      if indata[y][x] == '^':
        # set the starting pos
        ry = y
        rx = x
  return ry, rx

def part_one(indata):
  # do stuff
  hmap = dd(int)
  y, x = get_guard_xy(indata)
  print(y, x)
  di = 0
  pos = [y, x]
  visits = [pos]
  hmap[f'{pos[0]}.{pos[1]}'] = 1
  while (0 <= pos[0] < height) and (0 <= pos[1] < width):
    dy, dx = dirs[di]
    my, mx = pos[0] + dy, pos[1] + dx
    if 0 <= my < height and 0 <= mx < width:
      if indata[my][mx] == '#':
        di = (di + 1) % 4
      else:
        pos = [my, mx]
        visits.append(pos)
        hmap[f'{my}.{mx}'] = 1
        #print_grid(indata, visits)
    else:
      break
  return len(hmap)

def part_two(indata):
  # keep track of visited locations, ugly array but only generated once
  vgrid = []
  for row in range(height):
    vgrid.append([])
    for col in range(width):
      vgrid[row].append(False)

  y, x = get_guard_xy(indata)
  vgrid[y][x] = True

  di = 0
  pos = [y, x]

  # make a copy of the area for temporary loop checker
  indata_clone = copy.deepcopy(indata)
  obstructions = 0

  while True:
    dy, dx = dirs[di]
    if (0 <= pos[0] + dy < height) and (0 <= pos[1] + dx < width):
      my, mx = pos[0] + dy, pos[1] + dx
      if indata[my][mx] == '#':
        # smooth direction modifier
        di = (di + 1) % 4
        continue
      elif vgrid[my][mx] == False:
        # mark the location as visited, the temporarily mark the cloned
        # area with a wall, and then remove after loop checker
        vgrid[my][mx] = True
        indata_clone[my][mx] = '#'
        obstructions += check_loop(indata_clone, dy, dx, pos[0], pos[1], di)
        indata_clone[my][mx] = '.'
      pos[0] += dy
      pos[1] += dx
    else:
      break
  return obstructions

def check_loop(_indata_clone, _dy, _dx, _py, _px, _di):
  '''reuse variable names, but prefix with _ to signify local'''
  _vgrid = {}
  while True:

    # track current position and direction, and acknowledge loop if
    # we see any repeats (+1 to obstructions)
    if _vgrid.get((_py, _px)) is None:
      _vgrid[(_py, _px)] = [_di]
    elif _di not in _vgrid[(_py, _px)]:
      _vgrid[(_py, _px)].append(_di)
    else:
      return True
    
    _my, _mx = _py + _dy, _px + _dx
    if (0 <= _py + _dy < height) and (0 <= _px + _dx < width):
      if _indata_clone[_my][_mx] == '#':
        _di = (_di + 1) % 4
        _dy, _dx = dirs[_di][0], dirs[_di][1]
        continue
    else:
      return False
    _py += _dy
    _px += _dx

full_or_not = '--full' not in sys.argv
data = get_data_f(full_or_not, 'grid')
height, width = len(data), len(data[0])
dirs = [[-1,0],[0,1],[1,0],[0,-1]]

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

