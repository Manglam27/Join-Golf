from pip import main
import pygame
import math


pygame.init()

#Global variables
windowup = True
clock = pygame.time.Clock()
width = 800.0
hight = 600.0
screensize = (width,hight)
ball1x = 500.0
ball1y = 200.0
bscale1 = 20.0
bscale2 = 20.0
initmousepossx = 0.0
initmousepossy = 0.0
initmouseposs = [initmousepossy,initmousepossx]
mousepossx = 0.0
mousepossy = 0.0
mouseposs = [mousepossy,mousepossx]
leftpress = False
velocityx = 0.0
velocityy = 0.0
velocity1d = 0.0 
velocitymulti = 0.0
hole1x = 0.0
hole1y = 0.0
dark_boxx = 0.0
dark_boxy = 0.0

# loading textures :(
main_window = pygame.display.set_mode((screensize))
bg = pygame.image.load('res/gif/bg.png')
bg = pygame.transform.scale(bg,(screensize))
ball1 = pygame.image.load('res/gif/golf-ball.png')
ball1 = pygame.transform.scale(ball1,(bscale1,bscale2))
hole1 = pygame.image.load('res/gif/hole.png')
hole1 = pygame.transform.scale(hole1,(25,25))
dark_box = pygame.image.load('res/gif/tile64_dark.png')
dark_box = pygame.transform.scale(dark_box,(64,64))
ball1rect = pygame.Rect(ball1y,ball1x,20,20)




#main game loop :>
while windowup:
    main_window.blit(bg,(0.0,0.0))
    hole1x= 35
    hole1y = 100
    main_window.blit(hole1,(hole1y,hole1x))
    main_window.blit(ball1,(ball1y , ball1x))
    dark_boxx = 35
    dark_boxy = 100
    boxrect = pygame.Rect(dark_boxy,dark_boxx,64,64)
    main_window.blit(dark_box,(dark_boxy,dark_boxx))
    # pygame.draw.rect(main_window,(255,0,0),boxrect)


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            windowup = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if event.button == 1:
                leftpress = True
                initmousepossy,initmousepossx = pygame.mouse.get_pos()
                initmouseposs = [initmousepossy,initmousepossx]
                print ("left click")
                
                
                
        if event.type == pygame.MOUSEBUTTONUP:
            
            if event.button == 1:
                
                mousepossy,mousepossx = pygame.mouse.get_pos()
                velocityx = (initmousepossx-mousepossx)/-50
                velocityy = (initmousepossy-mousepossy)/-50
                leftpress = False
                velocity1d = math.sqrt(pow(abs(velocityx),2)+pow(abs(velocityy),2))
    
    if leftpress == True:
        if velocitymulti < 5:
            velocitymulti += .1
    
    if(velocity1d>0):
        velocity1d -= 0.1
        ball1y += (velocitymulti*(-velocityy))
        ball1rect.x = ball1y
        ball1x += (velocitymulti*(-velocityx))
        ball1rect.y = ball1x
        if velocity1d < 0:
            velocitymulti = 0.0
    
    #hole test
    if ball1x+2 > hole1x and ball1x + 16 < hole1x + 25 and ball1y + 4 > hole1y and ball1y + 16 < hole1y+25 :
        print ("won")
    
        print("khatam tata goodbye")
 


    # no escap from border :)

    if pygame.Rect.colliderect(ball1rect,boxrect):
        velocityy *= -1
        velocityx *= -1
    
    if ball1rect.right >= width/2 or ball1rect.left <= 0:
        velocityy *= -1
    if ball1rect.bottom >= hight or ball1rect.top <= 0:
        velocityx *= -1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

