import pygame
from pygame import mixer
import math

pygame.init()
pygame.mixer.init()

#Global variables
windowup = True

clock = pygame.time.Clock()

width = 800.0
hight = 600.0
screensize = (width,hight)

win = False
levelno = 1

showball1 = True
showball2 = True


ball1x = 500.0
ball1y = 180.0
ball2x = 500.0
ball2y = 580.0

initmousepossx = 0.0
initmousepossy = 0.0
mousepossx = 0.0
mousepossy = 0.0

leftpress = False
clk = 0

velocityx = 0.0
velocityy = 0.0
velocity2x = 0.0
velocity2y = 0.0
velocity1d = 0.0 
velocitymulti = 0.0

# loading textures :(

main_window = pygame.display.set_mode((screensize))

font = pygame.font.Font('freesansbold.ttf', 32)

bg = pygame.image.load('res/gif/bg.png')
bg = pygame.transform.scale(bg,(screensize))
bg2 = pygame.image.load('res/gif/bg2.png')
bg2 = pygame.transform.scale(bg2,(screensize))

ball1 = pygame.image.load('res/gif/golf-ball.png')
ball1 = pygame.transform.scale(ball1,(20,20))
ball1rect = pygame.Rect(0,0,20,20)

ball2 = pygame.image.load('res/gif/golf-ball.png')
ball2 = pygame.transform.scale(ball2,(20,20))
ball2rect = pygame.Rect(0,0,20,20)

hole = pygame.image.load('res/gif/hole.png')
hole = pygame.transform.scale(hole,(25,25))

dark_box = pygame.image.load('res/gif/tile64_dark.png')
dark_box = pygame.transform.scale(dark_box,(64,64))

light_box = pygame.image.load('res/gif/tile64_light.png')
light_box = pygame.transform.scale(light_box,(64,64))

pygame.display.set_caption("Mini-Golf")
icon = pygame.image.load('res/gif/icon.png')
pygame.display.set_icon(icon)

#loading music
holesound = mixer.Sound('res/sfx/hole.wav')
movingsound = mixer.Sound('res/sfx/swing.wav')



box = pygame.Rect
box1 = pygame.Rect
lbox = pygame.Rect


# some more functions 

    #level 

def level():
    global levelno,lbox,box1,box,showball1,showball2,ball1rect,ball2rect,ball2y,ball2x,leftpress,ball1x,ball1y,velocity2y,velocity2x,velocityx,velocityy,velocitymulti,velocity1d


    if levelno == 1:
        text = font.render( str("Level 1"), True ,(255,255,255),None)
        main_window.blit(text,(350,0))
        hole1x = 35
        hole1y = 180
        hole2x = 35
        hole2y = 580

        main_window.blit(hole,(hole1y,hole1x))
        main_window.blit(hole,(hole2y,hole2x))
        if showball1:
            main_window.blit(ball1,(ball1y , ball1x))
        else:
            ball1x = 0.0
            ball1y = 0.0
           
        if showball2:
            main_window.blit(ball2,(ball2y , ball2x))
        else:
            ball2x = 0.0
            ball2y = 0.0

        if showball1 == False and showball2 == False:
            levelno += 1
            ball1x = 500.0
            ball1y = 200.0
            ball2x = 500.0
            ball2y = 600.0
            showball1 = True
            showball2 = True

        box = pygame.Rect(50,200,64,64)
        main_window.blit(dark_box,(50,200))
       
        box1 = pygame.Rect(100,100,64,64)
        main_window.blit(dark_box,(100,100))

        light_boxx = 100
        light_boxy = 500
        lbox = pygame.Rect(light_boxy,light_boxx,64,64)
        main_window.blit(light_box,(light_boxy,light_boxx))

        if (ball1x + 2 > hole1x and ball1x + 11 < hole1x + 25 and ball1y + 6 > hole1y and ball1y + 11 < hole1y+20):
            showball1 = False
            holesound.play()

        if (ball2x + 2 > hole2x and ball2x + 11 < hole2x + 25 and ball2y + 6 > hole2y and ball2y + 11 < hole2y+20):
            showball2 = False
            holesound.play()

    elif levelno == 2:
        text = font.render( str("Level 2"), True , (255,255,255),None)
        main_window.blit(text,(350,0))
        hole1x = 50
        hole1y = 100
        hole2x = 200
        hole2y = 500

        main_window.blit(hole,(hole1y,hole1x))
        main_window.blit(hole,(hole2y,hole2x))
        if showball1:
            main_window.blit(ball1,(ball1y , ball1x))
        if showball2:
            main_window.blit(ball2,(ball2y , ball2x))
        if showball1 == False and showball2 == False:
            levelno += 1
            ball1x = 500.0
            ball1y = 200.0
            ball2x = 500.0
            ball2y = 600.0
            
        box = pygame.Rect(50,100,64,64)
        main_window.blit(dark_box,(50,100))
       
        box1 = pygame.Rect(100,200,64,64)
        main_window.blit(dark_box,(100,200))

        light_boxx = 100
        light_boxy = 700
        lbox = pygame.Rect(light_boxy,light_boxx,64,64)
        main_window.blit(light_box,(light_boxy,light_boxx))

        if (ball1x + 2 > hole1x and ball1x + 11 < hole1x + 25 and ball1y + 6 > hole1y and ball1y + 11 < hole1y+20):
            showball1 = False
            holesound.play()

        if (ball2x + 2 > hole2x and ball2x + 11 < hole2x + 25 and ball2y + 6 > hole2y and ball2y + 11 < hole2y+20):
            showball2 = False
            holesound.play()
    
    else:
        txt = font.render( str("Game Over :)"), True , (0,0,0),None)
        text = font.render( str("you have finished game in : "), True , (0,0,0),None)
        text2 = font.render( str(clk), True , (255,0,0),None)
        text3 = font.render( str("Moves "), True , (0,0,0),None)
        main_window.blit(bg2,(0.0,0.0))
        main_window.blit(txt,(280,100))
        main_window.blit(text,(100,240))
        main_window.blit(text2,(540,240))
        main_window.blit(text3,(595,240))
        

