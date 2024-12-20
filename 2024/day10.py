'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day10.py ]   █
 █   [ Type ................................. Advent of Code 2024 puzzle ]   █
 █                                                                           █
 █   Day 10: Hoof It                                                         █
 █   https://adventofcode.com/202#/day/10                                    █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 18, 2024 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

import time
import sys
from os import system
from aoc_utils import get_data_f, colors
from collections import deque

def print_grid(_array):
  o = 10 # offset 10 (y,x)
  for row in range(len(_array)):
    for col in range(len(_array[0])):
      if _array[row][col].isdigit():
        print(f'{colors[int(_array[row][col])]}{_array[row][col]}', end='', flush=True)
      else:
        print(f'{colors[10]}{_array[row][col]}', end='', flush=True)
    print(colors[10])

def find_coords_in_grid(grid, target):
  xy = []
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == target:
        xy.append((r, c))
  return xy

def add_border(grid):
  for r in range(len(grid)):
    grid[r].insert(0, '#')
    grid[r].append('#')
  w = len(grid[0])
  grid.insert(0, ['#' for x in range(w)])
  grid.append(['#' for x in range(w)])

def bfs_hillclimb(grid, coordinates, target, part=1):
  # input(f'{grid}, {coordinates}, {target}')
  dirs = [[-1,0], [0,1], [1,0], [0,-1]]
  visited = set()
  coordinates = deque([coordinates])
  hits = 0

  while coordinates:
    pos = coordinates.popleft()
    if part == 1:
      visited.add(pos)
    y = pos[0]
    x = pos[1]
    if grid[y][x] == '9':
      # found the end of the trail. Increment the hit tracker and try any
      # remaining nodes in c
      hits += 1
      # print(f'trailhead found at {y},{x} - count: {hits}')
      continue
    else:
      # run a check in all directions, and add all direction coordinates
      # that are +1 of the current position
      for delta in dirs:
        ty = y + delta[0]
        tx = x + delta[1]
        try:
          curr_val = int(grid[y][x])
          delta_val = int(grid[ty][tx])
        except Exception as e:
          # print(f'Value cannot be read as integer: {e}')
          continue
        if (ty, tx) not in visited and delta_val == curr_val + 1:
          if part == 1:
            visited.add((ty, tx))
          coordinates.append((ty, tx))
  return hits

def part_one(indata):
  # added a border so I dont have to mess with out of bounds math
  add_border(indata)

  # so first i find all positions with 0 to get all potential trailheads
  # then I want to run individual bfs from each 0, so I can track the score
  # of that particular start. ie, (for c in potheads: bfs_search(grid, c)) 
  
  headsum = 0

  potheads = find_coords_in_grid(indata, '0')
  for start in potheads:
    headsum += bfs_hillclimb(indata, start, '9')

  return headsum

def part_two(indata):
  # hang on, can I just reuse part 1 and dont care about crossing old paths?
  add_border(indata)
  headsum = 0

  potheads = find_coords_in_grid(indata, '0')
  for start in potheads:
    headsum += bfs_hillclimb(indata, start, '9', part=2)

  return headsum

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

