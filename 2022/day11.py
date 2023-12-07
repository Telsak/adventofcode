'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ............................................... day11.py ]   █
 █   [ Type ................................. Advent of Code 2022 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 19, 2022 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''
import time
import re
from collections import deque

def get_data(ns=0):
    with open (f'.//input//day11_input{ns * "_small"}', 'r') as file:
        filedata = re.split(r'\n\s*\n', file.read())
    return filedata
    
def parse_monkey(block, worry_d):
    for line in block.split('\n'):
        if 'Monkey' in line:
            mn = int(line.split()[1].rstrip(':'))
            worry_d[mn] = {
                    'items': 0,
                    'op': '',
                    'test': '',
                    1: '',
                    0: '',
                    'n': 0
                    }
        elif 'items:' in line:
            items = deque([int(x) for x in line.split(':')[1].strip().split(',')])
            worry_d[mn]['items'] = items
        elif 'Operation' in line:
            worry_d[mn]['op'] = line.split('=')[1].lstrip()
        elif 'Test' in line:
            dn = line.split(':')[1].split()[-1]
            worry_d[mn]['test'] = f'new % {dn} == 0'
        elif 'If' in line:
            worry_d[mn]['true' in line] = int(line.split(':')[1].split()[-1])
    return worry_d

def monkey_round(monkeys, round, part=1):
    divide = 1
    for m in monkeys:
        divide *= int(monkeys[m]['test'].split()[2])

    for i in range(round):
        for m in monkeys:
            while monkeys[m]['items']:
                old = monkeys[m]['items'].popleft()
                new = eval(monkeys[m]['op'])
                monkeys[m]['n'] += 1
                if part:
                    new = new // 3
                else:
                    new = new % divide
                target = monkeys[m][eval(monkeys[m]['test'])]
                monkeys[target]['items'].append(new)
    return monkeys

def part_one(data):
    # do stuff
    worry_d = {}
    for monkey in data:
        worry_d = parse_monkey(monkey, worry_d)
    worry_d = monkey_round(worry_d, 2)
    almost = sorted([worry_d[i]['n'] for i in range(len(worry_d))])[-2:]
    return almost[0] * almost[1]
    
def part_two(data):
    # do stuff again
    worry_d = {}
    for monkey in data:
        worry_d = parse_monkey(monkey, worry_d)
    worry_d = monkey_round(worry_d, 10000, 2)
    almost = sorted([worry_d[i]['n'] for i in range(len(worry_d))])[-2:]
    return almost[0] * almost[1]

start = time.time()

data = get_data(False)
#output = part_one(data)
output = part_two(data)

stop = time.time()

print(f'Körning tog: {stop - start:.4f} sekunder\n{output}')

