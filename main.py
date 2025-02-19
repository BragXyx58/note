from notes import Note
from notes_manager import NoteManager

manager = NoteManager()


while True:
    print("\n1) Добавить заметку\n2) Найти по ID\n3) Удалить по ID\n4) Выйти")
    action = input("Выберите действие: ")

    if action == "1":
        title = input("Введите заголовок: ")
        content = input("Введите текст: ")
        manager.add_note(title, content)
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
            print("Заметка удалена.")
        except ValueError:
            print("Некорректный ID.")

    elif action == "4":
        break
