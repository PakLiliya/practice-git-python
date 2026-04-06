import pygame
import sys
from player import MusicPlayer

pygame.init()

WIDTH, HEIGHT = 500, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

player = MusicPlayer()
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

running = True
while running:
    screen.fill((30, 30, 30))

    track_text = font.render(f"Track: {player.current_track_name()}", True, (255, 255, 255))
    screen.blit(track_text, (50, 80))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play
                player.play()
            elif event.key == pygame.K_s:  # Stop
                pass  # Заглушка
            elif event.key == pygame.K_n:  # Next
                player.next()
            elif event.key == pygame.K_b:  # Previous
                player.prev()
            elif event.key == pygame.K_q:  # Quit
                running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()