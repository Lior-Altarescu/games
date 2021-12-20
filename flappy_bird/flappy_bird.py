import pygame
import os
import random

from pygame.constants import GL_GREEN_SIZE

pygame.init()

Window_weidth=800
Window_height=600

availble_y_blocks = 50
column_x_speed=10

TOP     = Window_height/4
MIDDLE  = 2*(Window_height/4)
BOTTOM  = 3*(Window_height/4)
COLUMN_POS=[TOP,MIDDLE,BOTTOM]
NUM_OF_OBSTICALES = 4

GREEN       = (61, 217, 38)
DARK_GREEN  = (10,93,0)
BLACK       = (0,0,0)

screen=pygame.display.set_mode((Window_weidth, Window_height))
pygame.display.set_caption("Flappy Bird - By Lior Altarescu")
icon=pygame.image.load('{}/assets/flappy_bird_icon.png'.format(os.path.dirname(os.path.abspath(__file__))))
backgrounImg=pygame.image.load('{}/assets/flappy_bird_background.png'.format(os.path.dirname(os.path.abspath(__file__))))
playerImg=pygame.image.load('{}/assets/flappy_bird_player.png'.format(os.path.dirname(os.path.abspath(__file__))))
game_overImg=pygame.image.load('{}/assets/flappy_bird_game_over.png'.format(os.path.dirname(os.path.abspath(__file__))))
pygame.display.set_icon(icon)

font = pygame.font.Font('{}/assets/Karla-VariableFont_wght.ttf'.format(os.path.dirname(os.path.abspath(__file__))), 32)

def draw_player(player_y):
    screen.blit(playerImg, (Window_weidth/2,player_y))

def draw_blockade(pos):
    pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], 0, 20,pos[1]-availble_y_blocks))
    pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1]+availble_y_blocks, 20,Window_height))

def game_over_screen():
    msg="Press Ctrl C to restart game , Ctrl q to quit"
    screen.blit(game_overImg, (0,0))
    text = font.render(msg, True,DARK_GREEN)
    screen.blit(text,(Window_weidth/2-(text.get_width()/2),3*(Window_height/4)))

def  show_score(score):
    scoretext = font.render("Score {0}".format(score), 1, BLACK)
    screen.blit(scoretext, (10, 15))

def main():
    #Variables
    RUNNING=True
    GAME_OVER=False
    background_x=-10
    background_x_change=10
    player_y = Window_height/2
    obsticales=[]
    remove_obsticales=[]
    score=0

    clock = pygame.time.Clock()
    while RUNNING:

        #Created a continuation background from 2 pictures
        if background_x == -Window_weidth:
             background_x=0
        background_x-=background_x_change
        screen.blit(backgrounImg, (background_x, 0))
        screen.blit(backgrounImg, (background_x+Window_weidth, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_y -= background_x_change*5

        while GAME_OVER:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        main()  
                    if event.key == pygame.K_q:
                        RUNNING = False
                        GAME_OVER = False
                        #pygame.quit()

        player_y+=15 
        draw_player(player_y)

        #Creating the obsticales
        if len(obsticales) < NUM_OF_OBSTICALES:
            tmpObstacle=[]
            if len(obsticales) == 0:
                tmpObstacle.append(Window_weidth)
            else:   
                tmpObstacle.append(obsticales[len(obsticales)-1][0]+350)       
            
            tmpObstacle.append(random.choice(COLUMN_POS))
            obsticales.append(tmpObstacle)
        
        #Creating new obsticales when they are out of screen
        for i in range(len(obsticales)):
            draw_blockade(obsticales[i])
            obsticales[i][0]-=column_x_speed
            if obsticales[i][0] <= 0 :
                remove_obsticales.append(i)
                
            if Window_weidth/2-5 <= obsticales[i][0] <= Window_weidth/2+5:
                if player_y  > obsticales[i][1] + availble_y_blocks or player_y <  obsticales[i][1] - availble_y_blocks:
                    GAME_OVER=True
                    game_over_screen()
                else:
                    score+=1

        #Removing out of screen obsticales
        for i in range(len(remove_obsticales)):
                obsticales.pop(remove_obsticales[i])
        remove_obsticales=[]
        show_score(score)
       
        # #Game over out of bounds
        if player_y >= Window_height or player_y <= 0 : 
            GAME_OVER=True
            game_over_screen()

        clock.tick(background_x_change)
        pygame.display.update()

    pygame.quit()

main()