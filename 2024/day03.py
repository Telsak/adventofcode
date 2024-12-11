'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ day3.py ]   █
 █   [ Type ................................. Advent of Code 2024 puzzle ]   █
 █                                                                           █
 █   Day 3: Mull It Over                                                     █
 █   https://adventofcode.com/2024/day/3                                     █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 03, 2024 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

import time
import sys
import re

def get_data(ns=0):
  day_file = sys.argv[0].split('.')[0]
  with open (f'.//input//{day_file}_input{ns * "_small"}', 'r') as file:
    filedata = [line.strip() for line in file.readlines()]
  return filedata
    
def part_one(indata):
  # do stuff
  mem_product = 0
  for line in indata:
    results = re.findall("mul\([0-9]+,[0-9]+\)", line)
    for result in results:
      nums = [int(x) for x in result[4:-1].split(',')]
      mem_product += nums[0] * nums[1]
  return mem_product

def part_two(indata):
  # do stuff again
  operations = []
  mem_product = 0
  work = True
  
  # Find all operations and possible on/off instructions so we can run them
  # in order later
  indata = ''.join(indata)
  for result in re.finditer("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", indata):
    operations.append((result.start(), result.group()))
  operations.sort(key=lambda operations: operations[0])
  for instruction in operations:
    #print(instruction)
    if instruction[1] == "don't()":
      #print("Found don't(), work=False")
      work = False
    elif instruction[1] == "do()":
      #print("Found do(), work=True")
      work = True
    elif work == True and "mul" in instruction[1]:
      nums = [int(x) for x in instruction[1][4:-1].split(',')]
      #print('Multiplying', nums)
      mem_product += nums[0] * nums[1]

  return mem_product

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

