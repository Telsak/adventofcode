'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day09.py ]   █
 █   [ Type ................................. Advent of Code 2024 puzzle ]   █
 █                                                                           █
 █   Day #: Disk Fragmenter                                                  █
 █   https://adventofcode.com/2024/day/9                                     █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 16, 2024 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

import time
import sys
from aoc_utils import get_data_f

def calc_checksum(_disk):
  # The final step of this file-compacting process is to update the 
  # filesystem checksum. To calculate the checksum, add up the result of 
  # multiplying each of these blocks' position with the file ID number it 
  # contains. The leftmost block is in position 0. If a block contains free 
  # space, skip it instead.
  
  chk = 0
  x = len(_disk)
  for position, id in enumerate(_disk):
    # print(f'{position} * {id} = {position * int(id)}')
    # print(f'{position}/{x}\r')
    chk += position * int(id)
  return chk

def generate_diskmap(diskdata):
  # generate the map of where disk files are saved
  disk = []
  pos = 0
  for i in range(len(diskdata)):
    # if this is an even position (or a file, at position i)
    if i % 2 == 0:
      # add pos index as many times as there are blocks indicated in [i]
      disk += [str(pos) for _ in range(int(diskdata[i]))]
      pos += 1
    else:
      # add empty spots as many times as there are blocks indicated in [i]
      epos = int(diskdata[i])
      disk += ['.' for x in range(epos)]
  return disk

def part_one(indata):
  
  disk = generate_diskmap(indata)

  # as long as there are free spaces, shuffle elements from the back
  di = 0
  try:
    # lets continue while we have free spots left
    while '.' in disk:
      # print('trying', di, len(disk))
      # skip occupied positions
      while disk[di] != '.':
        di += 1
      # if the last position is a file, pop it off and assign the value
      # to the current free spot and increment the position, otherwise
      # keep stripping the last position
      if disk[-1].isdigit():
        disk[di] = disk.pop()
        di += 1
      else:
        while disk[-1] == '.':
          disk.pop()

      #input(disk)
  except:
    print('index out of bound!')

  checksum = calc_checksum(disk)
  return checksum

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
  output = part_one(data[0])

stop = time.time()

print(f'Körning tog: {stop - start:.4f} sekunder\n{output}')

