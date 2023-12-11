'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ day4.py ]   █
 █   [ Type ................................. Advent of Code 2023 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 11, 2023 ]             █
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
    
def check_card(card):
    id, card = card.split(':')
    winners, mine = card.split('|')
    return id.split()[1], winners.split(), mine.split()

def tally_points(winning_numbers, drawn_numbers):
    points = 0
    luck = [n for n in drawn_numbers if n in winning_numbers]
    if len(luck) > 0:
        for n in luck:
            if points == 0:
                points += 1
            else:
                points *= 2
    return points


def part_one(indata):
    # do stuff
    won_points = 0
    for card in indata:
        id, winners, mine = check_card(card)
        won_points += tally_points(winners, mine)
    return won_points

def part_two():
    # do stuff again
    return

start = time.time()

data = get_data()
output = part_one(data)
#output = part_two(data)

stop = time.time()

print(f'Körning tog: {stop - start:.4f} sekunder\n{output}')

