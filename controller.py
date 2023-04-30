from Menu import Menu
from model import Model
from list_notes import ListNotes
from notes import Note
import csv

class Controller:

    notes: ListNotes
    model: Model
    note: Note

    def __init__(self, model):
        self.model = model
        self.notes = self.model.load_notes()           
            
    def start(self):
        """
        Старт
        """
        menuitems = [
            (1, "Показать все заметки", self.view_all),
            (2, "Добавить заметку", self.add_note),
            (3, "Удалить заметку", self.del_notes_dialog),
            (4, "Поиск заметки", self.search_notes_dialog),
            (5, "Изменение заметки", self.change_note),
            (6, "Экспорт", self.export_notes),
            (7, "Импорт", self.import_notes),
            (8, "Сохранить изменения", self.save_force),
            (0, "Выход", self.exit_notes)]
        mainmenu = Menu(menuitems)
        mainmenu.prefixtext = "Главное меню\n"
        mainmenu.run()

    def change_note(self):
        """
        Изменение заметки
        """
        result = self.search_by_title_for_change()
        for note in result:
            print(note.get_text_note())
            choise = input("Хотите изменить эту записку? (Y/N)")
            if choise == 'Y':
                self.change_field_note(note)

    def change_field_note(self, note: Note):
        ch = input("Выберите поле для изменения (Заголовок - T, тело - B)")
        if ch == 'T':
            note.set_title()
        else:
            note.set_dody()

    def view_all(self): 
        res = self.notes.get_all_notes()
        for note in res:
            print(note.get_text_note())

    def add_note(self):
        """
        добавление заметки
        """
        print("Добавление заметки.")
        ready = 'N'
        while ready=='N':
            title = input("Введите заголовок (для отмены оставьте пустым) >>> ")
            if title == "": return
            body = input("Введите текст(для отмены оставьте пустым) >>> ")
            if body == "": return
            note = Note(title, body)
            print("Ваша заметка:\n")
            print(note.get_text_note())
            ready = input("Проверьте заметку и если все хорошо, введите Y >>> ")
        self.notes.add(note)
        print("Сохранение успешно.")


    def del_notes_dialog(self):
        """
        диалог удаления записей 
        """
        text = input("Укажите ID или фрагмент текста для удаления заметки\n(пусто для отмены): ")
        if text == '':
            return
        self.del_by_text(text)
        return
    
    def del_by_text(self, text):
        """удаление записей по текстовому запросу
        """
        result = []
        for id, record in self.notes.get_dict().items():
            if record.get_note_for_search().lower().find(text.lower()) != -1:
                result.append(id)
        if len(result) == 0:
            print('нет записей для удаления')
            return
            
        print('будет удалено', len(result), 'записей')
        res = self.notes.get_by_id_list(result)
        for note in res:
            print(note.get_text_note())

        while True:
            response = input('Удаляем?(Y/N):')
            if response.upper() == 'N':
                return
            if response.upper() == 'Y':
                for id in result:
                    self.notes.del_by_id(id)
                return
    
    def search_notes_dialog(self):
        menuitems = [
            (1, "Id", self.search_by_id),
            (2, "Любое другое поле", self.search_by_title),
            (0, "Назад в главное меню", -1)]
        export_menu = Menu(menuitems)
        export_menu.prefixtext = "\nПоле для поиска\n"
        export_menu.run(pause=True)

    def search_by_id(self):
        data = input("Введите Id для поиска >>> ")
        res = self.notes.get_by_id(data)
        print(res.get_text_note())
    
    def search_by_title_for_change(self):
        while True:
            text = input('Строка поиска (пусто для выхода): ')
            if text == '':
                return
            result = self.notes.get_by_title(text.lower())
            if len(result) == 0:
                print("ничего не найдено")
            else:
                return result
            


    def search_by_title(self):
        while True:
            text = input('Строка поиска (пусто для выхода): ')
            if text == '':
                return
            result = self.notes.get_by_title(text.lower())
            if len(result) == 0:
                print("ничего не найдено")
            else:
                print('найдено {} записей'.format(len(result)))
                for note in result:
                    print(note.get_text_note())
            print()

    def import_notes(self):
        menuitems = [
            (1, "Импорт из в CSV", self.import_from_CSV),
            (0, "Назад в главное меню", -1)]
        export_menu = Menu(menuitems)
        export_menu.prefixtext = "\nИмпорт\n"
        export_menu.run(pause=False)
    
    def import_from_CSV(self):
        """загрузка из CSV
        """
        fname = input("Укажите имя CSV файла(пусто для отмены): ")
        if fname == '':
            return
        count=self.load_from_CSV(fname)
        print('загружено {} записей'.format(count))
        self.delay()

    def load_from_CSV(self,fname)->int:
        """загрузка данных из CSV
        """
        count_line=0
        try:
            with open(fname+".csv", "r", encoding="utf-8") as f1:
                aa = csv.reader(f1, delimiter=';')
                for line in aa:
                    self.notes.add(Note(id = line[0], title = line[1], body=line[2], create_date=line[3], change_date=line[4]))
                    count_line += 1
            print('Загружено {count_line} строк.')
            return count_line
        except:
            print("Ошибка при загрузке данных из csv файла.")
            exit(2)

    def save_force(self):
        self.model.save_notes(self.notes)

    def exit_notes(self):
        self.model.save_notes(self.notes)
        exit(0)

    def save_notes_csv(self, file_name, note):
        with open(file_name, "+a", encoding ="utf-8") as file_csv:
            file_csv.write(note.get_csv())

    def export_to_CSV_interact(self):
        """
        экспорт в CSV
        """
        file_name = input("Укажите имя CSV файла(не может быть пустым): ")
        if file_name == '':
            return
        self.save_to_CSV(file_name)

    def save_to_CSV(self, filename):
        """
        запись данных в CSV
        """
        content = self.notes.get_CSV()
        with open(filename+".csv", "w", encoding="utf-8") as fl:
            fl.write(content)

    def export_notes(self):
        """экспорт заметок
        """
        menuitems = [
            (1, "Экспорт в CSV", self.export_to_CSV_interact),
            (0, "Назад в главное меню", -1)]
        export_menu = Menu(menuitems)
        export_menu.prefixtext = "\nЭкспорт\n"
        export_menu.run(pause=False)

    def delay(self,clrscr=True):
        input("Ввод для продолжения...")
        if clrscr: Menu.clrscr()