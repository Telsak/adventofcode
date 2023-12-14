'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  SCRIPT INFO   ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ day7.py ]   █
 █   [ Type ................................. Advent of Code 2023 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 14, 2023 ]             █
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

def categorize_hand(hand):
    hand_set = set([_ for _ in hand])
    cards = [hand.count(card) for card in hand_set]
    if 5 in cards:
        return 'five of a kind'
    elif 4 in cards:
        return 'four of a kind'
    elif 3 in cards:
        if 2 not in cards:
            return 'three of a kind'
        else:
            return 'full house'
    elif 2 in cards:
        one_two = ["one ", "two "][int(cards.count(2) == 2)]
        return f'{one_two}pair'
    return 'high card'

def tally_winnings(hands_list, offset=1):
    winnings = 0
    if len(hands_list) < 1:
        return 0
    for i, hand in enumerate(hands_list):
        winnings += (hands_list[i][1] * (i + offset))
    return winnings

def part_one(indata):
    # do stuff
    hands = {
            'five of a kind': [],
            'four of a kind': [],
            'full house': [],
            'three of a kind': [],
            'two pair': [],
            'one pair': [],
            'high card': [],
        }
    char_map = ['AKQJT', 'EDCBA']

    for line in indata:
        hand, winning = line.split()
        hand = hand.translate(str.maketrans(char_map[0], char_map[1]))
        hands[categorize_hand(hand)] += [(hand, int(winning))]
    for category, hand_series in hands.items():
        hands[category] = sorted(hand_series)

    total_winnings, offset = 0, 1
    categories = ['high card', 'one pair', 'two pair', 'three of a kind', 
            'full house', 'four of a kind', 'five of a kind']
    for i, category in enumerate(categories):
        if i != 0:
            offset += len(hands[categories[i-1]])
        total_winnings += tally_winnings(hands[category], offset)
    return total_winnings

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

