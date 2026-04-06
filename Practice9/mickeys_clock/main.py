import pygame
from clock import Clock

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()
mickey_clock = Clock(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    mickey_clock.update()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()