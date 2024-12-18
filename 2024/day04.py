'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day04.py ]   █
 █   [ Type ................................. Advent of Code 2024 puzzle ]   █
 █                                                                           █
 █   Day 4: Ceres Search                                                     █
 █   https://adventofcode.com/2024/day/4                                     █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 04, 2024 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

import time
import sys
from os import system

def get_data(ns=0):
  day_file = sys.argv[0].split('.')[0]
  with open (f'.//input//{day_file}_input{ns * "_small"}', 'r') as file:
    filedata = [line.strip() for line in file.readlines()]
  return filedata
    
def part_one(indata):
  # do naive search I guess? 
  TARGET = 'XMAS'
  target_count = 0
  dirs = [
      (1,0,'→'), 
      (1,1,'↘'), 
      (0,1,'↓'), 
      (-1,1,'↙'), 
      (-1,0,'←'), 
      (-1,-1,'↖'), 
      (0,-1,'↑'), 
      (1,-1,'↗')
    ]

  # bottom and right borders
  b = len(indata) -1
  r = len(indata[0]) -1
  # for debug 
  # zeros = [ ['.']*(b+1) for _ in range(b+1) ]
  for ri, row in enumerate(indata):
    for ci, col in enumerate(row.strip()):
      # always start with the same character
      if indata[ri][ci] == TARGET[0]:
        # print('X found at', ri, ci)
        for dir in dirs:
          found = False
          x = ci
          y = ri
          path = [(y,x)]
          for i in range(1,len(TARGET)):
            x += dir[0]
            y += dir[1]
            if (y >= 0 and x >= 0) and (y <= b and x <= r):
              # print(f'{ri, ci} {y} and col {x}, index {i}, dir {dir[2]}')
              if indata[y][x] == TARGET[i]:
                path.append((y,x))
                found = True
              else:
                found = False
                break
            else:
              found = False
              break
          if found == True:
            # print(f'{TARGET} found at {ri, ci}-{y, x}')
            # print(path)
            target_count += 1
            # print('total found:', target_count)
            # for debug
            # print_grid(zeros, path, 'XMAS')
  return target_count

RED = '\033[93m'
GREEN = '\033[92m'
RST = '\033[0m'

def print_grid(array, coords, s):
  system('clear')
  for i, v in enumerate(coords):
    array[v[0]][v[1]] = s[i]
  for r in array:
    for _ in r:
      if _ in 'SM':
        color = GREEN
      elif _ == 'A':
        color = RED
      else:
        color = RST
      print(color + _, end='')
    print(RST)

def part_two(indata):
  # do stuff again
  target_count = 0

  b = len(indata) -1
  r = len(indata[0]) -1

  zeros = [ ['.']*(b+1) for _ in range(b+1) ]
  a_points = []
  x_sum = sum([ord(x) for x in 'SAM'])
  for ri, row in enumerate(indata):
    for ci, col in enumerate(row.strip()):
      rcheck = ri > 0 and ri < b
      ccheck = ci > 0 and ci < r
      # Just find the center point of the X, ie the A
      if indata[ri][ci] == 'A' and (rcheck and ccheck):
        # print('A (possible X-MAS found at', ri, ci)
        path = [0,(ri, ci),0]
        ord1 = indata[ri+1][ci-1]+'A'+indata[ri-1][ci+1]
        ord2 = indata[ri-1][ci-1]+'A'+indata[ri+1][ci+1]
        if sum([ord(x) for x in ord1]) == x_sum == sum([ord(x) for x in ord2]):
          target_count += 1
          path = [(ri+1,ci-1), (ri, ci), (ri-1, ci+1),
                  (ri-1, ci-1), (ri, ci), (ri+1, ci+1)
                ]
          # debug only
          # print_grid(zeros, path, ord1+ord2)
          # input('Press enter to continue')
  return target_count

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

print(f'Körning tog: {stop - start:.4f} sekunder\n{output}')

