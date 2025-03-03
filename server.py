import socket
import pyodbc
from notes import Note
from notes_manager import NoteManager

IP = '127.0.0.1'
PORT = 4000

class NoteManagerServer(NoteManager):
    def __init__(self, server="localhost\\SQLEXPRESS", database="db_notes"):
        super().__init__(server, database)

    def handle_request(self, request):
        action, *params = request.split(',')

        if action == "add_note":
            title = params[0]
            content = params[1]
            note = Note(self.next_id, title, content)
            self.save_note(note)
            return "Заметка добавлена"

        elif action == "get_note_by_id":
            note_id = int(params[0])
            note = self.find_note_by_id(note_id)
            if note:
                return f"ID: {note.id}\nЗаголовок: {note.title}\nТекст: {note.content}"
            return "Заметка не найдена"

        elif action == "get_all_notes":
            notes = self.get_all_notes()
            if notes:
                return "\n".join([f"ID: {note.id}\nЗаголовок: {note.title}\nТекст: {note.content}" for note in notes])
            return "Заметок нет"

        return "Неизвестная команда"


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print("Сервер запущен")

    manager = NoteManagerServer()
    manager.notes, manager.next_id = manager.load_notes()

    while True:
        client_socket, client_address = server.accept()
        print(f"Подключен клиент {client_address}")

        try:
            while True:
                data = client_socket.recv(1024).decode("utf-8")
                if not data:
                    print(f"Соединение с клиентом {client_address} закрыто.")
                    break
                print(f"Получено сообщение: {data}")
                response = manager.handle_request(data)
                client_socket.send(response.encode("utf-8"))
        except Exception as e:
            print(f"Ошибка при обработке запроса: {e}")
        finally:
            client_socket.close()

if __name__ == "__main__":
    start_server()
