from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import pyqtgraph as pg
import sys

class Interface(QMainWindow):
    def __init__(self):
        super(Interface, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Teste")
        self.nextButtonId = 0
        self.nextLabelId = 0
        self.Labels = []
        self.Buttons = []


    def addButton(self, text, position, function):
        l1 = f"self.button_{self.nextButtonId} = QtWidgets.QPushButton(self)"
        l2 = f"self.button_{self.nextButtonId}.setText(\"{text}\")"
        l3 = f"self.button_{self.nextButtonId}.move(position[0], position[1])"
        l4 = f"self.button_{self.nextButtonId}.clicked.connect(function)"
        exec(l1)
        exec(l2)
        exec(l3)
        exec(l4)
        self.Buttons.append([text, self.nextButtonId])
        self.nextButtonId += 1


    def addLabel(self, text, position):
        l1 = f"self.label_{self.nextLabelId} = QtWidgets.QLabel(self)"
        l2 = f"self.label_{self.nextLabelId}.move(position[0], position[1])"
        l3 = f"self.label_{self.nextLabelId}.setText(\"{text}\")"
        exec(l1)
        exec(l2)
        exec(l3)
        self.Labels.append([text, self.nextButtonId])
        self.nextLabelId += 1


    def update(self):
        self.label.adjustSize()