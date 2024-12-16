'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day08.py ]   █
 █   [ Type ................................. Advent of Code 2024 puzzle ]   █
 █                                                                           █
 █   Day #: Resonant Collinearity                                            █
 █   https://adventofcode.com/2024/day/8                                     █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 11, 2024 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

import time
import sys
from aoc_utils import get_data_f
from itertools import combinations

def part_one(indata): 
  # the idea is to find pairs of antennas, which means I need to find
  # all coordinates where antenna x appears, and then track all pair of
  # coordinates, find the k value and plot the antinodes from the x1+k type
  # values
  antennas = {'types': {}}
  antinodes = set()
  for r in range(len(indata)):
    for c in range(len(indata[0])):
      if indata[r][c] != '.':
        if indata[r][c] in antennas['types']:
          antennas['types'][indata[r][c]].append((r, c))
        else:
          antennas['types'][indata[r][c]] = [(r, c)]
  for i in antennas['types']:
    pairs = list(combinations(antennas['types'][i], 2))
    for pair in pairs:
      dy = pair[0][0] - pair[1][0]
      dx = pair[0][1] - pair[1][1]
      # antinode x and y, run test to see if they end up out of bounds
      # we need two of these, one for the regular dx, dy and one for the
      # inverse direction
      ay1 = pair[0][0] + dy
      ax1 = pair[0][1] + dx
      # test the first node
      if 0 <= ay1 < len(indata) and 0 <= ax1 < len(indata[0]):
        antinodes.add((ay1, ax1))
      ay2 = pair[1][0] + (dy * -1)
      ax2 = pair[1][1] + (dx * -1)
      if 0 <= ay2 < len(indata) and 0 <= ax2 < len(indata[0]):
        antinodes.add((ay2, ax2))
  return len(antinodes)

def part_two(indata):
  # this time we do the same, but the antinodes repeat on the same delta mods
  antennas = {'types': {}}
  antinodes = set()
  for r in range(len(indata)):
    for c in range(len(indata[0])):
      if indata[r][c] != '.':
        if indata[r][c] in antennas['types']:
          antennas['types'][indata[r][c]].append((r, c))
        else:
          antennas['types'][indata[r][c]] = [(r, c)]
        # antennas are also antinodes, so add them too
        antinodes.add((r, c))
  for i in antennas['types']:
    pairs = list(combinations(antennas['types'][i], 2))
    for pair in pairs:
      dy = pair[0][0] - pair[1][0]
      dx = pair[0][1] - pair[1][1]
      # same as in p1, continously test if the antinode position is out of bounds
      # but also repeat the delta move until it no longer works
      ay1 = pair[0][0] + dy
      ax1 = pair[0][1] + dx
      while 0 <= ay1 < len(indata) and 0 <= ax1 < len(indata[0]):
        antinodes.add((ay1, ax1))
        ay1 += dy
        ax1 += dx
      # now the same for the other coordinate
      dy = dy * -1
      dx = dx * -1
      ay2 = pair[1][0] + dy
      ax2 = pair[1][1] + dx
      while 0 <= ay2 < len(indata) and 0 <= ax2 < len(indata[0]):
        antinodes.add((ay2, ax2))
        ay2 += dy
        ax2 += dx
  return len(antinodes)

def print_grid(indata, nodes):
  print(nodes)
  for r in range(len(indata)):
    for c in range(len(indata[r])):
      if (r,c) in nodes and indata[r][c] == '.':
        print('#', end='')
      else:
        print(indata[r][c], end='')
    print()

full_or_not = '--full' not in sys.argv
data = get_data_f(full_or_not, 'grid')

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

