import pygame as pg
from data import *
import physics as ph
import render as rd

class Player(pg.sprite.DirtySprite):
    def __init__(s, id: int, pos: vec):
        pg.sprite.DirtySprite.__init__(s, [groups["player"], groups["all"], groups["update"]])
        s.id: int = id
        s.pos: vec = pos
        s.mv: ph.Movement = ph.Movement(s)

    def update(s, dt):
        s.mv.update(dt)


class NoLogic(pg.sprite.DirtySprite):
    def __init__(s, id: int, pos: vec, groups: list(pg.sprite.Group())):
        pg.sprite.DirtySprite.__init__(s, groups)
        s.id: int = id
        s.pos: vec = pos


# this class will be exactly like the future dog class, its just that for now i didnt draw the textures for the dog
# so ill do everything the dog do but with the jelly, good luck for me <3
class jelly:
    pass