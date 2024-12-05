'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day05.py ]   █
 █   [ Type ................................. Advent of Code 2024 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 05, 2024 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

import time
import sys
from collections import defaultdict as dd

def get_data(ns=0):
  day_file = sys.argv[0].split('.')[0]
  with open (f'.//input//{day_file}_input{ns * "_small"}', 'r') as file:
    filedata = [line.strip() for line in file.readlines()]
  return filedata
    
def part_one(indata):
  # The first section specifies the page ordering rules, one per line. The
  # first rule, 47|53, means that if an update includes both page number 47 and
  # page number 53, then page number 47 must be printed at some point before
  # page number 53. (47 doesn't necessarily need to be immediately before 53;
  # other pages are allowed to be between them.)

  # The second section specifies the page numbers of each update. Because most 
  # safety manuals are different, the pages needed in the updates are different
  # too. The first update, 75,47,61,53,29, means that the update consists of
  # page numbers 75, 47, 61, 53, and 29.
  # me: maybe something with linked list to manage the priorities?
  
  inst = []
  updates = []
  inst_map = dd(list)
  valid_updates = []
  for row in indata:
    if '|' in row:
      inst.append([int(x) for x in row.split('|')])
    elif len(row) < len(indata[0]):
      continue
    else:
      updates.append([int(x) for x in row.split(',')])
  # hashmap with relationships for the pages
  for k, v in inst:
    inst_map[k].append(v)
  
  # parse all the updates, 
  for update in updates:
    for page in update:
      valid = True
      if len(inst_map[page]) > 0:
        for secondary in inst_map[page]:
          if secondary in update:
            valid = update.index(page) < update.index(secondary)
            if valid == False:
              break
        if valid == False:
          break
    if valid == True:
      # print(update)
      valid_updates.append(update)

  return sum([x[(len(x) // 2)] for x in valid_updates])

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

