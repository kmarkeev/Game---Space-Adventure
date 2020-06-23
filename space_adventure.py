import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from bullet import Bullet

def run_game():
    #Инициализирует игру и создаёт объект экрана.
    pygame.init()
    sa_settings = Settings()
    screen = pygame.display.set_mode((sa_settings.screen_width, sa_settings.screen_height))
    pygame.display.set_caption("Space Adventure")

    #Создание коробля
    ship = Ship(sa_settings, screen)
    #Создание группы для хранения пуль
    bullets = Group()
    
    
    #Запуск основного цикла игры.
    while True:
        #Отслеживание событий клавиатуры и мыши.
        gf.check_events(sa_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        #Удаление пуль, вышедших за край экрана.
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
                
        

        #При каждом проходе цикла перерисовывается экран.
        gf.update_screen(sa_settings, screen, ship, bullets)


run_game()
