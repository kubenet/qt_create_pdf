import glob
import shutil

import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QAction

import gui_v3  # Это наш конвертированный файл дизайна
from gen_pdf import generate_pdf
from compare_pdf import compare_pdf as compare
from clear_dir import clear

templates = os.listdir('learn_templates')
user_list = os.listdir('user_lists')


def view_diplomas():
    os.system('explorer.exe "diplomas"')


class ExampleApp(QtWidgets.QMainWindow, gui_v3.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_2.clicked.connect(self.start_generation)  # Выполнить функцию start_generation
        self.pushButton.clicked.connect(self.browse_folder)  # Выполнить функцию browse_folder
        self.pushButton_3.clicked.connect(view_diplomas)  # связь кнопки открыть папку с результатом (дипломами)
        #self.pushButton_4.clicked.connect(doc2pdf)
        self.comboBox.addItems(templates)  # заполнение comboBox списком файлов шаблонов
        self.comboBox_2.addItems(user_list)  # заполнение comboBox списком файлов групп
        self.dateEdit.setCalendarPopup(True)  # настройка даты опция выпадающего календаря
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())  # устанавливаем текущую дату
        self.dateEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())  # устанавливаем текущую дату
        self.dateEdit_2.setCalendarPopup(True)  # настройка даты опция выпадающего календаря
        self.progressBar.setValue(0)  # настройка первоначального значения progressBar
        self.menu.setEnabled(False)  # неактивный пункт меню "Справка"
        self.action = QAction("Выход")  # создание нового пункта меню
        self.action2 = QAction("Тест сертификата")  # создание одного сертификата для проверки шаблона и внешнего вида
        self.menu_2.addAction(self.action2)  # добавление в меню пункт "Тест сертификата"
        self.menu_2.addAction(self.action)  # добавление в меню пункт "Выход"
#        self.action2.triggered.connect(self.test_diploma)  # кнопка генерации тестового диплома (одного экземпляра)
        self.action.triggered.connect(self.close)  # кнопка закрытия приложения
        self.checkBox.setChecked(True)  # по умолчанию конвертация в pdf включена


        # shutil.rmtree('//pdf')
        # shutil.rmtree('//result')
        # os.mkdir("pdf")
        # os.mkdir("result")

    def view_diplomas(self):
        # lists_path = Path('diplomas')
        # print(lists_path)
        os.system('explorer.exe "diplomas"')

    def browse_folder(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, "Выбор шаблона", None, "word (*.doc *.docx)")[0]
        self.label_5.setText(file_name)

    def start_generation(self):
        clear("pdf//")  # очистка папки с шаблонами
        clear("result//")   # очистка папки результатов

        group_list = str(self.comboBox_2.currentText())
        # --- radio button --- #
        # if self.radioButton.isChecked():
        #     print('Базовая группа')
        # elif self.radioButton_2.isChecked():
        #     print('Проектная группа')
        # elif self.radioButton_3.isChecked():
        #     print('Свой шаблон')
        # # --- checkBox --- #
        # if self.checkBox_2.isChecked():
        #     print('Сохранить в один файл')
        # if self.checkBox_3.isChecked():
        #     print('Дата начала и окончания')
        date2 = self.dateEdit.date().toString('dd.MM.yyyy')
        date1 = self.dateEdit_2.date().toString('dd.MM.yyyy')
        duration = self.lineEdit.text()
        self.label_5.setText("Готовим PDF...")
        rezult = generate_pdf(group_list, date1, date2, duration)
        if rezult == 0:
            print("rez OK!")
            compare() # объединение шаблона с данными в pdf
        self.label_5.setText("PDF готовы")


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()