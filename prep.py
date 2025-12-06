'''
   ╒══════════════════╕ ╓─ ──── ─ ──══── ─ ────── ─ ────── ─ ──══── ─ ──── ─┐ 
 ┌─┤▌  RELEASE INFO  ▐├─╜ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ └┐
 █ ╘══════════════════╛                                                      █
 █   [ Filename ................................................ prep.py ]   █
 █   [ Type ..................................... AoC new day prepscript ]   █
 █                                                                           █
 █             [ Written by ........................... telsak ]             █
 █             [ Created date ................... Dec 05, 2025 ]             █
 █             [ Updated date ................... Dec 06, 2025 ]             █
 └┐ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ┌┘
  └ ──── ─ ──══── ─ ────── ─ ───── ─ ──══── ─ ──── ─ ────── ─ ──══── ─ ──── ┘
'''
import requests
import sys, time
from datetime import datetime
from pathlib import Path
from bs4 import BeautifulSoup as bs

def get_user_cookie():
    try:
      credentials = Path.home() / '.config' / 'script-creds' / 'aoc.crd'
      if credentials.is_file() and credentials.stat().st_size > 10:
        k, v = credentials.read_text().strip().split('=', 1)
        cookie = {k: v}
        return cookie
      else:
        raise FileNotFoundError
    except Exception:
      print('No session cookie!\Cannot access Advent of Code without it!')
      sys.exit()

def get_input_files(date, aoc_dir):
  # Takes a datetime.now() object as input
  # returns True/False based on file presence
  day, year = date.day, date.year
  input_dir = aoc_dir / str(year) / 'input'
  dayfile = input_dir / f'day{int(day):02}_input'

  if not dayfile.is_file():
    # try to acquire it
    try:
      print('trying to download input')
      aoc_url = f'https://adventofcode.com/{year}/day/{day}/input'
      cookie = get_user_cookie()
      response = requests.get(aoc_url, cookies=cookie)
      response.raise_for_status()
      print('input download successful')
      with dayfile.open('w', encoding='utf-8') as f:
        f.write(response.text)
        print('input write successful')
      return True
    except requests.exceptions.HTTPError as e:
      raise SystemExit(e)

  else:
    print('File exists, aborting download.')
    return True

def get_todays_puzzle_title(date):
  # takes a datime.now() object as input
  # returns the title of the puzzle, duh.
  day, year = 5, date.year
  try:
    print('trying to get puzzle page')
    aoc_url = f'https://adventofcode.com/{year}/day/{day}'
    cookie = get_user_cookie()
    response = requests.get(aoc_url, cookies=cookie)
    response.raise_for_status()

    soup = bs(response.text, 'lxml')
    day_desc = soup.find('article', class_='day-desc').h2.get_text()
    day_desc = day_desc[4:-4]
    return day_desc
  except requests.exceptions.HTTPError as e:
    raise SystemExit(e)

def populate_template_for_day(date, title, aoc_dir):
  # basically we already have a template file that is a source in the
  # aoc/ base dir. This is softlinked to by the aoc/yr/ templates
  # so just read in the template file, modify inline, dump the result
  # into the new daily file.
  day, year = str(date.day), str(date.year)
  template = aoc_dir / 'template.py'
  code_file = aoc_dir / year / f'day{int(day):02}.py'

  with template.open('r', encoding='utf-8') as f:
    template = f.readlines()

  for i, line in enumerate(template):
    if 'https' in line:
      template[i] = line.replace('YYYY', year)
      if len(day) < 2:
        nd = f'{day} '
      else:
        nd = day
      template[i] = template[i].replace('DD', nd)
    elif '.py' in line:
      template[i] = line.replace('DD', f'{int(day):02}')
    elif 'Puzzle title' in line:
      tlen = len(title)
      pf = ' █   '
      sf = '█'
      title = pf + title; tlen = len(title)
      template[i] = f'{title}{(77 - tlen) * " "}{sf}\n'
    elif 'Created date' in line:
      date_str = f' Dec {day}, {year} ]             █\n'
      pf = ' █             [ Created date '
      rem = 79 - len(pf) - len(date_str)
      template[i] = f'{pf}{"." * rem}{date_str}'
    elif 'YYYY' in line:
      template[i] = line.replace('YYYY', year)

  with code_file.open('w', encoding='utf-8') as f:
    f.writelines(template)

#------------------------------------------------------------------------------
aoc_dir = Path.home() / 'programming' / 'python' / 'adventofcode'

day_input_exists = get_input_files(datetime.now(), aoc_dir)

time.sleep(15)

title = get_todays_puzzle_title(datetime.now())
populate_template_for_day(datetime.now(), title, aoc_dir)

print('Done')
#------------------------------------------------------------------------------

