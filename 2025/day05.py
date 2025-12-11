'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day05.py ]   █
 █   [ Type ................................. Advent of Code 2025 puzzle ]   █
 █                                                                           █
 █   Day 5: Cafeteria                                                        █
 █   https://adventofcode.com/2025/day/5                                     █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date .................... Dec 5, 2025 ]             █
 █             [ Solved date .................... Dec ##, 2025 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

from aoc_utils import get_data
import time
import sys

def part_one(indata):
  # first impressions, it will get expensive to bruteforce create multiple
  # overlapping sequences, feels like a trap for p2 (also its bad)
  # went with num in range, fast in python?

  fresh_ranges = []
  available = []
  total = 0

  for line in indata:
    if '-' in line:
      fresh = [int(x) for x in line.split('-')]
      fresh_ranges.append(fresh)
    elif len(line) > 0:
      available.append(int(line))

  for unknown in available:
    for fresh in fresh_ranges:
      if unknown in range(fresh[0],fresh[1]+1):
        total += 1
        break

  return total

def part_two(indata):
  # ok so crazy idea, but what if we just build the number ranges real quick
  # using sets, and just union them together to get all unique IDs
  # I KNEW IT IT WAS A FUCKING TRAP GDI
  # ok ok.. all we really need is limit the ranges. Subtract the smallest num
  # from all values, assuming it won't break the smallest end value?
  # should shift all numbers into more manageable ranges but not fuck with the
  # relative worth in ids in ranges. THIS IS WHY HE IGNORES THE OTHER PART OF
  # THE INDATA??!? 
  # Nope..

  fresh_ids = set()

  smallest = None
  fresh_ranges = []
  unique_ranges = []
  
  for i, line in enumerate(indata):
    if '-' in line:
      fresh = [int(x) for x in line.split('-')]
      fresh_ranges.append(fresh)
      #fresh_ids = fresh_ids.union(range(fresh[0], fresh[1]+1))
  
  fresh_ranges.sort()
  print(fresh_ranges)
      
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

