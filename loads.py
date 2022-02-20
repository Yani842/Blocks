import pygame as pg
import os.path as op
import json
from data import *
import data as da
import objects as ob
import render as rd

def loadObjectsFromJson(path):
    level = json.load(open(op.join("data/json/", path)))
    for obj in level:
        if obj[0] == "player":
            # objects.append(ob.Player(getId(), vec(obj[1], obj[2])))
            pl = ob.Player(getId(), vec(obj[1], obj[2]))
            da.currentPlayer = pl
            rd.render.setAnimation(len(objects)-1, animations["playerIdle"])
            
        elif obj[0] == "ground":
            # objects.append(ob.Ground(getId(), (obj[1], obj[2])))
            ob.Ground(getId(), (obj[1], obj[2]))
            rd.render.setAnimation(len(objects)-1, animations["ground"])
