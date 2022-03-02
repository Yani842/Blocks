import pygame as pg
import os.path as op
import json
from data import *
import data as da
import objects as ob
import render as rd
import random as ra

def loadObjectsFromJson(path):
    level = json.load(open(op.join("data/json/", path)))
    for obj in level:
        if obj[0] == "player":
            if obj[1][0]:
                pl = ob.Player(getId(), vec(obj[1][1]*48, obj[1][2]*48))
            else:
                pl = ob.Player(getId(), vec(obj[1][1], obj[1][2]))
            da.currentPlayer = pl
            rd.render.setAnimation(len(objects)-1, animations["ghost idle"])
        
        elif obj[0] == "jelly":
            if obj[1][0]:
                ob.Jelly(getId(), vec(obj[1][1]*48, obj[1][2]*48))
            else:
                ob.Jelly(getId(), vec(obj[1][1], obj[1][2]))
            rd.render.setAnimation(len(objects)-1, animations["jelly idle"])

        elif obj[0] == "ground":
            if obj[2][0]:
                ob.NoLogic(getId(), vec(obj[2][1]*48, obj[2][2]*48), [groups["ground"], groups["all"], groups["player collide"], groups["friction"], groups["jelly collide"]])
            else:
                ob.NoLogic(getId(), vec(obj[2][1], obj[2][2]), [groups["ground"], groups["all"], groups["player collide"], groups["friction"], groups["jelly collide"]])
            if obj[1] == "r":
                rd.render.setAnimation(len(objects)-1, animations["ground-"+str(ra.randint(1, 6))])
            elif obj[1] == 1:
                rd.render.setAnimation(len(objects)-1, animations["ground-1"])