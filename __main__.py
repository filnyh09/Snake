#librery imports
import sys
import pygame
import time
from random import randint
import pygame_widgets
from pygame_widgets.slider import Slider

#initilise game
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.event.get()
pygame.display.set_caption("Snake Game")

speed_slider = Slider(screen, 650, 550, 100, 10, min=0, max=9, initial=5)
speed_slider.listen(pygame.event.get())

#snake class import
import snake
player = snake.snake(400, 300)

#seting veriables
pos_update_time = time.time()

#emergency exit
def emergency_exit_check():
    try:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT] and keys[pygame.K_LCTRL]:
            print("[emergency exit initiated]")
            return True
    except:
        print("[errer] emergency exit check failed")

#apple setup
apple = pygame.sprite.Sprite()
apple.image = pygame.image.load("apple.png").convert_alpha()
apple.rect = apple.image.get_rect()
apple.image = pygame.transform.scale(apple.image, (50, 50))

def apple_spawn(forward_x, forward_y):
    apple.rect.topleft = [50 * randint(1, 15), 50 * randint(1, 11)]
    while apple.rect.topleft in player.tail or (apple.rect.x == player.x + forward_x and apple.rect.y == player.y + forward_y):
        apple.rect.topleft = [50 * randint(1, 15), 50 * randint(1, 11)]

apple_spawn(0, 0)


#endgame condition function
def check_collision():
    #collision with self
    if (player.x, player.y) in player.tail:
        print("[collision with self detected]")
        return True
    elif player.x < 0 or player.x > 750 or player.y < 0 or player.y > 550:
        print("[collision with wall detected]")
        return True
    return False

def endgame_screen(win: bool):
    quit = snake.button(150, 250, 200, 100, "Quit")
    restart = snake.button(450, 250, 200, 100, "Restart")
    endgame_screen = pygame.font.SysFont('Comic Sans MS', 30)
    if win:
        endgame_message = endgame_screen.render("you win", False, (0, 0, 0))
    else:
        endgame_message = endgame_screen.render("you loose", False, (0, 0, 0))
    
    endgame_score = endgame_screen.render(str(player.tail_length), False, (0, 0, 0))

    end_screen = True
    while end_screen:
        screen.blit(endgame_message, (330, 100))
        screen.blit(endgame_score, (380, 200))
        quit.draw(screen)
        restart.draw(screen)
        if restart.is_clicked():
            player.restart()
            player.draw(screen)
            apple_spawn(0, 0)
            end_screen = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT or quit.is_clicked() or emergency_exit_check():
                    pygame.quit()
                    sys.exit("[exit successfull]")

#main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        player.control(event)

    game_speed = speed_slider.getValue()
    events = pygame.event.get()
    pygame_widgets.update(events)

    if time.time() - pos_update_time > 1 - game_speed * 0.1:
        
        #collision detection with apple
        if player.x + player.dir_x * 50 == apple.rect.x and player.y + player.dir_y * 50 == apple.rect.y:
            player.tail_length += 1
            apple_spawn(player.dir_x * 50, player.dir_y)
            player.load_image("snake_eat.png")
        else:
            player.load_image("snake_smile.png")
            
        player.pos_update()
        pos_update_time = time.time()

    #screan render
    screen.fill((94, 143, 67))
    screen.blit(apple.image, apple.rect)
    player.draw(screen)
    speed_slider.draw()
    pygame.display.update()
    
    if emergency_exit_check():
        pygame.quit()
        sys.exit("[exit successfull]")

    #endgame condition check
    if check_collision():
        if player.tail_length < 164:
            print("[lost]")
            endgame_screen(False)
        else:
            print("[won]")
            endgame_screen(True)




print(player.tail)

pygame.quit()
sys.exit("[exit successfull]")