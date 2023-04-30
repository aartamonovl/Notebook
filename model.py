import csv
import os.path as p
from list_notes import ListNotes
from notes import Note

class Model:
    # def __init__(self, path_csv):
    #     count_line=0
    #     try:
    #         with open(path_csv, "r", encoding="utf-8") as f1:
    #             aa = csv.reader(f1, delimiter=';')
    #             for line in aa:
    #                 ListNotes.add(Note(id = line[0], title = line[1], body=line[2]))
    #                 count_line += 1
    #             return ListNotes
    #     except:
    #         print("Ошибка при загрузке данных из базового csv файла.")
    #         exit(2)
    
    def __init__(self, path_csv):
        if p.isfile(path_csv):
            self.base_path = path_csv
            print("Базовый файл найден.")
        else:
            print("Базового файла по указанному пути нет.")
            exit(2)

    def load_notes(self):
        notes = ListNotes()
        count_line=0
        try:
            with open(self.base_path, "r", encoding="utf-8") as f1:
                aa = csv.reader(f1, delimiter=';')
                for line in aa:
                    notes.add(Note(id = line[0], title = line[1], body=line[2], create_date=line[3], change_date=line[4]))
                    count_line += 1
            print('Загружено {count_line} строк.')
            return notes
        except:
            print("Ошибка при загрузке данных из базового csv файла.")
            exit(2)

    def save_notes(self, notes_to_save: ListNotes):
        try:
            with open(self.base_path, "w", encoding="utf-8") as f1:
                f1.write(notes_to_save.get_CSV())
        except:
            print("Ошибка при записи в базовый csv файл.")
            exit(2)