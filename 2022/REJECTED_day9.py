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
import os

class Rope:
    def __init__(self, name, x, y):
        self.x = x
        self.y = y
        self.name = name
        self.child = 'none'

    def move(self, dir):
        if dir == 'R':
            self.x += 1
        elif dir == 'L':
            self.x -= 1
        elif dir == 'U':
            self.y += 1
        elif dir == 'D':
            self.y -= 1

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

class Knot(Rope):
    def __init__(self, name, x, y, head, lvl):
        Rope.__init__(self, name, x, y)
        self.head = head
        self.head.child = self
        self.history = []
        self.history.append((self.x, self.y))
        if lvl[0] < lvl[1]:
            self.child = Knot(f'knot{lvl[0]}',0,0,self,(lvl[0]+1, lvl[1]))
        else:
            self.child = 'none'

    def get_history(self):
        return set(self.history)

    def get_coords(self):
        return self.history

    def get_all_data(self):
        if self.child != 'none':
            self.child.get_all_data()
        print(f'Knot: {self.name}\tvnum: {len(set(self.history))}')

    def check_head(self):
        hx = self.head.get_x()
        hy = self.head.get_y()
        tx = self.x
        ty = self.y
        dist = abs(hx - tx) + abs(hy - ty)
        if hx == tx and dist >= 2:
            hy = hy - 1 if hy > ty else hy + 1
        elif hy == ty and dist >= 2:
            hx = hx - 1 if hx > tx else hx + 1
        elif dist > 2:
            if hx > tx:
                tx += 1
            elif hx < tx:
                tx -= 1
            ty = ty + 1 if hy > ty else ty - 1
        self.x = tx
        self.y = ty
        self.history.append((self.x, self.y))
        if self.child != 'none':
            self.child.check_head()

def get_data(ns: int = 0) -> list: 
    with open (f'.//input//day9_input{ns * "_small"}', 'r') as file:
        filedata = [line.strip() for line in file.readlines()]
    return filedata

def part_one(data):
    rope = Rope('Head',0,0)
    tail = Knot('knot1',0,0,rope,(2,10))
    for row in data:
        dir, v = row.split()
        v = int(v)
        for i in range(v):
            rope.move(dir)
            tail.check_head()
    tail.get_all_data()
    return len(tail.get_history())

def part_two():
    # do stuff again
    return

start = time.time()

data = get_data(False)
output = part_one(data)

stop = time.time()

print(f'Körning tog: {stop - start:.4f} sekunder\n{output}')

