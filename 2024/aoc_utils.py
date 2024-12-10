'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  RELEASE INFO  ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ........................................... aoc_utils.py ]   █
 █   [ Type ......................... Support module for smarter AOC use ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 10, 2024 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''
import sys

def get_data_f(ns=0, mode='lines'):
  '''Imports the puzzle data either as \n separated lines or a 2D array'''
  day_file = sys.argv[0].split('.')[0] 
  with open (f'.//input//{day_file}_input{ns * "_small"}', 'r') as file:
    if 'grid' in mode:
      filedata = [[x for x in line.strip()] for line in file.readlines()]
    elif 'lines' in mode:
      filedata = [line.strip() for line in file.readlines()]
  return filedata



