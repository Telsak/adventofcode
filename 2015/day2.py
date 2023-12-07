'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  RELEASE INFO  ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ day2.py ]   █
 █   [ Type ................................................. WHATISTHIS ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Mar 01, 2000 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''

with open (r'./input/day2_input', 'r') as file:
    boxes = file.read().split('\n')

def total_sq_ft(l, w, h):
    paper =  [l*w, w*h, h*l]
    ribbon = 2 * min([l+w, l+h, w+h])
    bow = l * w * h
    return sum(paper) * 2 + min(paper), ribbon + bow

def unpack(boxes):
    feet = 0
    ribbon = 0
    for box in boxes:
        if len(box) > 0:
            dim = [int(x) for x in box.split('x')]
            nfeet, nribbon = total_sq_ft(dim[0], dim[1], dim[2])
            feet += nfeet
            ribbon += nribbon

    return feet, ribbon

feet, ribbon = unpack(boxes)
print(f'First:  The elves require {feet} square feet of paper')
print(f'Second: The elves require {ribbon} total feet of ribbon')
