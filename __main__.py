#librery imports
import sys
import pygame
import time
from random import randint

#snake class import
from snake import snake
player = snake(400, 300)

#initilise game
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.event.get()
pygame.display.set_caption("Snake Game")

#seting veriables
pos_update_time = time.time()
aple_pos = [50 * randint(1, 15), 50 * randint(1, 11)]

#apple setup
apple = pygame.sprite.Sprite()
apple.image = pygame.image.load("apple.png").convert_alpha()
apple.rect = apple.image.get_rect()
apple.image = pygame.transform.scale(apple.image, (50, 50))
apple.rect.topleft = aple_pos


#main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        player.control(event)

    if time.time() - pos_update_time > 0.5:
        player.pos_update()
        pos_update_time = time.time()

    #screan render
    screen.fill((255, 255, 255))
    screen.blit(apple.image, apple.rect)
    player.draw(screen)
    pygame.display.update()

    #emergency exit
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT] and keys[pygame.K_LCTRL]:
        print("[emergency exit initiated]")
        break


print(player.tail)

pygame.quit()
sys.exit("[exit successfull]")