"""Дополнительный модуль: вспомогательные функции."""

# импорт из стандартной библиотеки
from pathlib import Path
from sys import path
from shutil import get_terminal_size as gts
from math import ceil, floor
from configparser import ConfigParser
from itertools import zip_longest
from pprint import pprint


# импорт дополнительных модулей
import data


# переменные модуля
script_dir = Path(path[0])
players_ini_path = script_dir / 'players.ini'
saves_ini_path = script_dir / 'saves.ini'



def show_title(title: str,
               *,
               padding_vertical: bool = False,
               center: bool = True,
               uppercase: bool = True) -> None:
    """Выводит в stdout заголовок в рамке."""
    terminal_width = gts()[0] - 1
    if center:
        # отступы при центрировании для чётного и нечётного значений ширины окна терминала
        padding_left = ceil((terminal_width - len(title) - 2) / 2)
        padding_right = floor((terminal_width - len(title) - 2) / 2)
    else:
        padding_left = 1
        padding_right = terminal_width - len(title) - padding_left - 2
    title = (title.capitalize(), title.upper())[uppercase]
    frame_char = ('+', '#')[padding_vertical]
    empty_line = (' '*(terminal_width - 2)).join(frame_char*2) + '\n'
    print(f'\n{frame_char*terminal_width}')
    print(('', empty_line)[padding_vertical], end='')
    print((' '*padding_left + title + ' '*padding_right).join(frame_char*2))
    print(('', empty_line)[padding_vertical], end='')
    print(f'{frame_char*terminal_width}\n')


def read_ini() -> bool:
    """Читает конфигурационные файлы, сохраняет прочитанные данные в глобальные переменные статистики и сохранений и возвращает True если приложение запущено впервые, иначе False."""
    players = ConfigParser()
    players.read(players_ini_path)
    # players.ini -> data.STATS
    for player in players.sections():
        stats = players[player]
        data.STATS[player] = {
            k: int(v) if v.isdecimal() else stats.getboolean(k)
            for k, v in stats.items()
        }
    saves = ConfigParser()
    saves.read(saves_ini_path)
    # saves.ini -> data.SAVES
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
        data.SAVES[tuple(players.split(':'))] = list_field
    # отсутствие сохранённых ранее имён игроков трактуем как первый запуск приложения
    if data.STATS:
        return False
    else:
        return True


def save_ini():
    """Записывает конфигурационные файлы, из глобальных переменных статистики и сохранений."""
    # data.STATS -> players.ini
    # data.SAVES -> saves.ini


def turns_to_board() -> data.Matrix:
    """Конвертирует матрицу ходов в матрицу с токенами."""
    board = [['']*data.DIM for _ in data.RANGE]
    for i in data.RANGE:
        for j in data.RANGE:
            if is_cross(data.TURNS[i][j]):
                board[i][j] = data.TOKENS[0]
            elif is_zero(data.TURNS[i][j]):
                board[i][j] = data.TOKENS[1]
    return board


def draw_boards(board: data.Matrix,
                *boards: data.Matrix,
                left_margin: int = 1,
                right: bool = False) -> str:
    """Возвращает в строковом виде одно или несколько игровых полей, расположенных на одном уровне, заполненных на основе переданных аргументами матриц."""
    boards = (board, ) + boards
    num_of_boards = len(boards)
    # для каждой матрицы вычисляет наибольшее количество символов в ячейке
    width_cells = tuple(max(max(len(str(cell)) for cell in row) for row in board) + 2
                        for board in boards)
    # для каждой матрицы вычисляет количество символов, занимаемое всей матрицей в ширину
    width_boards = tuple(width_cells[i]*data.DIM + data.DIM - 1
                         for i in range(num_of_boards))
    pad = 5
    margin = (left_margin, gts()[0] - 1 - sum(width_boards) - pad * (num_of_boards - 1))[right]
    # формирует строки со значениями и вертикальными разделителями
    value_lines = ()
    for i in data.RANGE:
        # записывает в кортеж строки значений из каждой переданной матрицы
        values = ('|'.join(f"{cell!s:^{width_cells[j]}s}" for cell in boards[j][i])
                  for j in range(num_of_boards))
        # формирует полную строку с отступами слева и между строками значений
        value_lines += (' '*margin + (' '*pad).join(values), )
    # формирует строку с горизонтальными разделителями матриц и отступами слева и между ними
    horiz_line = ' '*margin + (' '*pad).join('—'*wd for wd in width_boards)
    return f'\n{horiz_line}\n'.join(value_lines)


def is_cross(turn_number: int) -> bool:
    """Возвращает True если номер хода соответствует ходу крестика, иначе False."""
    return turn_number % 2 != 0


def is_zero(turn_number: int) -> bool:
    """Возвращает True если номер хода соответствует ходу нолика и не равен нолю, иначе False."""
    return turn_number != 0 and turn_number % 2 == 0


def update_stats(score: data.Score) -> None:
    """Обновляет глобальную переменную статистики в соответствии с результатом завершённой партии."""
    # for i in range(2):
    #     score[i] -> data.STATS[PLAYERS[i]]



# тестирование функций модуля
if __name__ == '__main__':
    print(read_ini(), end='\n\n')
    pprint(data.STATS)
    print()
    pprint(data.SAVES)
    print()
