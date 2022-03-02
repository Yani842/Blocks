from typing import Dict
import pygame as pg
from data import *
import render as rd

class Movement():
    def __init__(s, obj, speed:int, collisionGroup: pg.sprite.Group, frictionGroup: pg.sprite.Group, frictionDict: Dict[pg.sprite.Group, float], frictionDefault:float, isIdleAnimation: bool, idleAnimtion: rd.Animation):
        s.__SPEED = speed
        s.__JUMPVEL = 130
        
        s.__acc = vec(0, 0)
        s.__vel = vec(0, 0)
        s.__obj = obj
        s.__onSurface = False
        s.__jumpCounter = 0
        s.__isCollideX = False
        s.__isCollideY = False
        s.__lock = False
        
        s.__collisionG = collisionGroup
        s.__fricG = frictionGroup
        s.__fricDict = frictionDict
        s.__fricDef = frictionDefault
        s.__isIdle = isIdleAnimation
        s.__idleAn = idleAnimtion
        

    def addAcc(s, vec: vec):
        s.__acc += s.__SPEED * vec
    
    def getAcc(s):
        return s.__acc
    
    def getCollision(s): # return also in directions of the collisions(left right top bottom)
        return vec(s.__isCollideX, s.__isCollideY)

    def jump(s):
        if s.__onSurface:
            s.__jumpCounter = 0.2
    
    def lock(s):
        s.__lock = True
            
    def __getFric(s):
        s.__obj.rect = s.__obj.rect.inflate(2, 2)
        hits = pg.sprite.spritecollide(s.__obj, groups["all"], False)
        s.__obj.rect = s.__obj.rect.inflate(-2, -2)

        # this beast just somehow works
        if friction := -sum([v for g, v in s.__fricDict.items() if g in [item for sublist in [j.groups() for j in hits] for item in sublist]]):
            return friction
        else:
            return -s.__fricDef
    
    def __collideX(s):
        if hits := pg.sprite.spritecollide(s.__obj, s.__collisionG, False):
            if s.__vel.x > 0: # left
                s.__obj.pos.x = hits[0].rect.left - s.__obj.rect.width
                s.__vel.x = 0
            if s.__vel.x < 0: # right
                s.__obj.pos.x = hits[0].rect.right
                s.__vel.x = 0
            s.__obj.rect.x = s.__obj.pos.x
            s.__isCollideX = True
        else:
            s.__isCollideX = False

    def __collideY(s):
        s.__onSurface = False
        if hits := pg.sprite.spritecollide(s.__obj, s.__collisionG, False):
            if s.__vel.y > 0: # bottom
                s.__obj.pos.y = hits[0].rect.top - s.__obj.rect.height
                s.__vel.y = 0
                s.__onSurface = True
            if s.__vel.y < 0: # top
                s.__obj.pos.y = hits[0].rect.bottom
                s.__vel.y = 0
            s.__obj.rect.y = s.__obj.pos.y
            s.__isCollideY = True
        else:
            s.__isCollideY = False

    def update(s, dt):
        if s.__jumpCounter > 0:
            s.__jumpCounter -= dt
            s.__vel.y -= s.__JUMPVEL
        
        if s.__isIdle and not int(s.__acc.x):
            rd.render.setAnimationSameFrame(s.__obj.id, s.__idleAn)
        
        if s.__lock:
            s.__acc = vec(0, 55)
            s.__lock = False
        
        s.__acc += s.__vel * s.__getFric() * dt
        # s.__acc.y += s.__vel.y * s.__getFric() * dt
        s.__vel += s.__acc
        s.__obj.pos.x += (s.__vel.x + 0.5 * s.__acc.x) * dt
        s.__obj.pos.y += (s.__vel.y + 0.5 * s.__acc.y) * dt

        s.__obj.rect.x = s.__obj.pos.x
        s.__collideX()
        s.__obj.rect.y = s.__obj.pos.y
        s.__collideY()

        s.__acc = vec(0, 55)