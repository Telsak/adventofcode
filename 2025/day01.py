'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day01.py ]   █
 █   [ Type ................................. Advent of Code 2025 puzzle ]   █
 █                                                                           █
 █   Day 1: Secret Entrance                                                  █
 █   https://adventofcode.com/2025/day/1                                     █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 01, 2025 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''
from aoc_utils import get_data
import time
import sys

def part_one(indata):
    # iterate over indata instructions, mark how many times the dial is left
    # pointing at 0 after any rotation in the sequence (modulus)
    dial_pos = 50
    password = 0
    print(f'- The dial starts by pointing at {dial_pos}')

    for line in indata:
      op = '+' if line[0] == 'R' else '-'
      val = int(op + line[1:])
      dial_pos = (dial_pos + val) % 100
      if dial_pos == 0:
        password += 1

    return password

def part_two(indata):
    # iterate over indata instructions, mark how many times the dial passes or
    # stops at 0
    dial_pos = 50
    password = 0
    print(f'- The dial starts by pointing at {dial_pos}')

    # feel like I could do this cleaner with just % and //, but logic escapes
    # me currently
    for line in indata:
      op = 1 if line[0] == 'R' else -1
      val = int(line[1:])
      for i in range(val):
        dial_pos += op
        if dial_pos % 100 == 0:
          password += 1
      #print(line, dial_pos % 100)

    return password


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

