import UI.userMenuConsole as ui
import Controller.commands as com


def start():
    while True:
        ui.menu_console()
        user_input = input()
        if user_input == '1':
            com.show("all")
        elif user_input == '2':
            com.add_note()
        elif user_input == '3':
            com.show("all")
            com.change_note()
        elif user_input == '4':
            com.show("all")
            com.del_notes()
        elif user_input == '5':
            com.show("ID")
        elif user_input == '6':
            com.show("date")
        else:
            print("Программа Журнал заметок завершена")
            break
