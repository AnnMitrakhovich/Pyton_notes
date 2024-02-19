class View:
    def greeting(self):
        print("Вас приветствует приложение для управления личными заметками!")
    @staticmethod
    def show_number_point_list(notes):
        for note in notes:
            print("*****")
            print(note)
            print("*****")
    
    @staticmethod
    def show_note(note):
        print(note)
    
    @staticmethod
    def show_empty_list_message():
        print('Cписок пуст!')

    @staticmethod
    def display_note_id_not_exist(note_id):
        print('Заметка {} не найдена!'.format(note_id))

    @staticmethod
    def display_note_id_exist(note_id):
        print('Заметка с номером: {} уже существует!'.format(note_id))

    @staticmethod
    def display_note_stored():
        print('Заметка добавлена в список заметок.')
    
    @staticmethod
    def display_note_updated(note_id):
        print('Заметка с номером:{} обновлена успешно!'.format(note_id))

    @staticmethod
    def display_note_deletion(note_id):
        print('*****')
        print('Удаление заметки с номером: {} выполнено успешно!'.format(note_id))

    @staticmethod
    def display_all_notes_delete():
        print('Все заметки удалены!')
        print('*****')

    def display_note_id_not_exist(search_id):
        return search_id