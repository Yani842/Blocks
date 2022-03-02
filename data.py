import pygame as pg

vec = pg.math.Vector2
g = pg.sprite.Group

animations = {}
groups = {
    "all": g(),
    "update": g(),
    "player": g(),
    "friction": g(),
    "player collide": g(),
    "jelly collide": g(),
    "ground": g(),
    "jellys": g()
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