from notes import Note
class NoteSaver:
    def __init__(self, filename="notes.txt"):
        self.filename = filename

    def save_notes(self, notes):
        with open(self.filename, "w", encoding="utf-8") as file:
            for note in notes:
                file.write(f"{note.id}|||{note.title}|||{note.content}\n")

    def load_notes(self):
        notes = []
        next_id = 0
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split("|||")
                    if len(parts) == 3:
                        note = Note(int(parts[0]), parts[1], parts[2])
                        notes.append(note)
                        next_id = max(next_id, note.id + 1)
        except FileNotFoundError:
            pass
        return notes, next_id
