'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  RELEASE INFO  ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ day1.py ]   █
 █   [ Type ......................... advent of code 2015 puzzle - day 1 ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 02, 2022 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

with open (r'./input/day1_input', 'r') as file:
    floors = file.read()

def final_level(floors):
    return floors.count('(') - floors.count(')')

def basement_pos(floors):
    pos = 1
    z = 0
    for f in floors:
        z+= 1 if f == '(' else -1
        if z < 0:
            return pos
        pos += 1

print(f'First:  Santa ends up at floor {final_level(floors)}')
print(f'Second: Santa enters the basement at position {basement_pos(floors)}')

