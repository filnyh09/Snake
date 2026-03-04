import pygame
from random import randint

from snake import snake

player = snake(400, 300)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.event.get()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    player.draw(screen)
    pygame.display.update()

pygame.quit()