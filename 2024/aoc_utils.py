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

colors = [
    "\033[38;2;0;0;128m",     # Dark Blue
    "\033[38;2;0;32;160m",    # Deep Blue
    "\033[38;2;0;64;192m",    # Medium Blue
    "\033[38;2;0;128;255m",   # Light Blue
    "\033[38;2;64;192;255m",  # Cyan
    "\033[38;2;128;255;192m", # Aqua Green
    "\033[38;2;128;255;128m", # Light Green
    "\033[38;2;192;255;64m",  # Lime Green
    "\033[38;2;255;192;0m",   # Golden Yellow
    "\033[38;2;255;0;0m",     # Red
    "\033[0m"                 # reset
]

