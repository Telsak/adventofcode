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
import re

def parse_table_column(table, col_index):
  # based on the str data in table[i][ci], use the operator in table[-2][ci]
  # to determine how to add the number
  _lines = get_table_column(table[:-2], col_index)
  lines = []
  total = 0
  for i in range(len(_lines[0])):
    _line = ''.join(get_table_column(_lines, i))
    _line = _line.replace('0', '')
    _line = int(_line)
    lines.append(_line)

  return lines
 
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
  # Lets start the same as p1, but then process the column line again
  # what if we for each line find the longest value and pad existing fields
  # with zeroes based on that length?
  # doesn't work as some columns have empty space before and some after
  # the actual numbers
  indata = indata.split('\n')
  indata.remove('')
  
  #bottom row is size of column
  indata.append([0 for x in indata[0].split()])
  for line in indata[:-1]:
    for i, col in enumerate(line.split()):
      if len(col) > indata[-1][i]:
        indata[-1][i] = len(col)

  table = []
  for line in indata[:-2]:
    _line = ''
    # work in small batches and just manually set spaces to 0 if they
    # fall within the column area, based on the size already parsed from
    # the first pass
    x = 0
    for seq in indata[-1]:
      for _ in range(seq):
        if line[x] == ' ':
          _line += '0'
        else:
          _line += line[x]
        x += 1
      _line += ' '
      x += 1
    table.append(_line.rstrip().split())
  table.append(indata[-2].split())
  table.append(indata[-1])

  # at this point I have a table with some data that also has the size of
  # all columns at the lowest row, now just send that to a modified parse
  # function that calls the table column function from part 1 and voila  
  total = 0
  for i in range(len(table[-1])):
    values = parse_table_column(table, i)
    if table[-2][i] == '*':
      total += prod(values)
    else:
      total += sum(values)
  
  return total

full_or_not = '--full' not in sys.argv

# part one or two? part one is default
if '-p2' in sys.argv:
  print('== Running part two ==')
  data = get_data(full_or_not, 'raw')
  start = time.time()
  output = part_two(data)
else:
  print('== Running part one (use -p2 for part two) ==')
  data = get_data(full_or_not)
  start = time.time()
  output = part_one(data)

stop = time.time()

print(f'Runtime was: {stop - start:.4f} seconds\n{output}')

