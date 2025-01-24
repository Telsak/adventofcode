'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day13.py ]   █
 █   [ Type ................................. Advent of Code 2024 puzzle ]   █
 █                                                                           █
 █   Day 13: Claw Contraption                                                █
 █   https://adventofcode.com/2024/day/13                                    █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date .................... Jan 23, 2024 ]            █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

import time
import sys
from aoc_utils import get_data_f

def part_one(indata):
  # do stuff
  games = []
  for line in indata:
    if 'A:' in line:
      btn_a = []
      line = line.split(':')[1].split(',')
      ax = int(line[0][3:])
      ay = int(line[1][3:])
      btn_a = [ax, ay]
    elif 'B:' in line:
      btn_b = []
      line = line.split(':')[1].split(',')
      bx = int(line[0][3:])
      by = int(line[1][3:])
      btn_b = [bx, by]
    elif 'Prize' in line:
      line = line.split(':')[1].split(',')
      px = int(line[0][3:])
      py = int(line[1][3:])
      prize = [px, py]

      games.append([btn_a, btn_b, prize])

  tokens = 0
  for game in games:
    tokens += solved_equation(game[0], game[1], game[2], 1)

  return tokens

def scan_game(a, b, prize):
  tokens = 0
  for ai in range(100):
    for bi in range(100):
      tx = (a[0] * ai) + (b[0] * bi)
      ty = (a[1] * ai) + (b[1] * bi)
      if tx == prize[0] and ty == prize[1]:
        if tokens == 0:
          tokens = (ai * 3) + bi
        elif ai + bi < tokens:
          tokens = (ai * 3) + bi
  return tokens

def solved_equation(a, b, prize, part=2):
  # the new big number is too big to bruteforce like I did in part 1
  if part == 1:
    CORRECTION = 0
  else:
    CORRECTION = 10000000000000

  ax, ay = a
  bx, by = b
  px = prize[0] + CORRECTION
  py = prize[1] + CORRECTION

  b = abs((bx * ay) - (by * ax))
  p = abs((px * ay) - (py * ax))
  
  b = p/b

  if b.is_integer():
    a = int((px - (int(b) * bx)) / ax)
    # verify the solution actually works, before returning OK
    try:
      assert (a * ax + int(b) * bx) == px
      assert (a * ay + int(b) * by) == py
    except:
      a, b = 0, 0
  else:
    a, b = 0, 0

  return (a * 3) + int(b)

def part_two(indata):
  # do stuff again
  games = []
  for line in indata:
    if 'A:' in line:
      btn_a = []
      line = line.split(':')[1].split(',')
      ax = int(line[0][3:])
      ay = int(line[1][3:])
      btn_a = [ax, ay]
    elif 'B:' in line:
      btn_b = []
      line = line.split(':')[1].split(',')
      bx = int(line[0][3:])
      by = int(line[1][3:])
      btn_b = [bx, by]
    elif 'Prize' in line:
      line = line.split(':')[1].split(',')
      px = int(line[0][3:])
      py = int(line[1][3:])
      prize = [px, py]

      games.append([btn_a, btn_b, prize])

  tokens = 0
  for game in games:
    tokens += solved_equation(game[0], game[1], game[2])

  return tokens

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

