import pygame as pg
import os.path as op
from data import *

def importImages(imagePath: list[str], width: int = 48, height: int = 48, colorkey: bool = False):
    images = []
    for path in imagePath:
        image = pg.image.load(op.join("data/images/", path)).convert_alpha()
        if colorkey:
            image.set_colorkey((255, 255, 255))
        images.append(pg.transform.scale(image, (width, height)))
    return images

class Animation:
    def __init__(s, images: list[pg.Surface], rate: float, oneCycle: bool):
        s.images: list(pg.Surface) = images
        s.length: int = len(images)-1
        s.rate: float = rate
        s.oneCycle: bool = oneCycle
        if rate == 0:
            s.noAnimation: bool = True
        else:
            s.noAnimation: bool = False


class Render:
    def __init__(s):
        # [pointInRate, currentFrame, animation, doOWAEnded, id]
        s.objectStates = []
        s.scroll: vec = vec(0, 0)
        s.__focuseObjct = None
        s.__winW = 0
        s.__winH = 0

    def init(s, w, h):
        s.__winW = w
        s.__winH = h
        # ["player/"+str(i)+".png" for i in range(1, 16)]
        animations["ghost idle"] = Animation(importImages(["ghost/idle-1.png"], 40, 54), 0, False)
        animations["ghost left"] = Animation(importImages(["ghost/left-1.png"], 40, 54), 0, False)
        animations["ghost right"] = Animation(importImages(["ghost/right-1.png"], 40, 54), 0, False)
        animations["jelly left"] = Animation(importImages(["jelly/left/"+str(i)+".png" for i in range(1, 16)], 40, 54, True), 0.02, False)
        animations["jelly right"] = Animation(importImages(["jelly/right/"+str(i)+".png" for i in range(1, 16)], 40, 54, True), 0.02, False)
        animations["ground-1"] = Animation(importImages(["ground/grass-1.png"]), 0, False)
        animations["ground-2"] = Animation(importImages(["ground/grass-2.png"]), 0, False)
        animations["ground-3"] = Animation(importImages(["ground/grass-3.png"]), 0, False)
        animations["ground-4"] = Animation(importImages(["ground/grass-4.png"]), 0, False)
        animations["ground-5"] = Animation(importImages(["ground/grass-5.png"]), 0, False)
        animations["ground-6"] = Animation(importImages(["ground/grass+water.png"]), 0, False)
        print(pg._sdl2.touch.get_device())

    def setFocusedObject(s, obj):
        s.__focuseObjct = obj
    
    def update(s, dt):
        if s.__focuseObjct:
            s.scroll.x += (s.__focuseObjct.rect.x-s.scroll.x-s.__winW/2+s.__focuseObjct.rect.width/2)/9
            s.scroll.y += (s.__focuseObjct.rect.y-s.scroll.y-s.__winH/2+s.__focuseObjct.rect.height/2)/9
            
        for obj in s.objectStates:
            if obj[2].noAnimation:
                continue
            obj[0] += dt
            if obj[0] > obj[2].rate:
                obj[0] = 0
                obj[1] += 1
                if obj[1] > obj[2].length:
                    if obj[2].oneCycle:
                        obj[1] = -1
                    else:
                        obj[1] = 0

    def render(s, screen):
        for obj in s.objectStates:
            if obj[1] >= 0:
                screen.blit(obj[2].images[obj[1]], (groups["all"].sprites()[obj[4]].rect.x-s.scroll.x, groups["all"].sprites()[obj[4]].rect.y-s.scroll.y))

    def setAnimation(s, id, animation):
        if len(s.objectStates) <= id:
            groups["all"].sprites()[id].rect = animation.images[0].get_rect()
            groups["all"].sprites()[id].rect.x, groups["all"].sprites()[id].rect.y = groups["all"].sprites()[id].pos
            s.objectStates.append([0, 0, animation, False, id])
        else:
            groups["all"].sprites()[id].rect = animation.images[0].get_rect()
            groups["all"].sprites()[id].rect.x, groups["all"].sprites()[id].rect.y = groups["all"].sprites()[id].pos
            s.objectStates[id] = [0, 0, animation, False, id]

    def setAnimationSameFrame(s, id, animation):
        groups["all"].sprites()[id].rect = animation.images[0].get_rect()
        groups["all"].sprites()[id].rect.x, groups["all"].sprites()[id].rect.y = groups["all"].sprites()[id].pos
        s.objectStates[id][2] = animation

render = Render()
