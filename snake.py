import pygame
from random import randint

class snake:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.size = int(50)
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.x, self.y, self.size, self.size))