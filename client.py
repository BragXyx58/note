import socket

IP = '127.0.0.1'
PORT = 4000

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, PORT))

    while True:
        print("\n1) Добавить заметку\n2) Найти по ID\n3) Вывести все заметки\n4) Выйти")
        action = input("Выберите действие: ")

        if action == "1":
            title = input("Введите заголовок: ")
            content = input("Введите текст: ")
            client.send(f"add_note,{title},{content}".encode("utf-8"))
            response = client.recv(1024).decode("utf-8")
            print(response)

        elif action == "2":
            note_id = input("Введите ID заметки: ")
            client.send(f"get_note_by_id,{note_id}".encode("utf-8"))
            response = client.recv(1024).decode("utf-8")
            print(response)

        elif action == "3":
            client.send("get_all_notes".encode("utf-8"))
            response = client.recv(1024).decode("utf-8")
            print(response)

        elif action == "4":
            client.send("exit".encode("utf-8"))
            print("Выход из клиента...")
            break

    client.close()

if __name__ == "__main__":
    start_client()
