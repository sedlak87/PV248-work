from random import randint

import pygame
from pygame import display, draw, time, event


class circle:
    def __init__(self):
        self.color = [255, randint(0, 255), randint(0, 255)]
        self.center = [randint(0, 1280), randint(0, 800)]
        self.radius = 5
        self.maxr = randint(1, 50)


screen = display.set_mode([1250, 800])
c = time.Clock()
d = []
while True:
    screen.fill([0, 0, 0])
    for i in d[:]:
        draw.circle(screen, i.color, i.center, i.radius, 1)
        i.radius += 1
        if i.radius >= i.maxr: d.remove(i)
    d.append(circle())
    display.flip()
    c.tick(100)
    if event.poll().type == pygame.KEYDOWN: break