import pygame as pg
from data import *
import physics as ph


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
