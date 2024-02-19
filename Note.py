class Note:
    def __init__(self, note_id, date, title, text):
        self.note_id = note_id
        self.date = date
        self.title = title
        self.text = text
    def get_note_id(self):
        return self.note_id
    def set_note_id(self, id):
        self.note_id = id
    def get_date(self):
        return self.date
    def set_date(self, d):
        self.date = d
    def get_title(self):
        return self.title
    def set_title(self, t):
        self.title = t
    def get_text(self):
        return self.text
    def set_text(self, tt):
        self.text = tt
    def __str__(self):
        return f'\nЗаметка: {self.note_id}\nДата создания(редактирования):' \
               f' {self.date}\nЗаголовок: {self.title}\nСодержание: {self.text}\n '
    