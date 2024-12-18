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
    if id != '.':
      chk += position * int(id)
  return chk

def generate_diskmap(diskdata, part=1):
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
      disk += ['.' for _ in range(epos)]
  return disk

def part_one(indata):
  disk = generate_diskmap(indata)
  input(disk)
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
  except:
    print('index out of bound!')

  checksum = calc_checksum(disk)
  return checksum

def part_two(indata):
  disk = generate_diskmap(indata, part=2)
  # a lot of previous attempts were with using .pop() to pull things from the
  # end of the list, but that is counterproductive now when some elements
  # can and should be left where they are if they dont fit
  # we still work from right to left
  
  # set the seen id to -1 to begin with, and keep track of the number of times
  # where the id has been seen. When something new is seen, either a space or
  # a new digit, save the index+1 (which is the previous position from right)
  # and now you know how many positions the file takes up

  seen_id = -1

  for r_pos, file_id in reversed(list(enumerate(disk))):
    if file_id != seen_id and file_id != '.':
      i = r_pos
      id_count = 1
      fl = [i]
      seen_id = file_id
      # now we know how many there are of 
      while i > 0 and disk[i-1] == file_id:
        id_count += 1
        i -= 1
        fl += [i]
      # look for empty spaces up to r_pos index
      sl = [x for x in fl]; lsl = len(sl)
      s_count = 0
      for l_pos in range(r_pos):
        # if this isn't a free space, ignore it and move to the next
        if disk[l_pos] != '.':
          s_count = 0
          continue
        else:
          # set up to start tracking spaces
          s_count += 1
          if s_count == 1:
            l_start = l_pos
          if s_count == lsl:
            l_end = l_pos
            for s in range(l_start, l_end + 1):
              disk[s], disk[sl[s - l_start]] = disk[sl[s - l_start]], disk[s]
            break
      continue
    else:
      continue
  return calc_checksum(disk)

full_or_not = '--full' not in sys.argv
data = get_data_f(full_or_not, 'lines')

# part one or two? part one is default
if '-p2' in sys.argv:
  print('== Running part two ==')
  start = time.time()
  output = part_two(data[0])
else:
  print('== Running part one (use -p2 for part two) ==')
  start = time.time()
  output = part_one(data[0])

stop = time.time()

print(f'Körning tog: {stop - start:.4f} sekunder\n{output}')

