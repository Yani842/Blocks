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
            pl = ob.Player(getId(), vec(obj[1], obj[2]))
            da.currentPlayer = pl
            rd.render.setAnimation(len(objects)-1, animations["ghost idle"])
            
        elif obj[0] == "ground":
            ob.NoLogic(getId(), (obj[1], obj[2]), [groups["ground"], groups["all"], groups["player collide"], groups["friction"]])
            rd.render.setAnimation(len(objects)-1, animations["ground"])