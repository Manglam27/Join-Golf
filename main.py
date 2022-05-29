import pygame
import math

pygame.init()

# some more functions 

    #level 

def level():
    global levelno,ball1rect,ball2rect,ball2y,ball2x,leftpress,ball1x,ball1y,hole1x,hole1y,velocity2y,velocity2x,velocityx,velocityy,velocitymulti,velocity1d,dark_box,dark_boxx,dark_boxy

    if levelno == 1:
        hole1x= 35
        hole1y = 100
        main_window.blit(hole1,(hole1y,hole1x))
        main_window.blit(ball1,(ball1y , ball1x))
        main_window.blit(ball2,(ball2y , ball2x))
        dark_boxx = 35
        dark_boxy = 100
        darkboxrect = pygame.Rect(dark_boxy,dark_boxx,64,64)
        main_window.blit(dark_box,(dark_boxy,dark_boxx))
    
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

    if pygame.Rect.colliderect(ball1rect,darkboxrect):
        velocityy *= -1
        velocityx *= -1
    
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
    global windowup ,leftpress,initmousepossy,initmousepossx,mousepossy,mousepossx,velocity1d,velocity2x,velocity2y,velocityy,velocityx

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            windowup = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if event.button == 1:
                leftpress = True
                initmousepossy,initmousepossx = pygame.mouse.get_pos()
                print ("left click")        
        if event.type == pygame.MOUSEBUTTONUP:
            
            if event.button == 1:
                mousepossy,mousepossx = pygame.mouse.get_pos()
                velocityx = (initmousepossx-mousepossx)/-50
                velocityy = (initmousepossy-mousepossy)/-50
                velocity2x = velocityx
                velocity2y = velocityy
                leftpress = False
                velocity1d = math.sqrt(pow(abs(velocityx),2)+pow(abs(velocityy),2))
    
    #main game loop :>
def main():
    while windowup:
        main_window.blit(bg,(0.0,0.0))
        events()
        level()
        pygame.display.flip()
        clock.tick(60)

#Global variables
windowup = True

clock = pygame.time.Clock()

width = 800.0
hight = 600.0
screensize = (width,hight)

levelno = 1


ball1x = 500.0
ball1y = 200.0
ball2x = 500.0
ball2y = 600.0

initmousepossx = 0.0
initmousepossy = 0.0
mousepossx = 0.0
mousepossy = 0.0


leftpress = False

velocityx = 0.0
velocityy = 0.0
velocity2x = 0.0
velocity2y = 0.0
velocity1d = 0.0 
velocitymulti = 0.0

hole1x = 0.0
hole1y = 0.0

dark_boxx = 0.0
dark_boxy = 0.0

light_boxx = 0.0
light_boxy = 0.0

# loading textures :(

main_window = pygame.display.set_mode((screensize))
bg = pygame.image.load('res/gif/bg.png')
bg = pygame.transform.scale(bg,(screensize))

ball1 = pygame.image.load('res/gif/golf-ball.png')
ball1 = pygame.transform.scale(ball1,(20,20))
ball1rect = pygame.Rect(0,0,20,20)

ball2 = pygame.image.load('res/gif/golf-ball.png')
ball2 = pygame.transform.scale(ball2,(20,20))
ball2rect = pygame.Rect(0,0,20,20)

hole1 = pygame.image.load('res/gif/hole.png')
hole1 = pygame.transform.scale(hole1,(25,25))

dark_box = pygame.image.load('res/gif/tile64_dark.png')
dark_box = pygame.transform.scale(dark_box,(64,64))
darkboxrect = pygame.Rect(dark_boxy,dark_boxx,64,64)


light_box = pygame.image.load('res/gif/tile64_light.png')
light_box = pygame.transform.scale(light_box,(64,64))
lightboxrect = pygame.Rect(light_boxy,light_boxx,64,64)



# main game function :)

main()
