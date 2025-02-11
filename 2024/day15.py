'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day15.py ]   █
 █   [ Type ................................. Advent of Code 2024 puzzle ]   █
 █                                                                           █
 █   Day #: Warehouse Woes                                                   █
 █   https://adventofcode.com/2024/day/15                                    █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date .................... Feb 6, 2025 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

import time
import sys
from aoc_utils import get_data_f, colors
import re
import os, time

def print_grid(_grid, robot):
  # basic output of the play area
  BLUE = colors[3]
  RED = colors[-2]
  YELLOW = colors[-3]
  RESET = colors[-1]
  #time.sleep(0.03)
  #os.system('clear')
  cmap = {'#': BLUE, 'O': RED, '@': YELLOW}
  for y, row in enumerate(_grid):
    for x, col in enumerate(row):
      val = col.get_value()
      ry, rx = robot.get_pos()
      if ry == y and rx == x:
        val = '@'
      if val in cmap:
        val = f'{cmap[val]}{val}{RESET}'
      print(val, end='')
    print()
  return

def part_one(indata):
  # do stuff
  dirs = ''.join(re.findall(r'[\^\<\>v]', indata))
  grid = ''.join(re.findall(r'[#.O@\n]', indata)).rstrip().split('\n') 
  grid = [[col for col in row] for row in grid]

  w = len(grid[0])
  h = len(grid)
  for y in range(h):
    for x in range(w):
      if grid[y][x] == '@':
        robot = pushing_robot(y, x)
        r = y,x
        pval = '.'
      else:
        pval = grid[y][x]
      grid[y][x] = grid_object(x, y, pval, w, h)
  grid[r[0]][r[1]].set_value('.')

  for move in dirs:
    robot.move(move, grid)
    _y, _x = robot.get_pos()
    #print_grid(grid, robot)

  gps_total = 0
  for y in range(h):
    for x in range(w):
      gps_total += grid[y][x].report_gps()
    
  return gps_total

def part_two(indata):
  # do stuff again
  return

class grid_object:
  def __init__(self, x=0, y=0, value='', grid_w=0, grid_h=0):
    self._value = value
    self._neighbor_up = (y-1,x) if y-1 >= 0 else None
    self._neighbor_right = (y,x+1) if x+1 < grid_w else None
    self._neighbor_down = (y+1,x) if y+1 < grid_h else None
    self._neighbor_left = (y,x-1) if x-1 >= 0 else None
    self._x = x
    self._y = y

  def report_gps(self):
    return int(self.get_value() == 'O') * ((100 * self._y) + self._x)

  def can_move(self, dir, grid):
    dirs = {'^':  self._neighbor_up,
            '>':  self._neighbor_right,
            'v':  self._neighbor_down,
            '<':  self._neighbor_left
           }
    if dirs[dir] is not None:
      ny = dirs[dir][0]
      nx = dirs[dir][1]
      if grid[ny][nx].get_value() == '#':
        return False
      elif grid[ny][nx].get_value() == '.':
        grid[ny][nx].set_value('O')
        return True
      else:
        return grid[ny][nx].can_move(dir, grid)
    else:
      return False

  def set_value(self, value):
    self._value = value

  def get_value(self):
    return self._value

class pushing_robot:
  def __init__(self, y=0, x=0):
    self._y = y
    self._x = x
    self._value = '@'

  def move(self, dir, grid):
    dirs = {'^':  (-1,0),
            '>':  (0,1),
            'v':  (1,0),
            '<':  (0,-1)
           }
    my = self._y + dirs[dir][0]
    mx = self._x + dirs[dir][1]
    #print(f'Attempting move {dir} from {self._y, self._x} to {my, mx}')
    #print(grid[my][mx].get_value())
    target_pos = grid[my][mx].get_value()

    if target_pos == '.':
      # free space, just move
      grid[self._y][self._x].set_value('.')
      self._x = mx
      self._y = my
    elif target_pos == '#':
      # wall, dont try
      pass
    elif grid[my][mx].can_move(dir, grid):
      # try to see how far we can move
      grid[self._y][self._x].set_value('.')
      self._x = mx
      self._y = my

  def get_pos(self):
    return self._y, self._x

full_or_not = '--full' not in sys.argv
data = get_data_f(full_or_not, 'raw')

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

