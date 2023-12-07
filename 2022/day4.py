'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  RELEASE INFO  ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ day4.py ]   █
 █   [ Type ................................. Advent of Code 2022 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 06, 2022 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''
def compare_pairs(pairs):
    p1, p2 = pairs.split(',')
    ps1 = p1.split('-')
    ps2 = p2.split('-')
    if int(ps1[0]) <= int(ps2[0]) and int(ps1[1]) >= int(ps2[1]):
        return True
    elif int(ps2[0]) <= int(ps1[0]) and int(ps2[1]) >= int(ps1[1]):
        return True
    else:
        return False

def part_one():
    counted = 0
    for row in filedata:
        counted += compare_pairs(row)
    print(counted)

def overlap(pairs):
    p1, p2 = pairs.split(',')
    ps1 = p1.split('-')
    ps2 = p2.split('-')
    p1 = [x for x in range(int(ps1[0]), int(ps1[1])+1)]
    for i in range(int(ps2[0]), int(ps2[1])+1):
        if i in p1:
            return True
    return False

def part_two():
    counted = 0
    for row in filedata:
        counted += overlap(row)
    print(counted)

with open (r'./input/day4_input', 'r') as file:
    filedata = [line.strip() for line in file.readlines()]

# --- Part One ---
part_one()
part_two()

