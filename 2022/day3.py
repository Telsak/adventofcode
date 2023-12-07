'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  RELEASE INFO  ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ day3.py ]   █
 █   [ Type ................................. Advent of code 2022 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 03, 2022 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''
from string import ascii_uppercase as UP

with open (r'./input/day3_input', 'r') as file:
    rs = [row.strip() for row in file.readlines()]

def rucksack_to_priority(letter):
    return ord(letter)-38 if letter in UP else ord(letter)-96

def get_priority(rucksacks):
    psum = 0
    for rucksack in rucksacks:
        comp_len = len(rucksack)//2
        cp1 = rucksack[:comp_len]
        cp2 = rucksack[comp_len:]
        for item in cp1:
            if cp2.count(item) > 0:
                psum += rucksack_to_priority(item)
                break
    return psum

def find_intersection(rucksacks):
    badgesum = 0
    for i in range(0, len(rs), 3):
        rs_s1 = set(rs[i])
        rs_s2 = set(rs[i+1])
        rs_s3 = set(rs[i+2])
        rs_is = set.intersection(rs_s1, rs_s2, rs_s3)
        if len([1 for i in rs_is]) == 1: 
            badgesum += rucksack_to_priority(rs_is.pop())
    return badgesum

# --- Part One ---
print(get_priority(rs))

# --- Part Two ---
print(find_intersection(rs))

