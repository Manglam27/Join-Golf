import pygame
from pygame import KEYDOWN, mixer
import math


pygame.init()
pygame.mixer.init()


# Global variables
windowup = True

clock = pygame.time.Clock()

width = 800.0
hight = 600.0
screensize = (width, hight)

win = False
levelno = 1

showball1 = True
showball2 = True


ball1x = 500.0
ball1y = 180.0
ball2x = 500.0
ball2y = 580.0

hole1x = 35
hole1y = 180
hole2x = 35
hole2y = 580

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

arraybox = []
arraybox2 = []
boxno = 0
box2no = 0

# loading textures :(

main_window = pygame.display.set_mode((screensize))

font = pygame.font.Font('freesansbold.ttf', 32)

start = pygame.image.load('res/gif/start.png')
start = pygame.transform.scale(start, (screensize))
bg = pygame.image.load('res/gif/bg.png')
bg = pygame.transform.scale(bg, (screensize))
bg2 = pygame.image.load('res/gif/bg2.png')
bg2 = pygame.transform.scale(bg2, (screensize))

ball1 = pygame.image.load('res/gif/golf-ball.png')
ball1 = pygame.transform.scale(ball1, (20, 20))
ball1rect = pygame.Rect(0, 0, 20, 20)

ball2 = pygame.image.load('res/gif/golf-ball.png')
ball2 = pygame.transform.scale(ball2, (20, 20))
ball2rect = pygame.Rect(0, 0, 20, 20)

hole = pygame.image.load('res/gif/hole.png')
hole = pygame.transform.scale(hole, (25, 25))

dark_box = pygame.image.load('res/gif/tile64_dark.png')
dark_box = pygame.transform.scale(dark_box, (64, 64))

light_box = pygame.image.load('res/gif/tile64_light.png')
light_box = pygame.transform.scale(light_box, (64, 64))

pygame.display.set_caption("Join-Golf")
icon = pygame.image.load('res/gif/icon.png')
pygame.display.set_icon(icon)

point = pygame.image.load('res/gif/point.png')

powermeterbg = pygame.image.load('res/gif/powermeter_bg.png')
powermeterfg = pygame.image.load('res/gif/powermeter_fg.png')
powermeterover = pygame.image.load('res/gif/powermeter_overlay.png')

# loading music

holesound = mixer.Sound('res/sfx/hole.wav')
movingsound = mixer.Sound('res/sfx/swing.wav')

# loding font

myfont = pygame.font.Font('res/font/ComicNeue-Bold.ttf', 30)

a = 0
# some more functions

# level


