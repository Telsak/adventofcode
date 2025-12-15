'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day07.py ]   █
 █   [ Type ................................. Advent of Code 2025 puzzle ]   █
 █                                                                           █
 █   Day 7: Laboratories                                                     █
 █   https://adventofcode.com/2025/day/7                                     █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date .................... Dec 7, 2025 ]             █
 █             [ Solved date ..................... Dec 15 2025 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

from aoc_utils import get_data
from aoc_utils import colors 
import time
import sys

def render_diagram(table):
  blue = colors[3]
  cyan = colors[4]
  a_green = colors[5]
  l_green = colors[6]
  yellow = colors[8]
  red = colors[9]
  reset = colors[10]

  for line in table:
    for c in line:
      if c == 'S':
        print(f'{yellow}{c}{reset}', end='')
      elif c == '^':
        print(f'{cyan}{c}{reset}', end='')
      elif c == '|':
        print(f'{a_green}{c}{reset}', end='')
      else:
        print(' ', end='')
    print()

def part_one(indata):
  # basically, trace 'down' from 'S' until you hit '^', then stop trace and
  # start two new traces left and right of the '^' position
  # make sure the splitter actually has a beam going into it from 'above'
  height = len(indata)
  splits = 0
  for y, line in enumerate(indata):
    for x, c in enumerate(line):
      if c in 'S|^':
        if c == 'S':
          indata[y+1][x] = '|'
        elif c == '^' and indata[y-1][x] == '|':
          if indata[y][x-1] is not '|':
            indata[y][x-1] = '|'
            indata[y+1][x-1] = '|'
          if indata[y][x+1] is not '|':
            indata[y][x+1] = '|'
          splits += 1
        elif c == '|':
          if y+1 < height and indata[y+1][x] == '^':
            continue
          elif y+1 < height:
            indata[y+1][x] = '|'

  render_diagram(indata)
  return splits

def part_two(indata):
  # do stuff again
  return

full_or_not = '--full' not in sys.argv
data = get_data(full_or_not, 'grid')

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

print(f'Runtime was: {stop - start:.4f} seconds\n{output}')

