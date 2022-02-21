import pygame as pg

vec = pg.math.Vector2

animations = {}

groups = {
    "all": pg.sprite.Group(),
    "update": pg.sprite.Group(),
    "player": pg.sprite.Group(),
    "friction": pg.sprite.Group(),
    "player collide": pg.sprite.Group(),
    "light collide": pg.sprite.Group(),
    "ground": pg.sprite.Group()
}
currentPlayer = None
vertices = [(300-1, 300), (300-1, 348),
            (632, 300), (632, 348),
            (444, 348), (492, 348),
            (444, 492), (492, 492)]

objects = []
freeIds = []

def getId():
    if not freeIds:
        objects.append(1)
        return len(objects) - 1
    else:
        return freeIds[-1]

def deleteObject(id):
    objects[id] = None
    freeIds.append(id)