def level():
    global a,powermeterfg,arraybox, box2no, boxno, arraybox2, initmousepossy, initmousepossx, levelno, hole1y, hole2x, hole2y, hole1x, showball1, showball2, ball1rect, ball2rect, ball2y, ball2x, leftpress, ball1x, ball1y, velocity2y, velocity2x, velocityx, velocityy, velocitymulti, velocity1d

    if levelno == 1:
        text = font.render(str("Level 1"), True, (0, 0, 0), None)
        main_window.blit(text, (350, 0))

        main_window.blit(hole, (hole1y, hole1x))
        main_window.blit(hole, (hole2y, hole2x))
        if showball1:
            main_window.blit(ball1, (ball1y, ball1x))
        else:
            ball1x = 0.0
            ball1y = 0.0

        if showball2:
            main_window.blit(ball2, (ball2y, ball2x))
        else:
            ball2x = 0.0
            ball2y = 0.0

        arraybox.append(pygame.Rect(1, 250, 64, 64))
        main_window.blit(dark_box, (1, 250))
        arraybox.append(pygame.Rect(68, 250, 64, 64))
        main_window.blit(dark_box, (68, 250))
        arraybox.append(pygame.Rect(336, 250, 64, 64))
        main_window.blit(dark_box, (336, 250))
        arraybox.append(pygame.Rect(270, 250, 64, 64))
        main_window.blit(dark_box, (270, 250))

        arraybox2.append(pygame.Rect(530, 150, 64, 64))
        main_window.blit(light_box, (530, 150))
        arraybox2.append(pygame.Rect(596, 150, 64, 64))
        main_window.blit(light_box, (596, 150))

        boxno = 4
        box2no = 2

        if showball1 == False and showball2 == False:
            levelno += 1
            boxno = 0
            box2no = 0
            arraybox.clear()
            arraybox2.clear()
            ball1x = 500.0
            ball1y = 200.0
            ball2x = 500.0
            ball2y = 600.0
            velocityy = 0
            velocityx = 0
            velocity2y = 0
            velocity2x = 0
            showball1 = True
            showball2 = True
            hole1x = 40
            hole1y = 80
            hole2x = 150
            hole2y = 500

    elif levelno == 2:
        text = font.render(str("Level 2"), True, (0, 0, 0), None)
        main_window.blit(text, (350, 0))

        main_window.blit(hole, (hole1y, hole1x))
        main_window.blit(hole, (hole2y, hole2x))

        if showball1:
            main_window.blit(ball1, (ball1y, ball1x))
        else:
            ball1x = 0.0
            ball1y = 0.0
        if showball2:
            main_window.blit(ball2, (ball2y, ball2x))
        else:
            ball2x = 0.0
            ball2y = 0.0

        arraybox.append(pygame.Rect(100, 130, 64, 64))
        main_window.blit(dark_box, (100, 130))
        arraybox.append(pygame.Rect(300, 130, 64, 64))
        main_window.blit(dark_box, (300, 130))
        arraybox.append(pygame.Rect(250, 230, 64, 64))
        main_window.blit(dark_box, (250, 230))
        arraybox.append(pygame.Rect(50, 330, 64, 64))
        main_window.blit(dark_box, (50, 330))

        arraybox2.append(pygame.Rect(700, 100, 64, 64))
        main_window.blit(light_box, (700, 100))
        arraybox2.append(pygame.Rect(434, 260, 64, 64))
        main_window.blit(light_box, (434, 260))
        arraybox2.append(pygame.Rect(500, 260, 64, 64))
        main_window.blit(light_box, (500, 260))
        boxno = 4
        box2no = 3

        if showball1 == False and showball2 == False:
            levelno += 1
            boxno = 0
            box2no = 0
            arraybox.clear()
            arraybox2.clear()
            ball1x = 500.0
            ball1y = 200.0
            ball2x = 100.0
            ball2y = 600.0
            velocityy = 0
            velocityx = 0
            velocity2y = 0
            velocity2x = 0
            showball1 = True
            showball2 = True
            hole1x = 100
            hole1y = 200
            hole2x = 500
            hole2y = 600

    elif levelno == 3:
        text = font.render(str("Level 3"), True, (0, 0, 0), None)
        main_window.blit(text, (350, 0))

        main_window.blit(hole, (hole1y, hole1x))
        main_window.blit(hole, (hole2y, hole2x))
        if showball1:
            main_window.blit(ball1, (ball1y, ball1x))
        else:
            ball1x = 0.0
            ball1y = 0.0

        if showball2:
            main_window.blit(ball2, (ball2y, ball2x))
        else:
            ball2x = 0.0
            ball2y = 0.0

        arraybox.append(pygame.Rect(200, 200, 64, 64))
        main_window.blit(dark_box, (200, 200))
        arraybox.append(pygame.Rect(130, 200, 64, 64))
        main_window.blit(dark_box, (130, 200))

        arraybox2.append(pygame.Rect(540, 300, 64, 64))
        main_window.blit(light_box, (540, 300))
        arraybox2.append(pygame.Rect(606, 300, 64, 64))
        main_window.blit(light_box, (606, 300))

        boxno = 2
        box2no = 2

        if showball1 == False and showball2 == False:
            levelno += 1
            boxno = 0
            box2no = 0
            arraybox.clear()
            arraybox2.clear()
            ball1x = 100.0
            ball1y = 200.0
            ball2x = 100.0
            ball2y = 600.0
            velocityy = 0
            velocityx = 0
            velocity2y = 0
            velocity2x = 0
            showball1 = True
            showball2 = True
            hole1x = 500
            hole1y = 200
            hole2x = 500
            hole2y = 600

    elif levelno == 4:
        text = font.render(str("Level 4"), True, (0, 0, 0), None)
        main_window.blit(text, (350, 0))

        main_window.blit(hole, (hole1y, hole1x))
        main_window.blit(hole, (hole2y, hole2x))
        if showball1:
            main_window.blit(ball1, (ball1y, ball1x))
        else:
            ball1x = 0.0
            ball1y = 0.0

        if showball2:
            main_window.blit(ball2, (ball2y, ball2x))
        else:
            ball2x = 0.0
            ball2y = 0.0

        arraybox.append(pygame.Rect(306, 100, 64, 64))
        main_window.blit(dark_box, (306, 100))
        arraybox.append(pygame.Rect(30, 164, 64, 64))
        main_window.blit(dark_box, (30, 164))
        arraybox.append(pygame.Rect(306, 228, 64, 64))
        main_window.blit(dark_box, (306, 228))
        arraybox.append(pygame.Rect(30, 292, 64, 64))
        main_window.blit(dark_box, (30, 292))
        arraybox.append(pygame.Rect(306, 356, 64, 64))
        main_window.blit(dark_box, (306, 356))
        arraybox.append(pygame.Rect(30, 420, 64, 64))
        main_window.blit(dark_box, (30, 420))

        arraybox2.append(pygame.Rect(734, 180, 64, 64))
        main_window.blit(light_box, (734, 180))
        arraybox2.append(pygame.Rect(668, 180, 64, 64))
        main_window.blit(light_box, (668, 180))
        arraybox2.append(pygame.Rect(602, 180, 64, 64))
        main_window.blit(light_box, (602, 180))
        arraybox2.append(pygame.Rect(536, 180, 64, 64))
        main_window.blit(light_box, (536, 180))
        arraybox2.append(pygame.Rect(402, 350, 64, 64))
        main_window.blit(light_box, (402, 350))
        arraybox2.append(pygame.Rect(466, 350, 64, 64))
        main_window.blit(light_box, (468, 350))
        arraybox2.append(pygame.Rect(602, 350, 64, 64))
        main_window.blit(light_box, (602, 350))
        arraybox2.append(pygame.Rect(536, 350, 64, 64))
        main_window.blit(light_box, (536, 350))

        boxno = 6
        box2no = 8

        if showball1 == False and showball2 == False:
            levelno += 1
            boxno = 0
            box2no = 0
            arraybox.clear()
            arraybox2.clear()
            ball1x = 510.0
            ball1y = 100.0
            ball2x = 500.0
            ball2y = 700.0
            velocityy = 0
            velocityx = 0
            velocity2y = 0
            velocity2x = 0
            showball1 = True
            showball2 = True
            hole1x = 100
            hole1y = 300
            hole2x = 500
            hole2y = 500

    elif levelno == 5:
        text = font.render(str("Level 5"), True, (0, 0, 0), None)
        main_window.blit(text, (350, 0))

        main_window.blit(hole, (hole1y, hole1x))
        main_window.blit(hole, (hole2y, hole2x))
        if showball1:
            main_window.blit(ball1, (ball1y, ball1x))
        else:
            ball1x = 0.0
            ball1y = 0.0

        if showball2:
            main_window.blit(ball2, (ball2y, ball2x))
        else:
            ball2x = 0.0
            ball2y = 0.0

        arraybox.append(pygame.Rect(334, 228, 64, 64))
        main_window.blit(dark_box, (334, 228))
        arraybox.append(pygame.Rect(268, 228, 64, 64))
        main_window.blit(dark_box, (268, 228))
        arraybox.append(pygame.Rect(202, 228, 64, 64))
        main_window.blit(dark_box, (202, 228))
        arraybox.append(pygame.Rect(6, 228, 64, 64))
        main_window.blit(dark_box, (6, 228))
        arraybox.append(pygame.Rect(72, 228, 64, 64))
        main_window.blit(dark_box, (72, 228))

        arraybox2.append(pygame.Rect(580, 530, 64, 64))
        main_window.blit(light_box, (580, 530))
        arraybox2.append(pygame.Rect(580, 464, 64, 64))
        main_window.blit(light_box, (580, 464))
        arraybox2.append(pygame.Rect(580, 398, 64, 64))
        main_window.blit(light_box, (580, 398))
        arraybox2.append(pygame.Rect(580, 332, 64, 64))
        main_window.blit(light_box, (580, 332))
        arraybox2.append(pygame.Rect(580, 6, 64, 64))
        main_window.blit(light_box, (580, 6))
        arraybox2.append(pygame.Rect(580, 72, 64, 64))
        main_window.blit(light_box, (580, 72))
        arraybox2.append(pygame.Rect(580, 138, 64, 64))
        main_window.blit(light_box, (580, 138))

        boxno = 5
        box2no = 7

        if showball1 == False and showball2 == False:
            levelno += 1
            ball1x = 00.0
            ball1y = 00.0
            ball2x = 00.0
            ball2y = 00.0
            velocityy = 0
            velocityx = 0
            velocity2y = 0
            velocity2x = 0
            showball1 = True
            showball2 = True

    else:
        end()

