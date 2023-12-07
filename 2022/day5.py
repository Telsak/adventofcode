'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  RELEASE INFO  ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ day5.py ]   █
 █   [ Type ................................. Advent of Code 2022 puzzle ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 07, 2022 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

def setup_stacks(stacks):
    snum = int(stacks[-1].split()[-1])
    stackdata = []
    for i in range(snum+1):
        stackdata.append([])
    for line in stacks[:-1]:
        for i in range(1, snum * 4, 4):
            if line[i] != ' ':
                x = i if i == 1 else (i // 4) + 1
                stackdata[x].insert(0, line[i])
    return stackdata

def stack_moves(stacks, crates, src, dst):
    # moves one crate at a time, by popping it off the stack
    for i in range(crates):
        stacks[dst].append(stacks[src].pop())
    return

def stack_lifts(stacks, crates, src, dst):
    # moves one big section at a time, retaining the order
    i = len(stacks[src])-crates
    stacks[dst] += stacks[src][i:]
    del stacks[src][i:]

def part_one(data):
    for index in range(len(data)):
        if 'move' in data[index]:
            break
    stacks = data[:index-1]
    moves = data[index:]
    stacks = setup_stacks(stacks)
    for move in moves:
        move = move.split()
        stack_moves(stacks, int(move[1]), int(move[3]), int(move[5]))

    for stack in stacks:
        if len(stack) > 0:
            print(stack[-1], end='')
    print()
    return


def part_two(data):
    for index in range(len(data)):
        if 'move' in data[index]:
            break
    stacks = data[:index-1]
    moves = data[index:]
    stacks = setup_stacks(stacks)
    for move in moves:
        move = move.split()
        stack_lifts(stacks, int(move[1]), int(move[3]), int(move[5]))

    for stack in stacks:
        if len(stack) > 0:
            print(stack[-1], end='')
    print()
    return

with open (r'./input/day5_input', 'r') as file:
    filedata = [line.replace('\n', '') for line in file.readlines()]

#part_one(filedata)
part_two(filedata)
