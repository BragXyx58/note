import pyodbc
from notes import Note

class NoteManager:
    def __init__(self, server="localhost\\SQLEXPRESS", database="db_notes"):
        self.dsn = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"

    def save_note(self, note):
        try:
            conn = pyodbc.connect(self.dsn)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Notes ([TITLE], [TEXT]) VALUES (?, ?)", (note.title, note.content))
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Ошибка сохранения: {e}")

    def load_notes(self):
        notes = []
        next_id = 0
        try:
            conn = pyodbc.connect(self.dsn)
            cursor = conn.cursor()
            cursor.execute("SELECT ID, TITLE, TEXT FROM Notes")
            rows = cursor.fetchall()
            for row in rows:
                notes.append(Note(row[0], row[1], row[2]))
                next_id = max(next_id, row[0] + 1)
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Ошибка загрузки: {e}")
        return notes, next_id

    def get_all_notes(self):
        notes = []
        try:
            conn = pyodbc.connect(self.dsn)
            cursor = conn.cursor()
            cursor.execute("SELECT ID, TITLE, TEXT FROM Notes")
            rows = cursor.fetchall()
            for row in rows:
                notes.append(Note(row[0], row[1], row[2]))
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Ошибка загрузки заметок: {e}")
        return notes

    def find_note_by_id(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None
