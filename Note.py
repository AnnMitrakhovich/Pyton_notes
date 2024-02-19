class Note(object):
    def __init__(self, note_id, date, title, text):
        self._note_id = note_id
        self._date = date
        self._title = title
        self._text = text
    def get_note_id(self):
        return self._note_id
    def set_note_id(self, id):
        self._note_id = id
    def get_date(self):
        return self._date
    def set_date(self, d):
        self._date = d
    def get_title(self):
        return self._title
    def set_title(self, t):
        self._title = t
    def get_text(self):
        return self._text
    def set_text(self, tt):
        self._text = tt
    def __str__(self):
        return f'\nЗаметка: {self._note_id}\nДата создания(редактирования):' \
               f' {self._date}\nЗаголовок: {self._title}\nСодержание: {self._text}\n '
    