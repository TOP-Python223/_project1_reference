"""Дополнительный модуль: глобальные переменные и константы."""

# импорт из стандартной библиотеки
from typing import Sequence
from numbers import Real


# глобальные переменные данных
STATS = {}
SAVES = {}

PLAYERS = ()

DIM = 3
RANGE = range(DIM)

TURNS = [[0]*DIM for _ in RANGE]


# глобальные переменные типов для аннотаций
Series = Sequence[Real | str]
Matrix = Sequence[Series]
TurnCoords = tuple[int, int]
Score = tuple[dict, dict]


# глобальные константы
APP_TITLE = 'Крестики-Нолики'
PROMPT = ' > '

BOT_NAME_EASY = '#1'
BOT_NAME_HARD = '#2'

TOKENS = ('X', 'O')
WEIGHTS = (1.5, 1)

COMMANDS = {
    'добавить нового игрока': ('player', 'новый', 'p', 'н'),
    'выбрать другого игрока': ('another', 'другой', 'a', 'д'),
    'начать новую партию': ('game', 'партия', 'g', 'п'),
    'загрузить партию': ('load', 'загрузка', 'l', 'з'),
    'отобразить статистику': ('stats', 'таблица', 's', 'т'),
    'изменить размер поля': ('dim', 'размер', 'd', 'р'),
    'показать справку': ('help', 'справка', 'h', 'с'),
    'включить режим обучения': ('training', 'обучение', 't', 'о'),
    'выйти из игры': ('quit', 'выход', 'q', 'в'),
}

TRAINING_MESSAGES = {

}
