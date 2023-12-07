'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  RELEASE INFO  ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ day9.py ]   █
 █   [ Type ................................. Advent of Code 2022 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 15, 2022 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''
import time

def get_data(ns: int = 0) -> list: 
    with open (f'.//input//day9_input{ns * "_small2"}', 'r') as file:
        filedata = [line.strip() for line in file.readlines()]
    return filedata

def move_knots(data, rope):
    moves = {"U": (0,1),
             "R": (1,0),
             "D": (0,-1),
             "L": (-1,0)
            }
    for row in data:
        dir, v = row.split()
        for i in range(int(v)):
            for knot in rope:
                if knot == 0: 
                    xy = rope[knot][-1]
                    move = moves[dir]
                    new_xy = tuple(map(sum, zip(xy, move)))
                    rope[knot].append(new_xy)
                else:
                    # get the last known coordinate of the preceeding knot
                    tx, ty = rope[knot-1][-1]
                    mx, my = rope[knot][-1]
                    delta = abs(tx - mx) + abs(ty - my)
                    if tx == mx and delta >= 2:
                        my = ty - 1 if ty > my else ty + 1
                    elif ty == my and delta >= 2:
                        mx = tx - 1 if tx > mx else tx + 1
                    elif delta > 2:
                        if tx > mx: mx = mx + 1
                        elif tx < mx: mx = mx - 1
                        my = my + 1 if ty > my else my - 1
                    rope[knot].append((mx, my))
    rl = len(rope)
    return len(set(rope[rl-1]))

def part_one(data, knots):
    # do stuff
    rope = {knot : [(0,0)] for knot in range(knots)}
    return move_knots(data, rope)

def part_two(data, knots):
    # do stuff again
    rope = {knot : [(0,0)] for knot in range(knots)}
    return move_knots(data, rope)

start = time.time()

data = get_data(False)
#output = part_one(data, 2)
output = part_two(data, 10)
stop = time.time()

print(f'Körning tog: {stop - start:.4f} sekunder\n{output}')

