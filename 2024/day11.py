'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day11.py ]   █
 █   [ Type ................................. Advent of Code 2024 puzzle ]   █
 █                                                                           █
 █   Day 11: Plutonian Pebbles                                               █
 █   https://adventofcode.com/2024/day/11                                    █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 20, 2024 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

import time
import sys
from aoc_utils import get_data_f

def parse_stones(stones):
  # takes a list of positions, and follows the rules in a specific order

  new_stones = []
  # we need to parse the stones without destroying the iteration
  for i, stone in enumerate(stones):
    if stone == 0:
      new_stones.append(1)
    elif len(str(stone)) % 2 == 0:
      sl = len(str(stone)) // 2
      lstone = int(str(stone)[0:sl])
      rstone = int(str(stone)[sl:])
      new_stones.append(lstone)
      new_stones.append(rstone)
    else:
      mul = stone * 2024
      new_stones.append(mul)
  return new_stones

def part_one(indata):
	# If the stone is engraved with the number 0, it is replaced by a stone 
  # engraved with the number 1.
  # If the stone is engraved with a number that has an even number of digits, 
  # it is replaced by two stones. The left half of the digits are engraved on 
  # the new left stone, and the right half of the digits are engraved on the 
  # new right stone. (The new numbers don't keep extra leading zeroes: 1000 
  # would become stones 10 and 0.)
  # 
  # If none of the other rules apply, the stone is replaced by a new stone; 
  # the old stone's number multiplied by 2024 is engraved on the new stone.
  EYESORE = 25
  num_stones = 0
  indata = [int(n) for n in indata[0].split()]

  print('Initial arrangement:')
  print(*indata, sep=' ')

  for blinks in range(EYESORE):
    #print(f'After {blinks} blink:')
    indata = parse_stones(indata)
    #print(*indata, sep=' ')

  return len(indata)

def part_two(indata):
  # do stuff again
  return

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

