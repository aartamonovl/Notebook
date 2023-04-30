from os import system


class Menu: 
    '''
    класс консольного текстового меню
    elements = список кортежей  
        кортеж => ("маркер","описание",метод)  
        если метод в кортеже==-1 то menu.run() возвращает True  
        это нужно для реализации выхода из меню реализованных  
        во вложенных методах'''

    def __init__(self, elenemts=[]):
        self.elements = elenemts
        self.prefixtext = ''

    def print(self):
        """отрисовка элементов меню
        """
        print(self.prefixtext, end='')
        for (mark, text, _) in self.elements:
            print('{} - {}'.format(mark, text))

    def run(self, prompt='Выберите команду >>> ', pause=True):
        """запуск основного меню
        Args:
            prompt (str, optional): приглашение после отрисовки меню . Defaults to 'выберите команду: '.
            pause (bool, optional): опция включения паузы и очистки экрана
                после выполнения команды меню. Defaults to False.
        Returns:
            _type_: _description_
        """
        self.clrscr()
        while True:
            self.print()
            user_choice = int(input(prompt))
            for (mark, _, runmethod) in self.elements:
                if user_choice == mark:
                    if runmethod == -1:
                        return
                    runmethod()
                    if pause:
                        input("Ввод для продолжения...")
                        Menu.clrscr()
                    break

    def __len__(self):
        return len(self.elements)

    @staticmethod
    def clrscr():
        """очистка экрана
        """
        system('cls')