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
 
def is_id_invalid_p1(id):
  # return true if the first half of the id is found more than once in
  # the id string
  idm = len(id) // 2
  return id.count(id[0:idm]) > 1

def is_id_invalid_p2(id):
  # trickiest part is to know how big slices to compare & count in the id
  # tried primes first, but got too edge-casey
  # try to find blocksizes that are up to half the length of id

  idl = len(id)
  # if the block is 1 and repeats, exit early
  if idl * id[0] == id:
    #print(id, idl, '<--')
    return True
  elif idl < 4:
    return False

  for width in range(2, idl//2+1):
    # increase the width size
    #print(f'id:{id} w:{width} l//w: {idl//width}')
    if id[0:width]*(idl//width) == id and idl % width == 0:
      return True

  return False

def part_one(indata):
    invalid_id_sum = 0
    for line in indata.split(','):
      start, stop = [int(x) for x in line.split('-')]
      # force 2 digits min
      if start < 10 and stop > 10:
        start = 10
      
      for id in range(start, stop+1):
        str_id = str(id)
        if len(str_id) % 2 == 0 and is_id_invalid_p1(str_id):
          invalid_id_sum += id
          #print(id, 'is invalid')

    return invalid_id_sum

def part_two(indata):
    # the digits sequences can now repeat more than once
    invalid_id_sum = 0
    for line in indata.split(','):
      start, stop = [int(x) for x in line.split('-')]
      # force 2 digits min
      if start < 10 and stop > 10:
        start = 10

      for id in range(start, stop+1):
        str_id = str(id)
        if is_id_invalid_p2(str_id):
          invalid_id_sum += id

    return invalid_id_sum

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

