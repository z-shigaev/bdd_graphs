import data_frame
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QTableWidgetItem, QCheckBox, QPushButton
from PyQt5.QtCore import Qt
import pyqtgraph as pg
import numpy as np
import main_window
import sys
import os


class MainWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.data = data_frame.RawData("data/test.csv")
        self.headers = None
        self.table_rows = 0
        self.table_columns = 0

        # раздел "Файл"
        self.actionOpen.triggered.connect(self.load_files)
        self.actionSave.triggered.connect(self.test)
        # Таблица
        self.tableLabels.cellClicked.connect(self.draw_graphs)

    def load_files(self):
        home_dir = os.getcwd()
        try:
            os.mkdir(home_dir + "\\Data")
        except OSError as error:
            print(error)
            pass
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, "Открыть файл", home_dir + "\\Data")[0]
        self.data = data_frame.RawData(file_name)
        self.headers = self.data.get_headers()
        self.table_rows = len(self.headers)
        self.table_columns = 1
        self.tableLabels.setRowCount(self.table_rows)
        self.tableLabels.setColumnCount(self.table_columns)
        for i in range(0, self.table_rows):
            # self.tableLabels.setItem(i, 1, QTableWidgetItem(self.headers[i]))
            item = QTableWidgetItem(self.headers[i])
            item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.tableLabels.setItem(i, 0, item)

    def draw_graphs(self):
        for i in range(0, self.table_rows):
            if self.tableLabels.item(i, 0).checkState() == 2:
                self.test()
            x = np.random.normal(size=1000)
            y = np.random.normal(size=1000)
            self.mainFrame.plot(x, y)

        pass
        # print(self.headers)

    def test(self):
        print("Good!")


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение