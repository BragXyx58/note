from notes import Note
class NoteManager:
    def __init__(self):
        self.notes = []
        self.next_id = 0

    def add_note(self, title, content):
        note = Note(self.next_id, title, content)
        self.notes.append(note)
        self.next_id += 1

    def find_note_by_id(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.id != note_id]
