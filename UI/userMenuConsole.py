def printMenuTitle(textMenu):
    print("=======================================")
    print("           ", textMenu)
    print("=======================================")


def printMenuLine():
    print("======================================")

def menu_console():
        printMenuTitle("ЖУРНАЛ ЗАМЕТОК")
        print("1 - Показать все заметки \n2 - Добавить заметку \n3 - Редактировать заметку\n4 - Удалить заметку"
              " \n5 - Поиск заметки по ID\n6 - Поиск заметки по дате\n7 - Выход")
        printMenuLine()
        print("\n выберите пункт из меню ")