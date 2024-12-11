'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day07.py ]   █
 █   [ Type ................................. Advent of Code 2024 puzzle ]   █
 █                                                                           █
 █   Day 7: Bridge Repair                                                    █
 █   https://adventofcode.com/2024/day/7                                     █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 10, 2024 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

import time
import sys
from aoc_utils import get_data_f

def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

def equation_sum_finder(total, numbers, operators, base=2):
  # just for fun.. we have two operators, so index 0 or 1
  # find the # of numbers, or bits..
  bit_len = str(base-1) * (len(numbers) - 1)
  bits = int(bit_len, base) + 1
  for perm in range(0, bits):
    if base == 2:
      _ = f'{perm:0{len(numbers)-1}b}' # generate a bitmask
    else:
      _ = f'{int(ternary(perm)):0{len(bit_len)}d}'
    a = ''
    # iterate over all the numbers, to run them through the bitmask
    for num in range(0, len(numbers)):
      a += ' ' + str(numbers[num])
      if num < len(_):
        a += ' ' + operators[int(_[num])]
    result = left_to_right(a, total)
    if result == total:
      return True
  return False

def left_to_right(configuration, target):
  tokens = configuration.split()
  total = int(tokens[0])
  
  for i in range(1, len(tokens)):
    if tokens[i] == '+':
      total += int(tokens[i+1])
    elif tokens[i] == '*':
      total *= int(tokens[i+1])
    elif tokens[i] == '||':
      total = int(str(total) + tokens[i+1])
    if total > target:
      return total
  return total

def part_one(indata):
  ops = ['+', '*']
  result = 0
  for line in indata:
    target, nums = line.split(':')
    target = int(target)
    nums = [int(n) for n in nums.strip().split()]
    works = equation_sum_finder(target, nums, ops)
    if works == True:
      result += int(target)
  return result

def part_two(indata):
  ops = ['+', '*', '||']
  result = 0
  z = len(indata)
  for i, line in enumerate(indata):
    target, nums = line.split(':')
    target = int(target)
    nums = [int(n) for n in nums.strip().split()]
    #print(f'Checking line {i+1}/{z}...', end='\r')
    works = equation_sum_finder(target, nums, ops, base=3)
    if works == True:
      result += int(target)
  return result

full_or_not = '--full' not in sys.argv
data = get_data_f(full_or_not, 'lines')

# part 1 asserts
# assert equation_sum_finder(190, ['10', '19'], ['+', '*']) == True, "should be True"
# assert equation_sum_finder(3267, ['81', '40', '27'], ['+', '*']) == True, "should be True"
# assert equation_sum_finder(292, ['11', '6', '16', '20'], ['+', '*']) == True, "should be True"

# part 2 asserts
# assert equation_sum_finder(156, ['15', '6'], ['+', '*', '||'], base=3) == True, "should be True"
# assert equation_sum_finder(7290, ['6', '8', '6', '15'], ['+', '*', '||'], base=3) == True, "should be True"
# assert equation_sum_finder(192, ['17', '8', '14'], ['+', '*', '||'], base=3) == True, "should be True"



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

