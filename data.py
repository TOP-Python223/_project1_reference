"""Дополнительный модуль: работа с данными и файлами данных."""

# импорт из стандартной библиотеки
from itertools import zip_longest
from pathlib import Path
from pprint import pprint
from sys import path
from configparser import ConfigParser


# глобальные переменные модуля
SCRIPT_DIR = Path(path[0])
players_path = SCRIPT_DIR / 'players.ini'
saves_path = SCRIPT_DIR / 'saves.ini'

STATS = {}
SAVES = {}

DIM = 3

PLAYERS = ()
TOKENS = ('X', 'O')


def read_ini() -> bool:
    """Читает из файлов данные и заполняет структуры данных."""
    players = ConfigParser()
    players.read(players_path)
    for player in players.sections():
        stats = players[player]
        STATS[player] = {
            k: int(v) if v.isdecimal() else stats.getboolean(k)
            for k, v in stats.items()
        }
    saves = ConfigParser()
    saves.read(saves_path)
    for players in saves.sections():
        save = saves[players]
        all_turns = [
            part.split(',')
            for part in save['turns'].split('|')
        ]
        turns = []
        for x, o in zip_longest(*all_turns):
            try:
                turns += [int(x), int(o)]
            except TypeError:
                turns += [int(x)]
        list_field = [0]*9
        for i in range(9):
            try:
                list_field[i] = turns.index(i) + 1
            except ValueError:
                list_field[i] = 0
        list_field = [
            [list_field[j] for j in range(i, i+3)]
            for i in range(0, 9, 3)
        ]
        SAVES[tuple(players.split(':'))] = list_field
    # первый ли запуск
    if STATS:
        return False
    else:
        return True


def save_ini():
    pass


def get_player_name():
    pass


if __name__ == '__main__':
    print(read_ini())
    print()
    pprint(STATS)
    print()
    pprint(SAVES)
    print()
