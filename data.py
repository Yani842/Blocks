import pygame as pg

vec = pg.math.Vector2

animations = {}

groups = {
    "all": pg.sprite.Group(),
    "update": pg.sprite.Group(),
    "player": pg.sprite.Group(),
    "friction": pg.sprite.Group(),
    "player collide": pg.sprite.Group(),
    "ground": pg.sprite.Group()
}
currentPlayer = None

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