import pygame
import os
import time
import random

pygame.init()

Window_weidth=800
Window_height=600

WHITE=(190,190,190)
BLACK=(0,0,0)
RED=(164, 0, 0)

player_speed    = 25
player_size     = 10


screen=pygame.display.set_mode((Window_weidth, Window_height))
pygame.display.set_caption("Snake - By Lior Altarescu")
icon=pygame.image.load('{}/assets/anaconda.png'.format(os.path.dirname(os.path.abspath(__file__))))
pygame.display.set_icon(icon)
font = pygame.font.Font('freesansbold.ttf', 32)

def message(msg,color):
    screen.fill(WHITE)
    text = font.render(msg, True,color)
    screen.blit(text,(int(Window_weidth//2-len(msg)//2)-50,Window_height/3))

def show_score(score):
    scoretext = font.render("Score {0}".format(score), 1, BLACK)
    screen.blit(scoretext, (10, 15)) 

def main():
    #Setting Variables
    spawn_food          = True
    player_score        = 0
    RUNNING             = True
    pos_x               = Window_weidth/2
    pos_y               = Window_height/2
    pos_x_change        = 10
    pos_y_change        = 0
    player_direction    = 'right'
    snake_body          = [(pos_x,pos_y)]
    food_x              = 0
    food_y              = 0 


    clock = pygame.time.Clock()
    

    while RUNNING:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and player_direction != 'RIGHT':
                    pos_x_change = -10
                    pos_y_change = 0
                    player_direction = 'LEFT'
                if event.key == pygame.K_RIGHT and player_direction != 'LEFT':
                    pos_x_change = 10
                    pos_y_change = 0
                    player_direction = 'RIGHT'
                if event.key == pygame.K_UP and player_direction != 'DOWN':
                    pos_x_change = 0
                    pos_y_change = -10
                    player_direction = 'UP'  
                if event.key == pygame.K_DOWN and player_direction != 'UP':
                    pos_x_change = 0
                    pos_y_change = 10
                    player_direction = 'DOWN'

        pos_x += pos_x_change
        pos_y += pos_y_change
        
        snake_pos=(pos_x,pos_y)
        snake_body.insert(0, snake_pos)

        #Spawn food
        if  spawn_food:
            while True:
                food_x=round(random.randrange(20,Window_weidth-20)/10)*10
                food_y=round(random.randrange(20,Window_height-20)/10)*10
                if (food_x,food_y) not in (snake_body):
                    break
            spawn_food=False 
        else:
            snake_body.pop()           
        
        pygame.draw.circle(screen,RED,(food_x,food_y),player_size/2)
        #Eat food
        if food_x == pos_x and food_y==pos_y:
            spawn_food=True
            player_score+=1

        for block in snake_body:
            pygame.draw.rect(screen,BLACK,pygame.Rect(block[0],block[1],player_size,player_size))

        show_score(player_score)

        if  pos_x + 10 >= Window_weidth or pos_x - 10 < 0 or \
            pos_y + 10 >= Window_height or pos_y - 10 < 0 or \
            (pos_x,pos_y) in (snake_body[1:]):
            message("Game Over",RED)
            RUNNING=False

        pygame.display.update()

        clock.tick(player_speed)

    time.sleep(2)
    pygame.quit()

main()