'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ day2.py ]   █
 █   [ Type ................................. Advent of Code 2024 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 02, 2024 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

import time
import sys

def get_data(ns=0):
  day_file = sys.argv[0].split('.')[0]
  with open (f'.//input//{day_file}_input{ns * "_small"}', 'r') as file:
    filedata = [line.strip() for line in file.readlines()]
  return filedata

'''
The engineers are trying to figure out which reports are safe. The Red-Nosed 
reactor safety systems can only tolerate levels that are either gradually 
increasing or gradually decreasing. So, a report only counts as safe if both 
of the following are true:

* The levels are either all increasing or all decreasing.
* Any two adjacent levels differ by at least one and at most three.
'''

def part_one(indata):
  # do stuff
  safe_reports = 0
  for level in indata:
    level = [int(x) for x in level.split()]
    # only accept reports that are increasing or decreasing
    if level == sorted(level) or level == sorted(level, reverse=True):
      safe = True
      for i in range(len(level)-1):
        if safe:
          delta = abs(level[i] - level[i+1])
          # if the delta is within safe parameters
          if 0 < delta < 4:
            continue
          else:
            safe = False
      safe_reports += safe

  return safe_reports

def part_two(indata):
  # do stuff again
  unsafe = []
  safe_reports = 0
  for level in indata:
    level = [int(x) for x in level.split()]
    # only accept reports that are increasing or decreasing
    if level == sorted(level) or level == sorted(level, reverse=True):
      safe = check_delta(level, 0, 4)
    else:
      safe = False
    # try to get the report safe
    if not safe:
      unsafe.append(level)

    safe_reports += safe

  for entry in unsafe:
    safe_reports += problem_dampener(entry)
  return safe_reports

def check_delta(data, min_v, max_v):
  # determine if the submitted list passes the safe parameters
  safe = True
  for i in range(len(data)-1):
    if safe:
      delta = abs(data[i] - data[i+1])
      # if the delta is within safe parameters
      if delta > min_v and delta < max_v:
        continue
      else:
        safe = False
  return safe
  
def problem_dampener(indata, n=0, reason=''):
  # I will go out of bounds here..
  if n == len(indata):
    return False
  report = indata.copy()
  report.pop(n)
  if report == sorted(report) or report == sorted(report, reverse=True):
    safe = check_delta(report, 0, 4)
  else:
    safe = False

  if safe == False:
    n += 1
    safe = problem_dampener(indata, n, reason)
  return safe

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

