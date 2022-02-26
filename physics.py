import pygame as pg
from data import *
import render as rd

class Movement():
    def __init__(s, obj):
        s.__SPEED = 50
        s.__JUMPVEL = 130
        
        s.__acc = vec(0, 0)
        s.__vel = vec(0, 0)
        s.__obj = obj
        s.__onSurface = False
        s.__jumpCounter = 0

    def addAcc(s, vec: vec):
        s.__acc += s.__SPEED * vec

    def jump(s):
        if s.__onSurface:
            s.__jumpCounter = 0.2
            
    def __getFric(s):
        s.__obj.rect = s.__obj.rect.inflate(2, 2)
        hits = pg.sprite.spritecollide(s.__obj, groups["friction"], False)
        s.__obj.rect = s.__obj.rect.inflate(-2, -2)

        friction = 0
        for h in hits:
            if groups["ground"] in h.groups():
                friction -= 4
        if not friction:
            friction -= 5/2
        return friction
    
    def __collideX(s):
        if hits := pg.sprite.spritecollide(s.__obj, groups["player collide"], False):
            if s.__vel.x > 0: # left
                s.__obj.pos.x = hits[0].rect.left - s.__obj.rect.width
                s.__vel.x = 0
            if s.__vel.x < 0: # right
                s.__obj.pos.x = hits[0].rect.right
                s.__vel.x = 0
            s.__obj.rect.x = s.__obj.pos.x

    def __collideY(s):
        s.__onSurface = False
        if hits := pg.sprite.spritecollide(s.__obj, groups["player collide"], False):
            if s.__vel.y > 0: # bottom
                s.__obj.pos.y = hits[0].rect.top - s.__obj.rect.height
                s.__vel.y = 0
                s.__onSurface = True
            if s.__vel.y < 0: # top
                s.__obj.pos.y = hits[0].rect.bottom
                s.__vel.y = 0
            s.__obj.rect.y = s.__obj.pos.y

    def update(s, dt):
        if s.__jumpCounter > 0:
            s.__jumpCounter -= dt
            s.__vel.y -= s.__JUMPVEL
        
        if not int(s.__acc.x):
            rd.render.setAnimationSameFrame(s.__obj.id, animations["jelly right"])
        
        s.__acc.x += s.__vel.x * s.__getFric() * dt
        s.__acc.y += s.__vel.y * s.__getFric() * dt
        s.__vel += s.__acc
        s.__obj.pos.x += (s.__vel.x + 0.5 * s.__acc.x) * dt
        s.__obj.pos.y += (s.__vel.y + 0.5 * s.__acc.y) * dt

        s.__obj.rect.x = s.__obj.pos.x
        s.__collideX()
        s.__obj.rect.y = s.__obj.pos.y
        s.__collideY()

        s.__acc = vec(0, 55)