#################################################################################################
    
    if leftpress == True:
        if velocitymulti < 5:
            velocitymulti += .1
    if(velocity1d>0): 
        velocity1d -= .1
        ball1y += (velocitymulti*(-velocityy))
        ball1rect.x = ball1y
        ball1x += (velocitymulti*(-velocityx))
        ball1rect.y = ball1x

        ball2y += (velocitymulti*(-velocity2y))
        ball2rect.x = ball2y
        ball2x += (velocitymulti*(-velocity2x))
        ball2rect.y = ball2x

        
        if velocity1d < 0:

            velocitymulti = 0.0

    # no escap from border :)

    if pygame.Rect.colliderect(ball1rect,box) or pygame.Rect.colliderect(ball1rect,box1):
        velocityy *= -1
        velocityx *= -1
    if pygame.Rect.colliderect(ball2rect,lbox):
        velocity2y *= -1
        velocity2x *= -1
    
    if ball1rect.right >= width/2 or ball1rect.left <= 0:
        velocityy *= -1
    if ball1rect.bottom >= hight or ball1rect.top <= 0:
        velocityx *= -1

    if ball2rect.right >= width or ball2rect.left <= width/2 :
        velocity2y *= -1
    if ball2rect.bottom >= hight or ball2rect.top <= 0:
        velocity2x *= -1
    
    
    
    #events

def events():
    global windowup ,clk,leftpress,initmousepossy,initmousepossx,mousepossy,mousepossx,velocity1d,velocity2x,velocity2y,velocityy,velocityx

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            windowup = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if event.button == 1:
                leftpress = True
                initmousepossy,initmousepossx = pygame.mouse.get_pos()       
        if event.type == pygame.MOUSEBUTTONUP:
            
            if event.button == 1:
                mousepossy,mousepossx = pygame.mouse.get_pos()
                velocityx = (initmousepossx-mousepossx)/-50
                velocityy = (initmousepossy-mousepossy)/-50
                velocity2x = velocityx
                velocity2y = velocityy
                leftpress = False
                velocity1d = math.sqrt(pow(abs(velocityx),2)+pow(abs(velocityy),2))
                movingsound.play()

                clk += 1 
    
    #main game loop :>
def main():
    while windowup:
        main_window.blit(bg,(0.0,0.0))
        events()
        level()
        pygame.display.flip()
        clock.tick(60)



# main game function :)

main()
