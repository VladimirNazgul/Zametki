import Repository.loadFromFile as lF
import Repository.writeToFile as wF
import Repository.Note as Note


def add_note():
    title = input("Введите заголовок заметки:\n")
    body = input("Введите описание заметки:\n")
    note = Note.Note(title=title, body=body)
    array_notes = lF.read_file()
    for i in array_notes:
        if Note.Note.get_id(note) == Note.Note.get_id(i):
            Note.Note.set_id(note)
    array_notes.append(note)
    wF.write_file(array_notes, 'a')
    print("Заметка добавлена в журнал!")

def show(txt):
    array_notes = lF.read_file()

    if array_notes:
        if txt == "all":
            print("ЖУРНАЛ ЗАМЕТОК:")
            for i in array_notes:
                print(Note.Note.map_note(i))

        elif txt == "ID":
            for i in array_notes:
                print("ID: ", Note.Note.get_id(i))
            id = input("\nВведите id заметки: ")
            flag = True
            for i in array_notes:
                if id == Note.Note.get_id(i):
                    print(Note.Note.map_note(i))
                    flag = False
            if flag:
                print("Нет такого ID")

        elif txt == "date":
            date = input("Введите дату в формате: dd.mm.yyyy: ")
            flag = True
            for i in array_notes:
                date_note = str(Note.Note.get_date(i))
                if date == date_note[:10]:
                    print(Note.Note.map_note(i))
                    flag = False
            if flag:
                print("Нет такой даты")
        else:
            print("Журнал заметок пустой!")
def del_notes():
    id = input("Введите ID удаляемой заметки: ")
    array_notes = lF.read_file()
    flag = False

    for i in array_notes:
        if id == Note.Note.get_id(i):
            array_notes.remove(i)
            flag = True

    if flag:
        wF.write_file(array_notes, 'a')
        print("Заметка с id: ", id, " успешно удалена!")
    else:
        print("нет такого id")
