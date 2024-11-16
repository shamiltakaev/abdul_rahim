from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from sys import *
from main_ui import Ui_MainWindow
from sqlite3 import *
from csv import *
from PyQt6.QtGui import QPixmap
from PIL import *
import sqlite3
import random
import time
from pygame import mixer
import threading


MUSIC_LIST = [
    'Ambience Fantasy',
    'Fantasy Medieval Music',
    'Game of Thrones',
    'Ramin Djawadi',
    'Game of Thrones на скрипку'
]

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

MUSIC_PLAY_LIST = {
    'Ambience Fantasy': 'Music/Ambience Fantasy — Long Night (Medieval Tavern Song) (www.lightaudio.ru).mp3',
    'Fantasy Medieval Music': 'Music/Fantasy Medieval Music — Dance with Dragons (www.lightaudio.ru).mp3',
    'Game of Thrones': 'Music/Game of Thrones Main Theme (Gingertail Cover) — House of the Dragon Opening Theme (www.lightaudio.ru).mp3',
    'Ramin Djawadi': "Music/Ramin Djawadi — The Night's Watch (Opening) (www.lightaudio.ru).mp3",
    'Game of Thrones на скрипку': 'Music/Песнь льда и пламени — Скрипка (Игра престолов) (www.lightaudio.ru).mp3'
}

mixer.init()
mixer.music.load(MUSIC_PLAY_LIST["Ambience Fantasy"])
mixer.music.play()
is_running = True
is_playing_music = True
def music_play():
    while is_running:
        if mixer.music.get_busy() is False and is_playing_music:
            mixer.music.load(MUSIC_PLAY_LIST[random.choice(MUSIC_LIST)])
            mixer.music.play()

music_play_thread = threading.Thread(target=music_play)
music_play_thread.start()

class Menu(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.new_game.clicked.connect(self.new_game_fun)
        self.downlaod_the_game.clicked.connect(lambda : print())
        self.music_playlist.clicked.connect(self.play_music)
        
    def new_game_fun(self):
        self.new = Menu_new()
        self.hide()
        self.new.show()

    def play_music(self):
        self.new = Menu_music()
        self.hide()
        self.new.show()
        
    def closeEvent(self, a0):
        global is_running
        is_running = False
        return super().closeEvent(a0)

    
class Menu_new(QWidget):
    def __init__(self):
        super().__init__()
        self.character = {"Motion": 0}
        self.initUI()

    def initUI(self):
        # настройки окна
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("Приключения")
        self.centralwidget = QWidget(self)

        self.start_game = QPushButton("Начать игру", self.centralwidget)
        self.start_game.move(200, 200)
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

        self.btn = QPushButton("Меню", self)
        self.btn.clicked.connect(self.btn_click)
        

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
        with open('novell.txt', 'r', encoding='utf8') as file:
            pass
            # text = [i] 
        self.text_window.addItem(self.character["Motion"])
        
    def btn_click(self):
        self.destroy()
        ex.show()
        
    def closeEvent(self, a0):
        ex.show()
        return super().closeEvent(a0)    


class Menu_music(QWidget):
    def __init__(self):
        super().__init__()
        # self.melodi_fon = Music()
        self.flag_music = False
        self.initUI()            
    
    def initUI(self):
        # настройки окна
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("Музыкальный лист")
        
        self.start_music = QPushButton("Выбрать Музыку", self)
        self.start_music.move(200, 200)
        self.start_music.clicked.connect(self.option_music)

        self.end_music = QPushButton("Отключить", self)
        self.end_music.move(200, 230)
        self.end_music.clicked.connect(self.turn_of)
        
        self.btn = QPushButton("Меню", self)
        self.btn.clicked.connect(self.btn_click)


    def option_music(self):
        global is_playing_music
        is_playing_music = False
        music, ok_pressed = QInputDialog.getItem(
            self, "выбор музыки", "какую выбираете музыку?", MUSIC_LIST, 0, False
        )
        if ok_pressed and not self.flag_music:
            mixer.music.stop()
            mixer.music.unload()
            mixer.music.load(MUSIC_PLAY_LIST[music])
            mixer.music.play()
            self.flag_music = True
            is_playing_music = True
            

    def turn_of(self):
        global is_playing_music
        is_playing_music = False
        mixer.music.stop()

    def error_music(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Ошибка")
        dlg.setText("Музыка выключена")
        dlg.show()
        button = dlg.exec()
        if button == QMessageBox.StandardButton.Ok:
            pass

    def btn_click(self):
        self.destroy()
        ex.show()
    
    def closeEvent(self, a0):
        ex.show()
        return super().closeEvent(a0)
    

if __name__ == '__main__':
    app = QApplication(argv)

    ex = Menu()
    ex.show()

    exit(app.exec())




