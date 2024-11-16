from PyQt6.QtWidgets import *
from sys import *
from sqlite3 import *
from csv import *
from PyQt6.QtGui import QPixmap
from PIL import *
import sqlite3


NAMES = (
    "Аридор",
    "Валард",
    "Валариан",
    "Гротар",
    "Ванн",
    "Фрон",
    "Йохан",
    "Грам",
    "Тарик",
    "Харальд",
)

HOUSE = (
    "Худородный",
    "Лурхан",
    "Байтмур",
    "Айлари",
    "Райстер",
    "Фирдар",
    "Хилтонг",
    "Юлитар",
    "Стойнхайр",
    "Айрохаммер",
    "Сайвербирд",
)

FROM = (
    "В лесистой Лотарии",
    "В жарком Крестмонде",
    "В прибрежной Лургундии",
    "В северной Готландии",
)


class MainWindowGame():
    def __init__(self):
        super().__init__()
        self.character = {"Motion": 0}
        self.initUI()

    def initUI(self):
        # настройки окна
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("Приключения")
        self.centralwidget = QWidget(self)
        self.grid_layout = QGridLayout(self.centralwidget)

        self.start_game = QPushButton("Начать игру", self.centralwidget)
        self.start_game.setMaximumSize(200, 30)

        self.grid_layout.addWidget(self.start_game)
        self.start_game.clicked.connect(self.familiarization)

        # поля для ввывода текста
        self.text_window = QListWidget(self)
        self.text_window.resize(300, 200)
        self.text_window.move(100, 0)
        self.text_window.hide()
        # кнопка для продолжения истории
        self.continue_way_button = QPushButton("продолжить", self)
        self.continue_way_button.resize(80, 40)
        self.continue_way_button.move(200, 220)
        self.continue_way_button.hide()
        self.continue_way_button.clicked.connect(self.continue_way)

        self.setCentralWidget(self.centralwidget)

    def familiarization(self):
        # узнаем информацию про вашего персонажа
        if "Name" in self.character.keys():
            pass
        else:
            name, ok_pressed = QInputDialog.getItem(
                self, "Введите имя", "Как Вас будут звать?", NAMES, 0, True
            )

            if ok_pressed and self.check_input(name):
                self.character["Name"] = name
            else:
                return self.error_input()

        if "Surname" in self.character.keys():
            pass
        else:
            surname, ok_pressed = QInputDialog.getItem(
                self,
                "Введите название вашего дома",
                "Какое имя вашей семьи?",
                HOUSE,
                0,
                True,
            )

            if ok_pressed and self.check_input(surname):
                self.character["Surname"] = surname
            else:
                return self.error_input()

        where_live, ok_pressed = QInputDialog.getItem(
            self, "Где вы начинаете", "Где вы находитесь?", FROM, 0, False
        )

        if ok_pressed:
            self.character["From_place"] = where_live

        conn = sqlite3.connect("characters_file_db.sqlite")
        cursor = conn.cursor()
        query = f"INSERT INTO users (Name, Surname, From_place, Motion) VALUES ('{name}', '{surname}', '{where_live}', '{0}')"
        cursor.execute(query)
        conn.commit()
        conn.close()

        self.start_game.hide()
        self.text_window.show()
        self.continue_way_button.show()

    def error_input(self):
        # Вывод ошибки
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Ошибка в вводе")
        dlg.setText("Введите корректно")
        dlg.show()
        button = dlg.exec()
        if button == QMessageBox.StandardButton.Ok:
            return self.familiarization()

    def check_input(self, meaning):
        # Проверка введеных данных
        for i in meaning.split():
            if not i.isalpha():
                return False
        if len(meaning.split()) == 0:
            return False
        return True

    def continue_way(self):
        self.text_window.clear()
        self.text_window.addItem(self.character["Motion"])


if __name__ == "__main__":
    app = QApplication(argv)
    ex = MainWindowGame()
    ex.show()
    exit(app.exec())
