import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, sa_settings, screen, ship, bullets):
    """Реагирует на нажатие клавиш."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #Создание новой пули и включение её в группу Bullets
        new_bullet = Bullet(sa_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    

def check_events(sa_settings, screen, ship, bullets):
    """Обрабатывает нажатия кловиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, sa_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
                

def update_screen(sa_settings, screen, ship, bullets):
    """Обновляет изображение на экране и отображает новый экран."""
    #Загружаем картинку
    background = pygame.image.load("img/bg.png")
    #Подганяет фоновую картинку под размер экрана
    #image = pygame.transform.scale(background, (50, 100))
    #image_rect = image.get_rect()
    background_rect = background.get_rect()

    #При каждом проходе цикла перерисовывается экран.
    #screen.fill(sa_settings.bg_color)
    screen.blit(background, background_rect)

    #Все пули выводятся позади изображения коробля и астероидов
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()

    # Отображение последнего прорисованного экрана.
    pygame.display.flip()
