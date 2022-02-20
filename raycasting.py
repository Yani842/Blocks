import math
import pygame as pg
from data import *
import render as rd

# shadow casting - continue a ray after edge(not from edge to edge)
# color blend the triangles created
# make it an object light point

class RayCasting():
    
    def check(s, p1, p2, screen):
        p2 -= rd.render.scroll
        isOvelap = False
        for obj in groups["light collide"].sprites():
            rect = obj.rect.copy()
            rect.x -= rd.render.scroll.x
            rect.y -= rd.render.scroll.y
            if rect.clipline(p1, p2):
                isOvelap = True
        if not isOvelap:
            return p2
        else:
            return None
    
    def render(s, screen, width):
        point = vec(pg.mouse.get_pos())
        ends = []
        for obj in groups["light collide"].sprites():
            ends.append(s.check(point, vec(obj.rect.left - 1, obj.rect.bottom), screen))
            ends.append(s.check(point, vec(obj.rect.left, obj.rect.top - 1), screen))
            ends.append(s.check(point, vec(obj.rect.right, obj.rect.top), screen))
            ends.append(s.check(point, vec(obj.rect.right, obj.rect.bottom), screen))
        
        ends = ([i for i in ends if i != None])
        def sorting(v):
            return math.atan2(point.x - v.x, point.y - v.y)
        ends.sort(key=sorting)
        
        for i in range(0, len(ends)-1):
            pg.draw.polygon(screen, (255, 255, 255, 100), (point, ends[i], ends[i+1]))
            # pg.draw.line(screen, (0, 0, 255), point, ends[i], 3)
            