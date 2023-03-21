import data_frame
from PyQt5 import QtWidgets, QtCore, QtGui
import main_window
import sys
import os


class MainWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.data = data_frame.RawData("data/test.csv")
        # раздел "Файл"
        self.actionOpen.triggered.connect(self.load_files)
        self.actionSave.triggered.connect(self.test)

    def load_files(self):
        home_dir = os.getcwd()
        try:
            os.mkdir(home_dir + "\\Data")
        except OSError as error:
            print(error)
            pass
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, "Открыть файл", home_dir + "\\Data")[0]

    def test(self):
        print("Good!")


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    # QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    # os.environ["QT_SCALE_FACTOR"] = "1.0"
    #
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение