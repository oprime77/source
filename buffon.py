# bug occured

import pygame, sys, os
import random
from pygame.locals import *
from math import *

# user define
count = 200000
barLength = 300  # of bar
width = 600  # display size
lineSize = 400
lineQuantity = 2


def DrawLine():
    for i in line_locations:
        pygame.draw.line(screen, (255, 0, 0, 255), (barBeginX, i), (barEndX, i), 1)

    pygame.display.flip()


def Input(events):
    for event in events:
        if event.type == QUIT:
            sys.exit(0)
        else:
            print(event)


def GetRotatingLocation(x, y):
    angle = random.randrange(0, 360)
    x = barLength * cos(radians(angle))
    y = barLength * sin(radians(angle))
    return int(x), int(y)


def GetRandomColor():
    red = random.randrange(0, 255)
    green = random.randrange(0, 255)
    blue = random.randrange(0, 255)
    return (red, green, blue)


# automatic setting
barBeginX = 0
barEndX = width
height = 2 * barLength * (lineQuantity - 1)  # display size
info_height = 50

pygame.init()
pygame.display.set_caption('line picker')
font = pygame.font.SysFont("Arial", 20, 0, 0)
window = pygame.display.set_mode((width, height + info_height))
screen = pygame.display.get_surface()
screen.fill((255, 255, 255))

# memorize location of lines
line_locations = []
i = 0
while i <= (lineQuantity - 1):
    line_locations.append(2 * barLength * i)
    i += 1

pygame.display.flip()

i = 0
check = 0
while True:
    Input(pygame.event.get())

    if i >= count:
        continue

    i += 1
    # put bar randomly
    beginX = random.randrange(0, width)
    beginY = random.randrange(0, height)
    endX, endY = GetRotatingLocation(beginX, beginY)
    endX += beginX
    endY += beginY

    pygame.draw.line(screen, GetRandomColor(), (beginX, beginY), (endX, endY), 2)
    DrawLine()

    # check bar count over line
    if beginY > endY:
        beginY, endY = endY, beginY

    for loc in line_locations:
        if beginY <= loc and endY >= loc:
            check += 1
            break

    # clear previous info
    pygame.draw.rect(screen, (255, 255, 255, 255), (0, height + 1, width, height + info_height))

    # build text about info
    textCount = font.render("count: " + repr(i), 1, (0, 0, 0))
    textCheck = font.render("check: " + repr(check), 1, (0, 0, 0))
    screen.blit(textCount, (10, height + 1))
    screen.blit(textCheck, (width / 3, height + 1))

    try:
        # put ratio try about checked
        pi = repr ( round ( 2 * 300 / 600 * float(count) / float(check) , 6 ) )
        textPercent = font.render ( "Pi : " + pi [ 0 : 6 ] , 1 , ( 0 , 0 , 0 ) )
        screen.blit(textPercent, (2 * width / 3, height + 1))

    except ZeroDivisionError as message:
        print(message)

    pygame.display.flip()
