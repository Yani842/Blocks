import pygame as pg
import os.path as op
from data import *

def importImages(imagePath: list[str], sizeX: int = 32, sizeY: int = 32):
    images = []
    for path in imagePath:
        image = pg.image.load(op.join("data/images/", path)).convert_alpha()
        images.append(pg.transform.scale(image, (sizeX, sizeY)))
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
        animations["playerIdle"] = Animation(importImages(["ghost/idle-1.png"]), 0, False)
        animations["ground"] = Animation(importImages(["ground/grass-1.png"], 48, 48), 0, False)

    def setFocusedObject(s, obj):
        s.__focuseObjct = obj
    
    def update(s, dt):
        if s.__focuseObjct:
            s.scroll.x += int((s.__focuseObjct.rect.x-s.scroll.x-s.__winW/2+s.__focuseObjct.rect.width/2)/6)
            s.scroll.y += int((s.__focuseObjct.rect.y-s.scroll.y-s.__winH/2+s.__focuseObjct.rect.height/2)/6)
            
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
        groups["all"].sprites()[id].rect = animation[0].get_rect()
        groups["all"].sprites()[id].rect.x, groups["all"].sprites()[id].rect.y = groups["all"].sprites()[id].pos
        s.objectStates[id][2] = animation

render = Render()
