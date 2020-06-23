class Settings():
    """Класс для хранения всех настроек игры Space Adventure"""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 300
        self.screen_height = 800
        #Это фон экрана, но сейчас там заливается картинка звёздного неба
        self.bg_color = (25, 25, 112)

        #Настройки коробля
        self.ship_speed_factor = 1.5

        # Параметры пули
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
