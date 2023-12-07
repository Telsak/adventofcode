'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  RELEASE INFO  ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ day2.py ]   █
 █   [ Type ................................. Advent of Code puzzle 2022 ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 02, 2022 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

with open ('./input/day2_input', 'r') as file:
    series = file.readlines()

table = {'A': (1, 'X', 'Y', 2),
         'B': (2, 'Y', 'Z', 3),
         'C': (3, 'Z', 'X', 1),
         'X': 1,
         'Y': 2,
         'Z': 3
        }

def lose(move, state):
    A = {'X': (0, 'Z'), 'Y': (3, 'X'), 'Z': (6, 'Y')}
    B = {'X': (0, 'X'), 'Y': (3, 'Y'), 'Z': (6, 'Z')}
    C = {'X': (0, 'Y'), 'Y': (3, 'Z'), 'Z': (6, 'X')}

    if move == 'A':
        score = A[state]
    elif move == 'B':
        score = B[state]
    else:
        score = C[state]
    return score[0] + table[score[1]]


game_sum = 0
for game in series:
    g = game.split()
    game_sum += lose(g[0], g[1])
    print(game_sum)
