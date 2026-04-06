import pygame
from clock import Clock

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

mickey_clock = Clock(screen)

# Таймер обновления каждую секунду
pygame.time.set_timer(pygame.USEREVENT, 1000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    mickey_clock.update()
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()