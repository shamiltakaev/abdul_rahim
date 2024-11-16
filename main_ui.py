from PyQt6.QtWidgets import QGridLayout, QPushButton, QWidget, QMainWindow, QStatusBar, QMenuBar
from PyQt6.QtCore import QMetaObject


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QMainWindow):
        MainWindow.resize(554, 379)
        MainWindow.setGeometry(500, 500, 500, 500)

        self.centralwidget = QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralWidget")
        self.layout = QGridLayout(self.centralwidget)
        self.centralwidget.setStyleSheet("""
                                         #centralWidget {
                                            border-image: url(Dungeons and Dragons Strahd Castle _ Patreon Dungeons_LAB.jpg) 0 0 0 0 ;
                                         }
                                         """)

        self.new_game = QPushButton("Новая Игра", self.centralwidget)
        self.downlaod_the_game = QPushButton(
            "Загрузить игру", self.centralwidget)
        self.music_playlist = QPushButton('Выбрать музыку', self.centralwidget)

        self.layout.addWidget(self.music_playlist, 2, 1)
        self.layout.addWidget(self.new_game, 0, 1)
        self.layout.addWidget(self.downlaod_the_game, 1, 1)

        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(1, 2)
        self.layout.setColumnStretch(2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(parent=MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(parent=MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        QMetaObject.connectSlotsByName(MainWindow)
