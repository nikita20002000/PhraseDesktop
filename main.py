# Created by nikitanovikov at 27.03.2023


import sys
from PyQt6 import uic, QtCore, QtGui, QtWidgets
import requests as req


class MainWindow(QtWidgets.QMainWindow):
    count = 0

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('untitled.ui', self)
        self.pushButton1.clicked.connect(self.pushButton1_clicked)
        self.pushButton.clicked.connect(self.clear_clicked)


    def pushButton1_clicked(self):
        self.get_text()

    def get_text(self, url='https://evilinsult.com/generate_insult.php?lang=en&type=json'):
        responce = req.get(url)
        self.listWidget.insertItem(self.count, responce.json()['insult'])
        self.count += 1

    def clear_clicked(self):
        self.listWidget.clear()






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

