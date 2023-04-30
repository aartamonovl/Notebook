import uuid
import datetime

class Note():
    def __init__(self, title, body, id='', create_date='', change_date=''):
        self.id = uuid.uuid4() if id == '' else id
        self.title = title
        self.body = body
        self.create_date = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S') if create_date=='' else create_date
        self.change_date = self.create_date if change_date=='' else change_date
        print("Создание успешно")
    
    def get_text_note(self):
        return f"| {self.id} | {self.title} | {self.body} | {self.create_date} | {self.change_date} |"

    def get_csv_format(self):
        return f"{self.id};{self.title};{self.body};{self.create_date};{self.change_date}"

    def get_id(self):
        return str(self.id)

    def get_title(self):
        return self.title
    
    def get_body(self):
        return self.body
    
    def get_create_date(self):
        return self.create_date
    
    def get_change_date(self):
        return self.change_date
    
    def get_tuple(self):
        return [self.id, self.title, self.body, self.create_date, self.change_date]
    
    def get_note_for_search(self):
        return f"{self.id} {self.title} {self.body} {self.create_date} {self.change_date}"

    def do_method(method):
        method()
    
    def set_title(self):
        while True:
            new_title = input("Введите новый заголовок >>> ")
            if new_title.lower() == self.title.lower():
                print("Вы ввели старый заголовок. Введите новый заголовок.")
            else:
                self.title = new_title
                self.set_change_date()
                print("Заголовок изменен успешно")
                break
    
    def set_dody(self):
        while True:
            new_body = input("Введите новый заголовок >>> ")
            if new_body.lower() == self.body.lower():
                print("Вы ввели старый текст заметки. Введите новый текст.")
            else:
                self.title = new_body
                self.set_change_date()
                print("Тело заметки изменено успешно")
                break

    def set_change_date(self):
        self.change_date = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        