import pygame


class button:
    def __init__(self, x, y, width, hight, text, action = None):
        self.rect = pygame.Rect(x, y, width, hight)
        self.action = action
        self.text = text
        self.color = (200, 200, 200)
        self.hover_color = (150, 150, 150)
        self.font = pygame.font.SysFont(None, 36)
    def draw(self, screen):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, "black")
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))
        pygame.display.update()
    def is_clicked(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and  pygame.mouse.get_pressed()[0]:
            return True
        return False

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
        self.tail_length = int(0)
        super().__init__()
        self.og_image = pygame.image.load("snake_smile.png").convert_alpha()
        self.image = pygame.Surface((self.size, self.size))
        self.image = self.og_image.subsurface((0, 0, self.size, self.size))
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        
    
    def draw(self, screen):
        for segment in self.tail:
            pygame.draw.rect(screen, ((86, 184, 154)), pygame.Rect(segment[0], segment[1], self.size, self.size))
        screen.blit(self.image, (self.x, self.y))
    
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

        self.rotation_angle = int()
        if self.dir == "up":
            self.rotation_angle = 180
        elif self.dir == "down":
            self.rotation_angle = 0
        elif self.dir == "left":
            self.rotation_angle = -90
        elif self.dir == "right":
            self.rotation_angle = 90
        else:
            print("[error] invalid direction")

        self.image = pygame.transform.rotate(self.og_image, self.rotation_angle)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
    
    def restart(self):
        self.x = int(400)
        self.y = int(300)
        self.dir = str()
        self.dir_controll = str()
        self.dir_x = int(0)
        self.dir_y = int(0)
        self.tail = []
        self.tail_length = int(0)