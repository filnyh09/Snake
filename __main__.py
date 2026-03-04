import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.event.get()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(400, 300, 50, 50))
    pygame.display.update()

pygame.quit()