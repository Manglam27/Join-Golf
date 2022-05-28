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
hole1x = 100
hole1y = 50

# loading textures :(
main_window = pygame.display.set_mode((screensize))
bg = pygame.image.load('res/gif/bg.png')
bg = pygame.transform.scale(bg,(screensize))
ball1 = pygame.image.load('res/gif/golf-ball.png')
ball1 = pygame.transform.scale(ball1,(bscale1,bscale2))
hole1 = pygame.image.load('res/gif/hole.png')
hole1 = pygame.transform.scale(hole1,(25,25))
dark_box = pygame.image.load('res/gif/tile64_dark.png')
ball1rect = pygame.Rect(ball1y,ball1x,20,20)

#main game loop :>
while windowup:
    main_window.blit(bg,(0.0,0.0))
    main_window.blit(hole1,(hole1y,hole1x))
    main_window.blit(ball1,(ball1y , ball1x))
    main_window.blit(dark_box,(0,0))

    pygame.draw.rect(main_window,(255,0,0),ball1rect)

    

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
        pygame.transform.scale(ball1(bscale1,bscale2))
        if bscale1 == 0 and bscale2 == 0 :
            print("khatam tata goodbye")
        else:   
            bscale2 = 0.1
            bscale1 = 0.1


    # no escap from border :)

    if ball1rect.right >= width/2 or ball1rect.left <= 0:
        velocityy *= -1
    if ball1rect.bottom >= hight or ball1rect.top <= 0:
        velocityx *= -1

    # if ball1y > 380:
    #     velocityy *= -1
    # if ball1x > 580:
    #     velocityx *= -1
    # if ball1y < 0:
    #     velocityy *= -1     
    # if ball1x < 0:
    #     velocityx *= -1


    # print(velocitymulti)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

