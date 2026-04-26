import pygame
from clock import Clock

pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

# Цвет фона (на случай, если стрелки не прозрачные)
BG_COLOR = (255, 255, 255)

# Создаем часы
mickey_clock = Clock(screen)

# Таймер обновления каждую секунду
pygame.time.set_timer(pygame.USEREVENT, 1000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Фон
    screen.fill(BG_COLOR)

    # Обновляем часы
    mickey_clock.update()

    pygame.display.flip()
    pygame.time.Clock().tick(60)  # 60 FPS

pygame.quit()