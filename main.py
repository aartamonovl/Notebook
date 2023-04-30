import sys
from controller import Controller
from model import Model

__path_csv__ = './notes.csv'

if __name__ == '__main__':
    model = Model(__path_csv__)
    app = Controller(model)
    app.start()