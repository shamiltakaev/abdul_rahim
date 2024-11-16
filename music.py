import time
import random
from pygame import mixer

MUSIC_PLAY_LIST = {
    'Ambience Fantasy': 'Music/Ambience Fantasy — Long Night (Medieval Tavern Song) (www.lightaudio.ru).mp3',
    'Fantasy Medieval Music': 'Music/Fantasy Medieval Music — Dance with Dragons (www.lightaudio.ru).mp3',
    'Game of Thrones': 'Music/Game of Thrones Main Theme (Gingertail Cover) — House of the Dragon Opening Theme (www.lightaudio.ru).mp3',
    'Ramin Djawadi': "Music/Ramin Djawadi — The Night's Watch (Opening) (www.lightaudio.ru) (1).mp3",
    'Game of Thrones на скрипку': 'Music/Песнь льда и пламени — Скрипка (Игра престолов) (www.lightaudio.ru).mp3'
}
#включает музыку во время игры
# class Music:
#     def play_start_music(self, name):
#         #воспроизводит музыку
#         mixer.init()
#         mixer.music.load(MUSIC_PLAY_LIST[name])
#         mixer.music.play()
#         while mixer.music.get_busy():
#             time.sleep(1)

#     def play_end_music(self):
#         mixer.pause()



import pygame as pg
import sys
pg.init()
sc = pg.display.set_mode((400, 300))
 
pg.mixer.music.load('Music/Game of Thrones Main Theme (Gingertail Cover) — House of the Dragon Opening Theme (www.lightaudio.ru).mp3')
pg.mixer.music.play()
 
sound1 = pg.mixer.Sound('Music/Ambience Fantasy — Long Night (Medieval Tavern Song) (www.lightaudio.ru).mp3')
sound2 = pg.mixer.Sound('Music/Ambience Fantasy — Long Night (Medieval Tavern Song) (www.lightaudio.ru).mp3')
 
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
 
        elif i.type == pg.KEYUP:
            if i.key == pg.K_1:
                pg.mixer.music.pause()
                # pygame.mixer.music.stop()
            elif i.key == pg.K_2:
                pg.mixer.music.unpause()
                # pygame.mixer.music.play()
                pg.mixer.music.set_volume(0.5)
            elif i.key == pg.K_3:
                pg.mixer.music.unpause()
                # pygame.mixer.music.play()
                pg.mixer.music.set_volume(1)
 
        elif i.type == pg.MOUSEBUTTONUP:
            if i.button == 1:
                sound1.play()
            elif i.button == 3:
                sound2.play()
 
    pg.time.delay(20)

