"""Модуль верхнего уровня для учебного проекта Крестики-Нолики."""

# импорт дополнительных модулей
import data
import functions
import help
import commands
import gameset
import game



functions.show_title(data.APP_TITLE, padding_vertical=True)

# 2. ЕСЛИ первый запуск
#    1. Чтение из .ini файла
if functions.read_ini():
    # вывод раздела помощи
    help.show_help()

# 3. Запрос имени игрока
commands.get_player_name()

# суперцикл
while True:
    # 4. Ожидание ввода команды
    command = input(data.PROMPT).lower()

    if command in data.COMMANDS['начать новую партию']:
        # 5. Запрос режима игры
        #    6. Запрос очерёдности хода (токена)
        gameset.game_mode()
        # 8. Цикл раунда:
        #    7. ЕСЛИ хотя бы у одного из игроков включен режим обучения
        result = game.game()
        if result is None:
            # 9. а) ЕСЛИ ввод пустой:
            #            ИСТИНА: запуск сохранения игры
            game.save_game()
        else:
            # 12. Обновление статистики игроков
            functions.update_stats(result)

    elif command in data.COMMANDS['загрузить партию']:
        try:
            # 13. Проверка наличия сохранённых партий для текущего игрока
            #     14. Запрос партии для загрузки
            # 7—12. Партия
            result = game.game(commands.load())
            if result is None:
                # 15. ЕСЛИ партия закончена досрочно:
                #          сохранение данных о партии
                game.save_game()
            else:
                # 16. Внесение изменений в статистику игрока(-ов)
                functions.update_stats(result)
                # 17. Удаление данных о доигранной сохранённой партии
                # ...
        except LookupError:
            print('no saved games for you')

    elif command in data.COMMANDS['выйти из игры']:
        # 18. Выход из суперцикла
        break

    # elif ... обработка других команд


# 19. Сохранение всех данных в .ini файлы
functions.save_ini()
