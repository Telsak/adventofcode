'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ day3.py ]   █
 █   [ Type ................................. Advent of Code 2015 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 02, 2024 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

import time
import sys
from collections import defaultdict

def get_data(ns=0):
    day_file = sys.argv[0].split('.')[0]
    with open (f'.//input//{day_file}_input{ns * "_small"}', 'r', encoding='utf-8') as file:
        filedata = file.readline()
    print(len(filedata))
    return filedata
    
def part_one(indata):
  # do stuff

  coords = [0,0]
  coord_list = ["0,0"]
  for line in indata:
    for x in line:
      if x == ">":
        coords[0]+=1
      elif x == "<": 
        coords[0]-=1
      elif x == "^":
        coords[1]+=1
      elif x == "v":
        coords[1]-=1
      coord_list.append(str(coords[0])+","+str(coords[1]))
  return len(set(coord_list)) 

def part_two(indata):
  # do stuff again
  # santa is index 0, robosanta is index 1
  actor = 0
  coords = [[0,0], [0,0]]
  coord_list = ['0,0']

  for line in indata:
    for x in line:
      actor = (actor + 1) % 2
      if x == ">":
        coords[actor][0]+=1
      elif x == "<": 
        coords[actor][0]-=1
      elif x == "^":
        coords[actor][1]+=1
      elif x == "v":
        coords[actor][1]-=1
      coord_list.append(str(coords[actor][0])+","+str(coords[actor][1]))
  return len(set(coord_list)) 

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

