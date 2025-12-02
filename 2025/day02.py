'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day02.py ]   █
 █   [ Type ................................. Advent of Code 2025 puzzle ]   █
 █                                                                           █
 █   Day 2: Gift Shop                                                        █
 █   https://adventofcode.com/2025/day/2                                     █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 02, 2025 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

from aoc_utils import get_data
import time
import sys
 
def is_id_invalid(id):
  # return true if the first half of the id is found more than once in
  # the id string
  idm = len(id) // 2
  return id.count(id[0:idm]) > 1

def part_one(indata):
    invalid_id_sum = 0
    for line in indata.split(','):
      start, stop = [int(x) for x in line.split('-')]
      # force 2 digits min
      if start < 10 and stop > 10:
        start = 10
      
      for id in range(start, stop+1):
        str_id = str(id)
        if len(str_id) % 2 == 0 and is_id_invalid(str_id):
          invalid_id_sum += id
          #print(id, 'is invalid')

    return invalid_id_sum

def part_two(indata):
    # do stuff again
    return

full_or_not = '--full' not in sys.argv
data = get_data(full_or_not, 'raw')

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

