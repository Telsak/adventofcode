'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ day2.py ]   █
 █   [ Type ................................. Advent of Code 2024 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 02, 2024 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

import time
import sys

def get_data(ns=0):
  day_file = sys.argv[0].split('.')[0]
  with open (f'.//input//{day_file}_input{ns * "_small"}', 'r') as file:
    filedata = [line.strip() for line in file.readlines()]
  return filedata

'''
The engineers are trying to figure out which reports are safe. The Red-Nosed 
reactor safety systems can only tolerate levels that are either gradually 
increasing or gradually decreasing. So, a report only counts as safe if both 
of the following are true:

* The levels are either all increasing or all decreasing.
* Any two adjacent levels differ by at least one and at most three.
'''

def part_one(indata):
  # do stuff
  safe_reports = 0
  for level in indata:
    level = [int(x) for x in level.split()]
    # only accept reports that are increasing or decreasing
    if level == sorted(level) or level == sorted(level, reverse=True):
      safe = True
      for i in range(len(level)-1):
        if safe:
          delta = abs(level[i] - level[i+1])
          # if the delta is within safe parameters
          if 0 < delta < 4:
            continue
          else:
            safe = False
      safe_reports += safe

  return safe_reports

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

print(f'Körning tog: {stop - start:.4f} sekunder\n{output}')

