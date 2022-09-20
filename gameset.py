"""Дополнительный модуль: подготовка партии."""

# импорт из стандартной библиотеки


# импорт дополнительных модулей
import data



def game_mode() -> None:
    """Запрашивает режим для новой партии, при необходимости выполняет запросы уровня сложности или имени второго игрока, выполняет запрос очерёдности ходов."""
    # stdin -> mode
    # if mode == 'single':
    #     get_difficulty_level()
    # elif mode == 'double':
    #     get_player_name()
    # get_turn_order()


def get_difficulty_level() -> None:
    """Запрашивает уровень сложности для режима игры с ботом, добавляет имя бота в глобальную переменную текущих игроков."""
    # stdin -> level
    # if level == 'easy':
    #     data.BOT_NAME_EASY -> data.PLAYERS
    # elif level == 'hard':
    #     data.BOT_NAME_HARD -> data.PLAYERS


def get_turn_order() -> None:
    """Запрашивает текущего активного игрока о его выборе токена для партии, при необходимости меняет порядок имён в глобальной переменной текущих игроков."""
    # stdin -> token
    # if token == 'X':
    #     pass
    # elif token == 'O':
    #     data.PLAYERS = data.PLAYERS[::-1]



# тестирование функций модуля
if __name__ == '__main__':
    pass
