import pygame
import random
from pygame.locals import *

pygame.init()

width=1000
height=600
screen=pygame.display.set_mode((width,height))

black=0,0,0
white=255,255,255
red=255,0,0
yellow=255,255,0

snake_size_x=50
snake_size_y=50
object_size=80
#snakeface=pygame.image.load('green-head-snake.jpg')
#snakeface=pygame.transform.scale(snakeface,(60,60))

bg_home=pygame.image.load('snake_bg1.png')
bg_home=pygame.transform.scale(bg_home,(width,height))
bg_main=pygame.image.load('snake_bg2.jpg')
bg_main=pygame.transform.scale(bg_main,(width,height))

frog_img=pygame.image.load('frog3.png')
frog_img=pygame.transform.scale(frog_img,(object_size,object_size))
frog_width=frog_img.get_width()
frog_height=frog_img.get_height()

heart=pygame.image.load('red_heart.png')
heart=pygame.transform.scale(heart,(object_size,object_size))
pygame.time.set_timer(USEREVENT,1000)

def snake(snakelist):
    for i in snakelist:
        pygame.draw.rect(screen,black,(i[0],i[1],snake_size_x,snake_size_y))
    #screen.blit(snakeface,(snakelist[-1][0],snakelist[-1][1]))

def gameover(score):
    msg1='Game Over'
    font1=pygame.font.Font('wicked-scary-movie/WickedScaryMovie.ttf',120)
    text1=font1.render(msg1,True,red)
    msg2=f'Your Score:{score}'
    font2=pygame.font.Font('wicked-scary-movie/WickedScaryMovie.ttf',60)
    text2=font2.render(msg2,True,yellow)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(text1,(350,150))
        screen.blit(text2,(390,260))
        pygame.display.update()

def homescreen():
    msg1="Press SPACE to Start"
    font=pygame.font.SysFont('comicsansms',60)
    text1=font.render(msg1,True,yellow)
    msg2="SNAKE GAME"
    font2 = pygame.font.SysFont('comicsansms', 80)
    text2 = font2.render(msg2, True, yellow)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # quit pygame
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game()
        screen.blit(bg_home,(0,0))
        screen.blit(text2,(230,75))
        screen.blit(text1,(190,400))
        pygame.display.update()

def Score(score):
    msg1=f'SCORE:{score}'
    font=pygame.font.Font('wicked-scary-movie/WickedScaryMovie.ttf',60)
    text1=font.render(msg1,True,yellow)
    screen.blit(text1,(200,5))

def timer(seconds):
    msg=f'Time Left : {seconds}'
    font1=pygame.font.Font('wicked-scary-movie/WickedScaryMovie.ttf',60)
    text1=font1.render(msg,True,yellow)
    screen.blit(text1,(700,5))

def heart_show(heart_x,heart_y):
    screen.blit(heart,(heart_x,heart_y))
    heart_rect = pygame.Rect(heart_x, heart_y, object_size, object_size)
    return heart_rect

def game():
    x=0
    y=0
    move_x=0
    move_y=0
    frog_x=random.randint(0,width-frog_width)
    frog_y=random.randint(0,height-frog_height)
    heart_x = random.randint(0, width - object_size)
    heart_y = random.randint(0, height - object_size)
    snakelength=1
    speed=7
    snakelist = []
    score=0
    time_left=30
    seconds=0
    right=True
    left=True
    top=True
    bottom=True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   
                quit()          
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if right:
                        move_x = speed
                        move_y = 0
                        left=False
                        top=True
                        bottom=True
                if event.key == pygame.K_LEFT:
                    if left:
                        move_x = -speed
                        move_y = 0
                        right = False
                        top = True
                        bottom = True
                if event.key == pygame.K_DOWN:
                    if bottom:
                        move_y = speed
                        move_x = 0
                        left = True
                        top = False
                        right = True
                if event.key == pygame.K_UP:
                    if top:
                        move_y = -speed
                        move_x = 0
                        left = True
                        right= True
                        bottom = False
            elif event.type==USEREVENT:
                time_left-=1
                seconds+=1
        #screen.fill(white)
        screen.blit(bg_main,(0,0))
        snake_rect=pygame.Rect(x,y,50,50)
        screen.blit(frog_img,(frog_x,frog_y))
        frog_rect=pygame.Rect(frog_x,frog_y,frog_width,frog_height)
        x+=move_x
        y+=move_y
        snakehead=[]

        snakehead.append(x)
        snakehead.append(y)
        snakelist.append(snakehead)
        

        if len(snakelist)>snakelength:
            del snakelist[0]
        snake(snakelist)

        if snake_rect.colliderect(frog_rect):
            frog_x = random.randint(0, width - frog_width)
            frog_y = random.randint(0, height - frog_height)
            snakelength+=5
            score+=1

        if (time_left<29 and time_left>24)or(time_left>5 and time_left<9):
            heart_rect=heart_show(heart_x,heart_y)
            if heart_rect.colliderect(snake_rect):
                time_left+=10
                heart_x = random.randint(0, width - object_size)
                heart_y = random.randint(0, height - object_size)

        if x>width:
            x=0
        elif x<0:
            x=width
        elif y>height:
            y=0
        elif y<0:
            y=height

        for each in snakelist[:-1]:
            if each==snakelist[-1]:
                gameover(score)
        if time_left<0:
            gameover(score)
        Score(score)
        timer(time_left)

        pygame.display.update()

homescreen()
