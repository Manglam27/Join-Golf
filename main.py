from turtle import screensize, width
import pygame

pygame.init()

#Global variables
windowup = True
clock = pygame.time.Clock()
width = 800
hight = 600
screensize = (width,hight)

# loading textures
main_window = pygame.display.set_mode((screensize))
bg = pygame.image.load('res/gif/bg.png')
bg = pygame.transform.scale(bg,(screensize))

while windowup:
    main_window.blit(bg,(0.0,0.0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            windowup = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

