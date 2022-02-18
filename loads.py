import pygame as pg
import os.path as op
import json
import vars as vr
import objects as ob

def importImages(imagePath, sizeX = 32, sizeY = 32):
    images = []
    for path in imagePath:
        image = pg.image.load(op.join("data/images/", path)).convert_alpha()
        images.append(pg.transform.scale(image, (sizeX, sizeY)))
    return images

def loadObjectsFromJson(path):
    level = json.load(open(op.join("data/json/", path)))
    for obj in level:
        if obj[0] == "player":
            vr.objects.append(ob.Player(vr.getId(), vr.Vec(obj[1], obj[2])))
            vr.currentPlayer = vr.objects[-1]
            vr.Render.setAnimation(len(vr.objects)-1, vr.animations["playerIdle"])
            
        elif obj[0] == "wall":
            vr.objects.append(ob.Wall(vr.getId(), (obj[1], obj[2])))
            vr.Render.setAnimation(len(vr.objects)-1, vr.animations["wall"])


if __name__ == "__main__":
    import main as m
    m.init()
    m.gameMainLoop()
    pg.quit()