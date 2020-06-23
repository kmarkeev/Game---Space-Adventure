import pygame

class Ship():

    def __init__(self, sa_settings, screen):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = screen
        self.sa_settings = sa_settings

        #Загрузка изображения коробля и получение прямоугольника.
        self.image = pygame.image.load("img/ship.bmp")
        #self.image_transform = pygame.transform.scale(image, (50, 100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - self.rect.bottom - self.rect.top

        #Сохранение вещественной координаты центра корабля
        self.center = float(self.rect.centerx)

        #Флаги перемещения
        self.moving_right = False
        self.moving_left = False
        

    def update(self):
        """Обновляет позицию коробля с учётом флагов."""
        #Обновляется атрибут center, не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.sa_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.sa_settings.ship_speed_factor

        #Обновление атрибута rect на основании self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
        
        
