from copy import copy
from notes import Note

class ListNotes:
    listNotes = {}

    def __init__(self):
        self.clean()

    def get_dict(self):
        return copy(self.listNotes)
    
    def add(self, note: Note):
        self.listNotes[note.get_id()] = note

    def clean(self):
        self.listNotes = {}

    def get_listRecords_text(self, method, text) -> list:
        result = []
        for note in self.listNotes.values():
            if note.do_method(method).lower().find(text) != -1:
                result.append(note)
        return result
    
    def del_by_id(self, id: str):
        if id in self.listNotes:
            self.listNotes.pop(id)

    def get_by_id(self, id: str):
        return self.listNotes[id]
        
    def get_by_title(self, text: str):
        res = []
        for note in self.listNotes.values():
            if note.get_note_for_search().find(text) != -1:
                res.append(note)
        return res

    def get_CSV(self):
        csv_raw = ""
        for note in self.listNotes.values():
            csv_raw += note.get_csv_format() + "\n"
        return csv_raw
    
    def get_all_notes(self):
        result = []
        for note in self.listNotes.values():
            result.append(note)
        return result
    
    def get_len_list_notes(self):
        return len(self.listNotes)
    
    def get_by_id_list(self,id_list:list) ->list:
        result=[]
        for id in id_list:
            result.append(self.listRecords[id])
        return result