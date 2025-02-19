from notes import Note
from notes_manager import NoteManager
from notes_saver import NoteSaver

manager = NoteManager()
saver = NoteSaver()
manager.notes, manager.next_id = saver.load_notes()

while True:
    print("\n1) Добавить заметку\n2) Найти по ID\n3) Удалить по ID\n4) Выйти")
    action = input("Выберите действие: ")

    if action == "1":
        title = input("Введите заголовок: ")
        content = input("Введите текст: ")
        manager.add_note(title, content)
        saver.save_notes(manager.notes)
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
        try:
            note_id = int(input("Введите ID заметки для удаления: "))
            manager.delete_note(note_id)
            saver.save_notes(manager.notes)
            print("Заметка удалена.")
        except ValueError:
            print("Некорректный ID.")

    elif action == "4":
        break
