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

def part_one(indata):
  ITERATIONS = 100
  robots = parse_p_and_v(indata)
  r = 103
  c = 101
  midx = c // 2
  midy = r // 2
  
  grid = numpy.zeros((r, c), dtype=int)

  for rp, rv in robots:
    rx, ry = rp
    vx, vy = rv
    rx = (rx + vx * ITERATIONS) % c
    ry = (ry + vy * ITERATIONS) % r
    grid[ry][rx] += 1

  #for line in grid:
  #  print(''.join('.' if c == 0 else str(c) for c in line))

  q1 = numpy.sum(grid[0:midy, 0:midx])
  q2 = numpy.sum(grid[0:midy, midx+1:])
  q3 = numpy.sum(grid[midy+1:, 0:midx])
  q4 = numpy.sum(grid[midy+1:, midx+1:])

  return q1 * q2 * q3 * q4

def build_grid(r, c):
  '''build our empty grid for the robot final positions'''
  return [[0 for _ in range(c)] for _ in range(r)]

def parse_p_and_v(data):
  _robots = []

  for line in data:
    regex_array = [int(num) for num in re.findall(r'-?[0-9]+', line)]

    px, py, vx, vy = regex_array
    _robots.append([(px, py), (vx, vy)])

  return _robots

def part_two(indata):
  # do stuff again
  return

full_or_not = '--full' not in sys.argv
data = get_data_f(full_or_not, 'lines')

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

