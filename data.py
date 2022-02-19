import pygame as pg

Vec = pg.math.Vector2
animations = {}
groups = {
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
        return len(objects)
    else:
        return freeIds[-1]

def deleteObject(id):
    objects[id] = None
    freeIds.append(id)


if __name__ == "__main__":
    import main as m
    main = m.Main()
    main.init()
    main.run()
    pg.quit()