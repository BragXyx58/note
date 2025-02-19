class Note:
    def __init__(self, title, content):
        self.id = str(len(title) + len(content))
        self.title = title
        self.content = content
