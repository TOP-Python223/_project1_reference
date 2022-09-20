"""Дополнительный модуль: обработка дополнительных пользовательских команд."""

# импорт из стандартной библиотеки


# импорт дополнительных модулей
import data



def get_player_name() -> None:
    """Запрашивает имя игрока и проверяет присутствие этого имени в глобальной переменной статистики, добавляет имя в глобальную переменную текущих игроков."""
    # stdin -> name
    # if name not in data.STATS:
    #     new_player(name)
    # name -> data.PLAYERS


def new_player(player_name: str) -> None:
    """Создаёт запись о новом игроке в глобальной переменной статистики."""
    # data.STATS[player_name] = {'wins': 0, 'ties': 0, 'fails': 0, 'training': True}


def load() -> bool:
    """Выводит в stdout все сохранённые партии для текущего игрока, запрашивает партию для загрузки, настраивает глобальные переменные и возвращает True/False в зависимости от очерёдности хода."""
    # name = data.PLAYERS[0]
    # saves_found = False
    # for save in data.SAVES:
    #     if name in save:
    #         save -> stdout
    #         saves_found = True
    # if not saves_found:
    #     raise LookupError
    # stdin -> choice
    # data.SAVES[choice]['turns'] -> data.TURNS
    # choice -> data.PLAYERS
    # data.TURNS -> turns_amount
    # if turns_amount % 2 == 0:
    #     return False
    # else:
    #     return True


def change_dimension() -> None:
    """Запрашивает у пользователя новую размерность игрового поля и пересчитывает соответствующий диапазон."""
    # stdin -> data.DIM
    # data.DIM -> data.RANGE


def show_stats(table: bool = False) -> None:
    """В зависимости от логического ключа выводит либо персональную статистику активного игрока (table=False) либо таблицу со статистикой всех игроков (table=True)."""
    # if table:
    #     data.STATS -> stdout
    # else:
    #     data.STATS[data.PLAYERS[0]] -> stdout


def training_on() -> None:
    """Включает режим обучения для текущего активного игрока."""
    # data.STATS[data.PLAYERS[0]]['training'] = True



# тестирование функций модуля
if __name__ == '__main__':
    pass
