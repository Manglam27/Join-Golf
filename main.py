import pygame
import math


pygame.init()

#Global variables
windowup = True
clock = pygame.time.Clock()
width = 800.0
hight = 600.0
screensize = (width,hight)
ball1x = 52.0
ball1y = 51.0
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

# loading textures
main_window = pygame.display.set_mode((screensize))
bg = pygame.image.load('res/gif/bg.png')
bg = pygame.transform.scale(bg,(screensize))
ball1 = pygame.image.load('res/gif/golf-ball.png')
ball1 = pygame.transform.scale(ball1,(20,20))

#main game loop
while windowup:
    main_window.blit(bg,(0.0,0.0))
    main_window.blit(ball1,(ball1y , ball1x))
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
                velocityx = (initmousepossx-mousepossx)/-100
                velocityy = (initmousepossy-mousepossy)/-100
                leftpress = False
                velocity1d = math.sqrt(pow(abs(velocityx),2)+pow(abs(velocityy),2))
    
    if leftpress == True:
        if velocitymulti < 5:
            velocitymulti += .1
    
    if(velocity1d>0):
        velocity1d -= 0.1
        ball1y += (velocitymulti*(-velocityy))
        ball1x += (velocitymulti*(-velocityx))
        if velocity1d < 0:
            velocitymulti = 0.0
            
    print(velocitymulti)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

