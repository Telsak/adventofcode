'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day14.py ]   █
 █   [ Type ................................. Advent of Code 2024 puzzle ]   █
 █                                                                           █
 █   Day 14: Restroom Redoubt                                                █
 █   https://adventofcode.com/2024/day/14                                    █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date .................... Jan 24, 2025 ]            █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

import time
import sys
from aoc_utils import get_data_f
import re
import numpy

def part_one(indata, full=False):
  ITERATIONS = 100
  robots = parse_p_and_v(indata)

  RC = [[103,101], [7,11]]
  ROWS, COLS = RC[full]

  grid = numpy.zeros((ROWS, COLS), dtype=int)

  for rp, rv in robots:
    rx, ry = rp
    vx, vy = rv
    rx = (rx + vx * ITERATIONS) % COLS
    ry = (ry + vy * ITERATIONS) % ROWS
    grid[ry][rx] += 1


  return quadrants(grid, COLS, ROWS)

def quadrants(_grid, COLS, ROWS):
  midx = COLS // 2
  midy = ROWS // 2

  q1 = numpy.sum(_grid[0:midy, 0:midx])
  q2 = numpy.sum(_grid[0:midy, midx+1:])
  q3 = numpy.sum(_grid[midy+1:, 0:midx])
  q4 = numpy.sum(_grid[midy+1:, midx+1:])

  return q1 * q2 * q3 * q4

def build_grid(r, c):
  '''build our empty grid for the robot final positions'''
  return [[0 for _ in range(c)] for _ in range(r)]

def parse_p_and_v(data):
  _robots = []

  for line in data:
    regex_array = [int(num) for num in re.findall(r'-?[0-9]+', line)]

    px, py, vx, vy = regex_array
    _robots.append([[px, py], (vx, vy)])

  return  _robots

def part_two(indata, full=False):
  # do stuff again
  robots = parse_p_and_v(indata)
  
  pos = [r[0] for r in robots]
  vel = [v[1] for v in robots]

  RC = [[103,101], [7,11]]
  ROWS, COLS = RC[full]
  
  grid = numpy.zeros((ROWS, COLS), dtype=int)

  min_safety = 0
  max_safety = 0
  
  for i in range(len(pos)):
    rx, ry = pos[i]
    grid[ry][rx] += 1

  for n in range(1, (ROWS * COLS)+1):
    for i in range(len(pos)):
      rx, ry = pos[i]
      vx, vy = vel[i]
      
      grid[ry][rx] -= 1
      rx = (rx + vx) % COLS
      ry = (ry + vy) % ROWS
      grid[ry][rx] += 1
      pos[i][0] = rx
      pos[i][1] = ry

    #for line in grid:
    #  print(''.join('.' if c == 0 else str(c) for c in line))
    
    safety_factor = quadrants(grid, ROWS, COLS)
    if safety_factor < min_safety or min_safety == 0:
      min_safety = safety_factor
      seconds = n
    if safety_factor > max_safety:
      max_safety = safety_factor
  
  return seconds

full_or_not = '--full' not in sys.argv
data = get_data_f(full_or_not, 'lines')

# part one or two? part one is default
if '-p2' in sys.argv:
  print('== Running part two ==')
  start = time.time()
  output = part_two(data, full_or_not)
else:
  print('== Running part one (use -p2 for part two) ==')
  start = time.time()
  output = part_one(data, full_or_not)

stop = time.time()

print(f'Körning tog: {stop - start:.4f} sekunder\n{output}')

