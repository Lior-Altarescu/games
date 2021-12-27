import pygame
import os
import sys
import math
import numpy
import random


pygame.init()

Window_weidth=400
Window_height=500

FPS = 50
BACKGROUND=(169,169,169)
BLACK=(0,0,0)
TEXTBOX_Y=100
BUFFER=10
LINES_PER_ORIANTAION=2
AI='x'
HUMAN='o'
CURRENT_TURN=HUMAN
GAME_RESULT='INPLAY'
GAMEBOARD=[[0,0,0],[0,0,0],[0,0,0]]


screen=pygame.display.set_mode((Window_weidth, Window_height))
pygame.display.set_caption("Tick Tac Toe - By Lior Altarescu")
icon=pygame.image.load('{}/assets/tic-tac-toe_icon.png'.format(os.path.dirname(os.path.abspath(__file__))))
game_startImg=pygame.image.load('{}/assets/tic-tac-toe-startscreen.png'.format(os.path.dirname(os.path.abspath(__file__))))
xImg=pygame.image.load('{}/assets/x.png'.format(os.path.dirname(os.path.abspath(__file__))))
oImg=pygame.image.load('{}/assets/o.png'.format(os.path.dirname(os.path.abspath(__file__))))
pygame.display.set_icon(icon)

font = pygame.font.Font('{}/assets/Karla-VariableFont_wght.ttf'.format(os.path.dirname(os.path.abspath(__file__))), 32)

def game_start():
    #Variables
    INITRUNNING=True

    clock = pygame.time.Clock()
    while INITRUNNING:
        screen.blit(game_startImg,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                INITRUNNING = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    main()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


def check_3_in_a_row(board):
    global CURRENT_TURN,GAME_RESULT
    
    #check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != 0:
            if row[0] == HUMAN:
                return 1
            elif row[0] == AI:
                return -1
            
    #check columns
    transported_matrix=numpy.transpose(board)
    for row in transported_matrix:
        if len(set(row)) == 1 and row[0] != 0:
            if row[0] == HUMAN:
                return 1
            elif row[0] == AI:
                return -1

    #check horizontal if won
    transported_matrix=numpy.fliplr(board)
    if len(set(numpy.array(board).diagonal())) == 1:
            if board[0][0] == HUMAN:
                return 1
            elif board[0][0] == AI:
                return -1
    if len(set(numpy.array(transported_matrix).diagonal())) == 1:
            if transported_matrix[0][0] == HUMAN:
                return 1
            elif transported_matrix[0][0] == AI:
                return -1
    
    if not any(0 in square for square in board)  :
         return 0
                

def display_game_status():

    if GAME_RESULT == 'INPLAY':
        if CURRENT_TURN == HUMAN:
            msg="Your (\"O\") turn"
        else:
            msg="X's turn"
    else :
        if GAME_RESULT=='WON' :
            msg="Player Won \o/"
        elif GAME_RESULT=='TIE':
            msg='TIE !!!'
        else:
            msg="Player Lost > o<"
    playermsg = font.render(msg, 1, BLACK)
    screen.blit(playermsg, ( Window_weidth/2-playermsg.get_width()/2,(Window_height-TEXTBOX_Y+BUFFER)))

    if GAME_RESULT != 'INPLAY':
        playermsg = font.render('Click to restart', 1, BLACK)
        screen.blit(playermsg, ( Window_weidth/2-playermsg.get_width()/2,(Window_height-TEXTBOX_Y+BUFFER+playermsg.get_height())))

    
def draw_bord():
    pos_x=Window_weidth/3

    for i in range(LINES_PER_ORIANTAION):
        pygame.draw.line(screen, BLACK, (pos_x, BUFFER), (pos_x,Window_height-TEXTBOX_Y-BUFFER), 3)
        pygame.draw.line(screen, BLACK, (BUFFER,pos_x), (Window_height-TEXTBOX_Y-BUFFER,pos_x), 3)

        pos_x *=2

    
    pos_y=((Window_height-TEXTBOX_Y)/3)/2 - xImg.get_height()/2
    for row in GAMEBOARD:
        pos_x=(Window_weidth/3)/2 - (xImg.get_width()/2)
        for column in row:
            if column == HUMAN:
                screen.blit(oImg,(pos_x,pos_y))
            elif column == AI:
                screen.blit(xImg,(pos_x,pos_y))
            pos_x += Window_weidth/3
        pos_y+=(Window_height-TEXTBOX_Y)/3

def next_best_move():
    BEST_SCORE=-math.inf
    BEST_MOVE=()

    for i in range(0,3):
        for j in range(0,3):
            if GAMEBOARD[i][j]==0:
                GAMEBOARD[i][j]=AI
                score = minimax(GAMEBOARD, False)
                GAMEBOARD[i][j]=0
                if (score>BEST_SCORE):
                    BEST_SCORE=score
                    BEST_MOVE=(i,j)
            j+=1
        i+=1
    GAMEBOARD[BEST_MOVE[0]][BEST_MOVE[1]]=AI
    
        


def minimax(board,isMaximizing):
    result=check_3_in_a_row(board)
    if  result is not None:
        return result * -1
    
    if(isMaximizing):
        BEST_SCORE=-math.inf
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j]==0:
                    board[i][j]=AI
                    score = minimax(board, False)
                    board[i][j]=0
                    BEST_SCORE=max(score,BEST_SCORE)
                j+=1
            i+=1
        return BEST_SCORE
    else:
        BEST_SCORE=math.inf
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j]==0:
                    board[i][j]=HUMAN
                    score = minimax(board, True)
                    board[i][j]=0
                    BEST_SCORE=min(score,BEST_SCORE)
                j+=1
            i+=1
        return BEST_SCORE



def main():
    #Variables
    RUNNING=True
    global CURRENT_TURN,GAMEBOARD,GAME_RESULT
    
    clock = pygame.time.Clock()
    while RUNNING:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                #player can't click on text box 
                if mouse_pos[1]<(Window_height-TEXTBOX_Y) and GAME_RESULT == 'INPLAY':
                    gameboard_pos=[math.floor(x/(Window_weidth/3)) for x in mouse_pos]
                    gameboard_pos.reverse()
            
                    if GAMEBOARD[gameboard_pos[0]][gameboard_pos[1]] == 0:
                        if CURRENT_TURN==HUMAN:
                            GAMEBOARD[gameboard_pos[0]][gameboard_pos[1]] = HUMAN
                            CURRENT_TURN=AI

                else:
                    GAMEBOARD=[[0,0,0],[0,0,0],[0,0,0]]
                    GAME_RESULT = 'INPLAY'
                    CURRENT_TURN=HUMAN
                    main()

        screen.fill(BACKGROUND)
        draw_bord()
        
        result=check_3_in_a_row(GAMEBOARD)
        if result is not None:
            if result == 0:
                GAME_RESULT = 'TIE'
            elif result == 1:
                GAME_RESULT = 'WON'
            else:
                GAME_RESULT = 'LOST'
        else:
            if CURRENT_TURN == AI:
                next_best_move()
                CURRENT_TURN=HUMAN
        display_game_status()
        
        

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    
game_start()