#################################################################################################

    if (ball1x + 2 > hole1x and ball1x + 11 < hole1x + 25 and ball1y + 6 > hole1y and ball1y + 11 < hole1y+20):
        showball1 = False
        holesound.play()

    if (ball2x + 2 > hole2x and ball2x + 11 < hole2x + 25 and ball2y + 6 > hole2y and ball2y + 11 < hole2y+20):
        showball2 = False
        holesound.play()


    if (leftpress == True):
        
        if velocitymulti < 7:
            velocitymulti += .12
            a+=1
            powermeterfg = pygame.transform.scale(powermeterfg,(8,a))

        mousepossy, mousepossx = pygame.mouse.get_pos()
        angle = math.atan2(initmousepossy-mousepossy,
                           mousepossx-initmousepossx)*180 / math.pi
        point2 = pygame.transform.rotate(point, -1*(angle))

        if (showball1 == True):
            main_window.blit(powermeterbg,(ball1y+40,ball1x-60))
            main_window.blit(powermeterfg,(ball1y+42,ball1x-57))        
            main_window.blit(powermeterover,(ball1y+40,ball1x-60))        
            main_window.blit(point2, ((ball1y+10)-int(point2.get_width()/2), (ball1x+10)-int(point2.get_height()/2)))


        if (showball2 == True):
            main_window.blit(powermeterbg,(ball2y+40,ball2x-60))
            main_window.blit(powermeterfg,(ball2y+42,ball2x-57))        
            main_window.blit(powermeterover,(ball2y+40,ball2x-60)) 

            main_window.blit(point2, ((ball2y+10)-int(point2.get_width()/2), (ball2x+10)-int(point2.get_height()/2)))
        
    if(velocity1d > 0):
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
            a=0

    # no escap 

    for i in range(boxno):
        if pygame.Rect.colliderect(ball1rect, arraybox[i]):
            velocityy *= -1
            velocityx *= -1
    for i in range(box2no):
        if pygame.Rect.colliderect(ball2rect, arraybox2[i]):
            velocity2y *= -1
            velocity2x *= -1

    if ball1rect.right >= width/2 or ball1rect.left <= 0:
        velocityy *= -1
    if ball1rect.bottom >= hight or ball1rect.top <= 0:
        velocityx *= -1

    if ball2rect.right >= width or ball2rect.left <= width/2:
        velocity2y *= -1
    if ball2rect.bottom >= hight or ball2rect.top <= 0:
        velocity2x *= -1

    # events


