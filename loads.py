import pygame as pg
import os.path as op
import json
import data as da
import objects as ob
import render as rd

def loadObjectsFromJson(path):
    level = json.load(open(op.join("data/json/", path)))
    for obj in level:
        if obj[0] == "player":
            da.objects.append(ob.Player(da.getId(), da.Vec(obj[1], obj[2])))
            da.currentPlayer = da.objects[-1]
            rd.render.setAnimation(len(da.objects)-1, da.animations["playerIdle"])
            
        elif obj[0] == "ground":
            da.objects.append(ob.Ground(da.getId(), (obj[1], obj[2])))
            rd.render.setAnimation(len(da.objects)-1, da.animations["ground"])


if __name__ == "__main__":
    import main as m
    main = m.Main()
    main.init()
    main.run()
    pg.quit()