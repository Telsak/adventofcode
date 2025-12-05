'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day04.py ]   █
 █   [ Type ................................. Advent of Code 2025 puzzle ]   █
 █                                                                           █
 █   Day 4: Printing Department                                              █
 █   https://adventofcode.com/2025/day/4                                     █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 05, 2025 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

from aoc_utils import get_data
from aoc_utils import add_border_to_2d_grid
import time
import sys

def sweep(x, y, data, targ):
  lookup = data[y-1][x-1:x+2] + data[y][x-1:x+2] + data[y+1][x-1:x+2]
  return lookup.count(targ)

def part_one(indata):
  # do stuff
  indata = add_border_to_2d_grid(indata, '.')

  rows = len(indata)
  cols = len(indata[0])
  rolls = 0
  symb = '@'
  
  for r in range(1, rows-1):
    for c in range(1, cols-1):
      if indata[r][c] == symb and sweep(c, r, indata, symb) < 5:
        rolls += 1        

  return rolls

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

