import pygame
from random import randint

class snake:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.size = int(50)
        self.dir_x = int(0)
        self.dir_y = int(0)
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.x, self.y, self.size, self.size))
    def control(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and self.dir_x != 1:
                self.dir_x = -1
                self.dir_y = 0
            elif event.key == pygame.K_RIGHT and self.dir_x != -1:
                self.dir_x = 1
                self.dir_y = 0
            elif event.key == pygame.K_UP and self.dir_y != 1:
                self.dir_x = 0
                self.dir_y = -1
            elif event.key == pygame.K_DOWN and self.dir_y != -1:
                self.dir_x = 0
                self.dir_y = 1
    def pos_update(self):
        self.x += self.dir_x * self.size
        self.y += self.dir_y * self.size