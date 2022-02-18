import pygame as pg

Scroll = [0, 0]
Screen = None
Run = True
Render = None
Vec = pg.math.Vector2

animations = {}

groups = {
    "player": pg.sprite.Group(),
    "friction": pg.sprite.Group(),
    "player collide": pg.sprite.Group(),
    "walls": pg.sprite.Group(),
    "frozen walls": pg.sprite.Group()
}
currentPlayer = None

objects = []
freeIds = []

def getId():
    if not freeIds:
        return len(objects)
    else:
        return freeIds[-1]

def deleteObject(id):
    objects[id] = None
    freeIds.append(id)


if __name__ == "__main__":
    import main as m
    m.init()
    m.gameMainLoop()
    pg.quit()