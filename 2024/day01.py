'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day01.py ]   █
 █   [ Type ................................. Advent of Code 2024 puzzle ]   █
 █                                                                           █
 █   Day 1: Historian Hysteria                                               █
 █   https://adventofcode.com/2024/day/1                                     █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 02, 2024 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

import time
import sys
from collections import defaultdict as ddict

def get_data(ns=0):
  day_file = sys.argv[0].split('.')[0]
  with open (f'.//input//{day_file}_input{ns * "_small"}', 'r') as file:
    filedata = [line.strip() for line in file.readlines()]
  return filedata
    
def part_one(indata):
  left = []
  right = []
  distance = 0
  for line in indata:
    line = [int(x) for x in line.split()]
    left.append(line[0])
    right.append(line[1])
  left.sort()
  right.sort()

  for i in range(len(left)):
    distance += abs(left[i] - right[i])

  return distance

def part_two(indata):
  # do stuff again
  left = []
  right = ddict(int)
  similarity = 0
  for line in indata:
    line = [int(x) for x in line.split()]
    left.append(line[0])
    right[line[1]] += 1
  for number in left:
    similarity += (number * right[number])
  return similarity

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

