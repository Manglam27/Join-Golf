from tkinter import Button
import pygame

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
mousepossx = 0.0
mousepossy = 0.0
leftpress = False


# loading textures
main_window = pygame.display.set_mode((screensize))
bg = pygame.image.load('res/gif/bg.png')
bg = pygame.transform.scale(bg,(screensize))
ball1 = pygame.image.load('res/gif/golf-ball.png')
ball1 = pygame.transform.scale(ball1,(20,20))

#main game loop
while windowup:
    main_window.blit(bg,(0.0,0.0))
    main_window.blit(ball1,(ball1x , ball1y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            windowup = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                leftpress = True
                print ("left click")
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                leftpress = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

