import pygame
import datetime

class Clock:
    def __init__(self, screen):
        self.screen = screen
        self.center = (400, 300)  # центр циферблата

        # Загружаем фон и стрелки
        self.clock_face = pygame.image.load('images/mickey_clock.png').convert_alpha()
        self.second_hand = pygame.image.load('images/mickey_second.png').convert_alpha()
        self.minute_hand = pygame.image.load('images/mickey_minute.png').convert_alpha()

        # Масштабируем стрелки (чуть больше)
        self.second_hand = pygame.transform.scale(self.second_hand, (200, 180))
        self.minute_hand = pygame.transform.scale(self.minute_hand, (200, 150))

        # Масштабируем фон, если нужно
        self.clock_face = pygame.transform.scale(self.clock_face, (400, 400))

    def update(self):
        # Получаем текущее время
        now = datetime.datetime.now()
        seconds = now.second
        minutes = now.minute

        # Углы вращения
        angle_seconds = seconds * 6   # 360° / 60 сек
        angle_minutes = minutes * 6   # 360° / 60 мин

        # Рисуем фон
        rect = self.clock_face.get_rect(center=self.center)
        self.screen.blit(self.clock_face, rect.topleft)

        # Вращаем секундную стрелку
        rotated_second = pygame.transform.rotate(self.second_hand, -angle_seconds + 90)
        rect_second = rotated_second.get_rect(center=self.center)
        self.screen.blit(rotated_second, rect_second.topleft)

        # Вращаем минутную стрелку
        rotated_minute = pygame.transform.rotate(self.minute_hand, -angle_minutes + 90)
        rect_minute = rotated_minute.get_rect(center=self.center)
        self.screen.blit(rotated_minute, rect_minute.topleft)