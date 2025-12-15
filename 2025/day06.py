'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day06.py ]   █
 █   [ Type ................................. Advent of Code 2025 puzzle ]   █
 █                                                                           █
 █   Day 6: Trash Compactor                                                  █
 █   https://adventofcode.com/2025/day/6                                     █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date .................... Dec 6, 2025 ]             █
 █             [ Solved date ..................... Dec 15 2025 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

from aoc_utils import get_data, get_table_column
import time
import sys
from math import prod

def part_one(indata):
  # convert the indata lines to a grid table, split on spaces
  table = []
  for line in indata[:-1]:
    table.append([int(x) for x in line.split()])
  table.append([x for x in indata[-1].split()])
  
  total = 0
  #print(table)
  for i in range(len(table[0])):
    column = get_table_column(table, i)
    if column[-1] == '+':
      total += sum(column[:-1])
    else:
      total += prod(column[:-1])
  return total

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

print(f'Runtime was: {stop - start:.4f} seconds\n{output}')

