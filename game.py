"""Дополнительный модуль: обработка игрового процесса."""

# импорт дополнительных модулей
import data
import functions
import bot



def game(zero_turn=False) -> data.Score | None:
    """Управляет игровым процессом для каждой новой или загруженной партии."""
    # training = is_first_game()
    # for i in range(2):
    #     if zero_turn:
    #         continue
    #     if training:
    #         data.TRAINING_MESSAGES['...'] -> stdout
    #     if name in (data.BOT_NAME_EASY, data.BOT_NAME_HARD):
    #         bot.bot_turn(i, training) -> data.TURNS
    #     else:
    #         human_turn(training) -> inp
    #         if inp:
    #             inp -> data.TURNS
    #         else:
    #             return None
    #     functions.draw_boards(functions.turns_to_board()) -> stdout
    #     check_win_or_tie() -> win, tie
    #     if win:
    #         functions.show_title(f'победил игрок {data.PLAYERS[i]}')
    #         return -> ({...}, {...})
    #     if tie:
    #         functions.show_title('ничья')
    #         return -> ({...}, {...})


def is_first_game() -> bool:
    """Проверяет является ли данная партия первой для любого из игроков."""
    # for name in data.PLAYERS:
    #     if data.STATS[name]['training']:
    #         return True
    # else:
    #     return False


def human_turn(training: bool = False) -> data.TurnCoords:
    """Запрос координат ячейки поля для текущего хода."""
    # if training:
        # data.TRAINING_MESSAGES['ход игрока'] -> stdout
    # while True:
    #     stdin -> turn_coords
    #     if turn_coords ... :
    #         return turn_coords
    #     else:
    #         data.TRAINING_MESSAGES['неверный ввод хода'] -> stdout


def bot_turn(token_index: int, training: bool = False) -> data.TurnCoords:
    """Возвращает координаты ячейки поля для текущего хода бота в зависимости от сложности."""
    # if training:
        # data.TRAINING_MESSAGES['ход бота'] -> stdout
    # if data.BOT_NAME_EASY in data.PLAYERS:
        # bot.easy()
    # elif data.BOT_NAME_HARD in data.PLAYERS:
        # bot.hard(token_index)


def check_win_or_tie() -> tuple[bool, bool]:
    """Возвращает кортеж из двух логических значений (есть_победа, есть_ничья)."""
    def check_win() -> bool:
        """Проверяет глобальную переменную сделанных ходов на наличие любой победной комбинации."""
        rows = functions.turns_to_board()
        # транспонированная матрица поля: для упрощения перебора — столбцы прямой матрицы станут строками в транспонированной
        columns = [[rows[j][i] for j in data.RANGE] for i in data.RANGE]
        # список из главной и побочной диагоналей
        diagonals = (
            [rows[i][i] for i in data.RANGE],
            [rows[i][data.DIM-i-1] for i in data.RANGE]
        )
        # перебираем прямую, транспонированную матрицы и диагонали
        for matrix in (rows, columns, diagonals):
            # есть ли ряд, целиком заполненный только одним символом
            if 1 in [len(set(row)) for row in matrix if all(row)]:
                # локальную функцию делали, чтобы не выполнять дальнейшие проверки после того, как будет найдена первая победная комбинация
                return True
        else:
            return False
    # нет пустых  победа  ничья
    #   False     False   False
    #   False     True    False
    #   True      False   True
    #   True      True    False
    win = check_win()
    return win, all([all(row) for row in data.TURNS]) and not win


def save_game() -> None:
    """Обновляет глобальную переменную сохранений в соответствии с текущим состоянием глобальных переменных текущих игроков и сделанных ходов."""
    # data.PLAYERS -> players_str
    # TURNS -> turns_str
    # turns_str -> data.SAVES[players_str]



# тестирование функций модуля
if __name__ == '__main__':
    data.TURNS = [[6, 5, 1], [0, 2, 3], [0, 0, 4]]
    print(functions.draw_boards(
        data.TURNS,
        functions.turns_to_board(),
        right=True
    ))
    win, tie = check_win_or_tie()
    print(f'{win = }\n{tie = }')
