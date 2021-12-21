import pygame
import os
import sys


pygame.init()

Window_weidth=400
Window_height=500

FPS = 25
BACKGROUND=(169,169,169)
BLACK=(0,0,0)
TEXTBOX_Y=100
BUFFER=10
LINES_PER_ORIANTAION=2
CURRENT_TURN='o'
GAME_RESULT='INPLAY'


screen=pygame.display.set_mode((Window_weidth, Window_height))
pygame.display.set_caption("Tick Tac Toe - By Lior Altarescu")
icon=pygame.image.load('{}/assets/tic-tac-toe_icon.png'.format(os.path.dirname(os.path.abspath(__file__))))
game_startImg=pygame.image.load('{}/assets/tic-tac-toe-startscreen.png'.format(os.path.dirname(os.path.abspath(__file__))))
pygame.display.set_icon(icon)

font = pygame.font.Font('{}/assets/Karla-VariableFont_wght.ttf'.format(os.path.dirname(os.path.abspath(__file__))), 32)

def game_start():
    #Variables
    RUNNING=True

    clock = pygame.time.Clock()
    while RUNNING:
        screen.blit(game_startImg,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    main()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

def display_game_status():

    if GAME_RESULT == 'INPLAY':
        if CURRENT_TURN == 'o':
            msg="Your (\"O\") turn"
        else:
            msg="X's turn"
    else :
        if GAME_RESULT=='WON' :
            msg="Player Won \o/"
        else:
            msg="Player Lost > o<"
    playermsg = font.render(msg, 1, BLACK)
    screen.blit(playermsg, ( Window_weidth/2-playermsg.get_width()/2,(Window_height-TEXTBOX_Y+BUFFER)))

    
def draw_borders():
    pos_x=Window_weidth/3

    for i in range(LINES_PER_ORIANTAION):
        pygame.draw.line(screen, BLACK, (pos_x, BUFFER), (pos_x,Window_height-TEXTBOX_Y-BUFFER), 3)
        pygame.draw.line(screen, BLACK, (BUFFER,pos_x), (Window_height-TEXTBOX_Y-BUFFER,pos_x), 3)

        pos_x *=2


def main():
    #Variables
    RUNNING=True
    
    clock = pygame.time.Clock()
    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                sys.exit()

        screen.fill(BACKGROUND)

        draw_borders()
        display_game_status()
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    
game_start()
