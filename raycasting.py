import math
import pygame as pg
from data import *
import render as rd

# color blend thee triangles created
# make it an object light point

class RayCasting():
    def check(s, screen, p1, p2):
        p2 -= rd.render.scroll
        isOvelap = False
        for obj in groups["light collide"].sprites():
            rect = obj.rect.copy()
            rect.x -= rd.render.scroll.x
            rect.y -= rd.render.scroll.y
            if rect.clipline(p1, p2):
                isOvelap = True
        
        if not isOvelap:
            pg.draw.line(screen, (255, 255, 255), p1, p2)
    
    
    def render(s, screen, width):
        point = vec(pg.mouse.get_pos())
        for obj in groups["light collide"].sprites():
            s.check(screen, point, vec(obj.rect.left, obj.rect.top - 1))
            s.check(screen, point, vec(obj.rect.right, obj.rect.top))
            s.check(screen, point, vec(obj.rect.right, obj.rect.bottom))
            s.check(screen, point, vec(obj.rect.left, obj.rect.bottom))