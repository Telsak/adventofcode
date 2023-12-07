'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ day1.py ]   █
 █   [ Type ................................. Advent of Code 2023 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 04, 2023 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

import time
import sys

numbers = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
        }

def get_data(ns: int = 0) -> list:
    day_file = sys.argv[0].split('.')[0]
    with open (f'.//input//{day_file}_input{ns * "_small"}', 'r') as file:
        filedata = [line.strip() for line in file.readlines()]
    return filedata
    
def get_digits(line: str) -> int:
    digits = [n for n in line.strip() if n.isdigit()]
    calibration_value = int(f'{digits[0]}{digits[-1]}')
    return calibration_value

def parse_text(line: str) -> str:
    digits = {}
    ll = len(line)

    l_index = ll
    r_index = -1

    for key, value in numbers.items():
        li = line.find(key)
        if -1 < li < l_index:
            digits[li] = value 
            l_index = li
        ri = line.rfind(key)
        if r_index < ri < ll:
            digits[ri] = value
            r_index = ri

    for i, n in enumerate(line):
        if n.isdigit():
            digits[i] = str(n)
            break
    for i, n in enumerate(line[::-1]):
        if n.isdigit():
            i = line.rfind(n)
            digits[i] = str(n)
            break

    line = (''.join(v for k, v in sorted(digits.items())))
    return line

def part_one(indata: list) -> int:
    calibration_sum = 0
    for line in indata:
        calibration_sum += get_digits(line)
    return calibration_sum

def part_two(indata: list) -> int:
    calibration_sum = 0
    for line in indata:
        line = parse_text(line)
        calibration_sum += get_digits(line)
    return calibration_sum



start = time.time()

data = get_data()
#output = part_one(data)
output = part_two(data)

stop = time.time()

print(f'Körning tog: {stop - start:.4f} sekunder\n{output}')

