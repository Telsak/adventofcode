'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day12.py ]   █
 █   [ Type ................................. Advent of Code 2024 puzzle ]   █
 █                                                                           █
 █   Day #: Garden Groups                                                    █
 █   https://adventofcode.com/2024/day/12                                    █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date .................... Jan 3, 2025 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

import time
import sys
from aoc_utils import get_data_f, add_border_to_2d_grid
from collections import deque

def bfs_zone(y, x, visited, _grid):
  # keep searching for all neighbors of _grid[y][x] that are equal
  # return area and edges
  dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

  edges = 0
  area = set()
  zone = _grid[y][x]

  nodes = deque([(y, x)])

  while nodes:
    node = nodes.popleft()
    visited.add(node)
    area.add(node)
    for di, dir in enumerate(dirs):
      ty = node[0] + dir[0]
      tx = node[1] + dir[1]
      #input(f'Testing {(ty, tx)}')
      if _grid[ty][tx] != zone:
        #print('found edge')
        edges += 1
      else:
        if (ty, tx) not in visited:
          #print('havent seen', (ty, tx), 'before')
          nodes.append((ty, tx))
          visited.add((ty, tx))

  corners = 0
  for node in area:
    y, x = node
    zone = _grid[y][x]
    for di in range(len(dirs)):
      ty1 = y + dirs[di][0]
      tx1 = x + dirs[di][1]
      i = (di + 1) % len(dirs)
      ty2 = y + dirs[i][0]
      tx2 = x + dirs[i][1]
      ty3 = y + dirs[di][0] + dirs[i][0]
      tx3 = x + dirs[di][1] + dirs[i][1]
      if zone != _grid[ty1][tx1] and zone != _grid[ty2][tx2]:
        corners += 1
      elif (zone*2 == _grid[ty1][tx1] + _grid[ty2][tx2]) and zone != _grid[ty3][tx3]:
        corners += 1

  return area, edges, corners

def part_one(indata):
  # prep the grid so I dont have to worry about boundaries
  indata = add_border_to_2d_grid(indata, r'#')

  visited = set()
  region = ''
  total = 0

  width = len(indata[0]) - 1
  height = len(indata) - 1
  
  for r in range(1, width):
    for c in range(1, height):
      if (r, c) in visited:
        continue
      # found a new region
      area, edges, _ = bfs_zone(r, c, visited, indata)
      area = len(area)
      print(f'A region of {indata[r][c]} with price {area} * {edges} = {area * edges}.')
      #input(f'corners {_}')
      total += (area * edges)


  return total

def part_two(indata):
  # prep the grid so I dont have to worry about boundaries
  indata = add_border_to_2d_grid(indata, r'#')

  visited = set()
  region = ''
  total = 0

  width = len(indata[0]) - 1
  height = len(indata) - 1
  
  for r in range(1, width):
    for c in range(1, height):
      if (r, c) in visited:
        continue
      # found a new region
      area, edges, corners = bfs_zone(r, c, visited, indata)
      area = len(area)
      #print(f'A region of {indata[r][c]} with price {area} * {corners} = {area * corners}.')
      total += (area * corners)


  return total

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

