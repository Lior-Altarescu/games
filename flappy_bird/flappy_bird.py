import pygame
import os
import time
import random

pygame.init()

Window_weidth=800
Window_height=600

screen=pygame.display.set_mode((Window_weidth, Window_height))
pygame.display.set_caption("Flappy Bird - By Lior Altarescu")
icon=pygame.image.load('{}/assets/flappy_bird_icon.png'.format(os.path.dirname(os.path.abspath(__file__))))
backgrounImg=pygame.image.load('{}/assets/flappy_bird_background.png'.format(os.path.dirname(os.path.abspath(__file__))))
playerImg=pygame.image.load('{}/assets/flappy_bird_player.png'.format(os.path.dirname(os.path.abspath(__file__))))
pygame.display.set_icon(icon)

def draw_player(player_y):
    screen.blit(playerImg, (Window_weidth/2,player_y))

def main():
    #Variables
    RUNNING=True
    GAME_OVER=False
    background_x=-10
    background_x_change=10
    player_y = Window_height/2

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
                    player_y -= background_x_change*4

        while GAME_OVER:
            for event in pygame.event.get():
                if event.key == pygame.K_c:
                    GAME_OVER = False  
                if event.key == pygame.K_q:
                    pygame.quit()

        player_y+=5
        draw_player(player_y)
        clock.tick(background_x_change)
        pygame.display.update()

    pygame.quit()

main()