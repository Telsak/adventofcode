'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day03.py ]   █
 █   [ Type ................................. Advent of Code 2025 puzzle ]   █
 █                                                                           █
 █   Day 3: Lobby                                                            █
 █   https://adventofcode.com/2025/day/3                                     █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 03, 2025 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

from aoc_utils import get_data
import time
import sys

def highest_value(my_list):
  # dumb and simple, find the biggest value and index. This works since we
  # get a subsection of the main list and the first index hit will always be
  # the value that is found with max()
  hv = max(my_list)
  hvi = my_list.index(hv)
  return((hv, hvi))

def part_one(indata):
  # do two lookups, one for highest value that isnt at the end
  # and another for whatever highest is to the right of the first value
  total_joltage = 0
  for bank in indata:
    lv, lvi = highest_value(bank[:-1])
    rv, _ = highest_value(bank[lvi+1:])
    total_joltage += int(lv+rv)
  return total_joltage

def part_two(indata):
  # Scans ahead in the list but uses an offset and rear buffer so we always
  # have 12-n batteries to choose from. Greedily pick the first highest value
  # and so on...
  total_joltage = []
  for bank in indata:
    gi, hvi = 0, 0
    joltage = ''
    for i in range(12):
      #print(f'Checking {bank[gi:-11+i or None]} at index {gi}')
      hv, hvi = highest_value(bank[gi:-11+i or None])
      gi = gi + hvi + 1
      #print(f'Highest found: {hv} at index {hvi}')
      joltage += hv
    total_joltage.append(int(joltage))
    #print('===',joltage,'===')
  return sum(total_joltage)

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

