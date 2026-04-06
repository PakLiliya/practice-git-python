import pygame
import datetime

class Clock:
    def __init__(self, screen):
        self.screen = screen
        self.center = (400, 300)  # центр циферблата

        # Загружаем стрелки
        self.second_hand = pygame.image.load('images/mickey_second.png').convert_alpha()
        self.minute_hand = pygame.image.load('images/mickey_minute.png').convert_alpha()

        # Масштабируем стрелки
        self.second_hand = pygame.transform.scale(self.second_hand, (25, 180))
        self.minute_hand = pygame.transform.scale(self.minute_hand, (25, 150))

    def blit_rotate(self, image, center, pivot, angle):
        """
        Вращение изображения вокруг произвольной точки pivot
        center — центр циферблата
        pivot — координаты основания стрелки в изображении (Vector2 или кортеж)
        angle — угол вращения в градусах
        """
        rotated_image = pygame.transform.rotate(image, -angle + 90)
        pivot_rotated = pygame.math.Vector2(pivot).rotate(-angle + 90)
        rect = rotated_image.get_rect(center=(center[0]-pivot_rotated.x, center[1]-pivot_rotated.y))
        self.screen.blit(rotated_image, rect.topleft)

    def update(self):
        now = datetime.datetime.now()
        seconds = now.second
        minutes = now.minute

        # Рисуем фон
        clock_face = pygame.image.load('images/mickey_clock.png').convert_alpha()
        clock_face = pygame.transform.scale(clock_face, (400, 400))
        rect = clock_face.get_rect(center=self.center)
        self.screen.blit(clock_face, rect.topleft)

        # Основание стрелки — низ картинки (x = середина по ширине, y = 0)
        second_pivot = (self.second_hand.get_width() / 2, 0)
        minute_pivot = (self.minute_hand.get_width() / 2, 0)

        # Рисуем стрелки, вращая от основания
        self.blit_rotate(self.second_hand, self.center, second_pivot, seconds*6)
        self.blit_rotate(self.minute_hand, self.center, minute_pivot, minutes*6)