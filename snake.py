import pygame

class snake:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.size = int(50)
        self.dir = str()
        self.dir_controll = str()
        self.dir_x = int(0)
        self.dir_y = int(0)
        self.tail = []
        self.tail_length = int(3)
    
    def draw(self, screen):
        for segment in self.tail:
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(segment[0], segment[1], self.size, self.size))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.x, self.y, self.size, self.size))
    
    def control(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and self.dir != "right":
                self.dir_controll = "left"
                self.dir_x = -1
                self.dir_y = 0
            elif event.key == pygame.K_RIGHT and self.dir != "left":
                self.dir_controll = "right"
                self.dir_x = 1
                self.dir_y = 0
            elif event.key == pygame.K_UP and self.dir != "down":
                self.dir_controll = "up"
                self.dir_x = 0
                self.dir_y = -1
            elif event.key == pygame.K_DOWN and self.dir != "up":
                self.dir_controll = "down"
                self.dir_x = 0
                self.dir_y = 1
    
    def pos_update(self):
        if self.dir_x != 0 or self.dir_y != 0:
            self.tail.append((self.x, self.y))
            if len(self.tail) > self.tail_length:
                self.tail.pop(0)
        self.dir = self.dir_controll
        self.x += self.dir_x * self.size
        self.y += self.dir_y * self.size