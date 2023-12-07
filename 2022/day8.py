'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  RELEASE INFO  ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ day8.py ]   █
 █   [ Type ................................. Advent of Code 2022 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 14, 2022 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''
import time
import sys 

def get_data(ns=0):
    with open (f'.//input//day8_input{ns * "_small"}', 'r') as file:
        filedata = [line.strip() for line in file.readlines()]
    return filedata

def check_tree_row(row, i):
    # find out if any other index is higher or equal to row[i]
    return max(list(row[0:i])) < row[i] or max(list(row[i+1:])) < row[i]

def check_score(row, i):
    score = 1
    rl = row[0:i][::-1]
    rr = row[i+1:]
    for var in [rl, rr]:
        for x in range(len(var)):
            if row[i] <= var[x] or x == (len(var)-1):
                score *= (x+1)
                break
    return score

def part_one(data):
    trees = 0
    for ri, row in enumerate(data):
        for ci, col in enumerate(row):
            if not (ri == 0 or ri == len(data)-1 or ci == 0 or ci == len(data)-1):
                if check_tree_row(row, ci):
                    trees += 1
                else:
                    trees += check_tree_row([row[ci] for row in data], ri)
    trees += (len(data) * 2) + (len(row) * 2) - 4
    return trees

def part_two(data):
    # do stuff again
    scenic_scores = []
    for ri, row in enumerate(data):
        for ci, col in enumerate(row):
            # ignore edge trees, they have atleast 1 distance of 0 and we get
            # the score by multiplication, thus 0*n*n1*n2.. == 0
            scenic = 1
            if not (ri == 0 or ri == len(data)-1 or ci == 0 or ci == len(data)-1):
                scenic *= check_score(row, ci)
                scenic *= check_score([row[ci] for row in data], ri)
                scenic_scores.append(scenic)
    return max(scenic_scores)

start = time.time()

filedata = get_data()

#output = part_one(filedata)
output = part_two(filedata)

stop = time.time()
print(f'Körning tog: {stop - start:.4f} sekunder\n{output}')
