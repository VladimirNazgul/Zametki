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


