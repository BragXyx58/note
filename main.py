from notes import Note
from notes_manager import NoteManager

manager = NoteManager()
manager.notes, manager.next_id = manager.load_notes()

while True:
    print("\n1) Добавить заметку\n2) Найти по ID\n3) Удалить по ID (! IN PROCCESS ! )\n4) Вывести все заметки\n5) Выйти")
    action = input("Выберите действие: ")

    if action == "1":
        title = input("Введите заголовок: ")
        content = input("Введите текст: ")
        note = Note(manager.next_id, title, content)
        manager.save_note(note)
        print("Заметка добавлена.")

    elif action == "2":
        try:
            note_id = int(input("Введите ID заметки: "))
            note = manager.find_note_by_id(note_id)
            if note:
                print(f"\nID: {note.id}\nЗаголовок: {note.title}\nТекст: {note.content}")
            else:
                print("Заметка не найдена.")
        except ValueError:
            print("Некорректный ID.")

    elif action == "3":
        print("! IN PROCCESS !")

    elif action == "4":
        notes = manager.get_all_notes()
        if notes:
            print("\nВсе заметки:")
            for note in notes:
                print(f"\nID: {note.id}\nЗаголовок: {note.title}\nТекст: {note.content}")
        else:
            print("Заметок нет.")

    elif action == "5":
        break