def events():
    global windowup, clk, leftpress, initmousepossy, initmousepossx, mousepossy, mousepossx, velocity1d, velocity2x, velocity2y, velocityy, velocityx

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            windowup = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:
                leftpress = True
                initmousepossy, initmousepossx = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:

            if event.button == 1:
                mousepossy, mousepossx = pygame.mouse.get_pos()
                velocityx = (initmousepossx-mousepossx)/-150
                velocityy = (initmousepossy-mousepossy)/-150
                velocity2x = velocityx
                velocity2y = velocityy
                leftpress = False
                velocity1d = math.sqrt(
                    pow(abs(velocityx), 2)+pow(abs(velocityy), 2))
                movingsound.play()
                clk += 1

    # main game loop :>
up = True


def main():
    while windowup:
        main_window.blit(bg, (0.0, 0.0))
        events()
        level()
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)


def end():
    global clk, myfont
    up = True
    while up:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                up = False
                pygame.quit()
            if event.type == KEYDOWN:
                up = False
                pygame.quit()
        txt = myfont.render(str("Game Over :)"), True, (0, 0, 0), None)
        text = myfont.render(
            str("you have finished game in : "), True, (0, 0, 0), None)
        text2 = myfont.render(str(clk), True, (255, 0, 0), None)
        text3 = myfont.render(str("Moves "), True, (0, 0, 0), None)
        text4 = myfont.render('Press any key to Exit', True, (0, 0, 0), None)
        main_window.blit(bg2, (0.0, 0.0))
        main_window.blit(txt, (280, 100))
        main_window.blit(text, (150, 240))
        main_window.blit(text2, (520, 240))
        main_window.blit(text3, (565, 240))
        main_window.blit(text4, (240, 370))

        pygame.display.flip()
        pygame.display.update()
# main game function :)


while up:
    main_window.blit(start, (0, 0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            up = False
            main()
        if event.type == pygame.QUIT:
            up = False
            pygame.quit()

    pygame.display.flip()
    pygame.display.update()
