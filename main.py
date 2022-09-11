"""Модуль верхнего уровня для учебного проекта Крестики-Нолики."""

# импорт дополнительных модулей
import data
import help


# 2. ЕСЛИ первый запуск
#    1. Чтение из .ini файла
if data.read_ini():
    # вывод раздела помощи
    help.show_help()

# 3. Запрос имени игрока
data.get_player_name()

# суперцикл
while True:
    # 4. Ожидание ввода команды
    command = input(' > ').lower()

    if command in help.COMMANDS['выйти из игры']:
        break

    # elif command in help.COMMANDS['начать новую партию']:
        # 5. Запрос режима игры
        # ...

    # elif ... обработка других команд

data.save_ini()
