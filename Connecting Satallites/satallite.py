
import pgzrun
import random
from time import time

HEIGHT = 600
WIDTH = 800

satallites = []
lines = []

nextSatallite = 0
startTime = 0
endTime = 0
totalTime = 0
numSatallite = 8

def makeSatallites():
    global startTime, satallites
    startTime = time
    for i in range(numSatallite):
        satalliteA = Actor("satallite")
        satalliteA.pos = random.randint(50,750),random.randint(50,550)
        satallites.append(satalliteA)

def on_mouse_down(pos):
    global nextSatallite, lines
    if nextSatallite < numSatallite:
        if satallites[nextSatallite].collidepoint(pos):
            if nextSatallite:
                lines.append(satallites[nextSatallite - 1].pos, satallites[nextSatallite].pos)
            nextSatallite += 1
        else:
            lines = []
            nextSatallite = 0

makeSatallites()

def draw():
    global totalTime
    screen.blit("nightsky",(0,0))
    num = 1
    for satallite in satallites:
        satallite.draw()
        screen.draw.text(str(num),(satallite.pos[0],satallite.pos[1]+15))
        num += 1
        

def update():
    pass

pgzrun.go()