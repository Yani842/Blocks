import pygame as pg
from data import *
import physics as ph


class Player(pg.sprite.DirtySprite):
    def __init__(s, id: int, pos: vec):
        pg.sprite.DirtySprite.__init__(s, [groups["player"], groups["all"], groups["update"]])
        s.id = id
        s.pos: vec = pos
        s.mv = ph.Movement(s)

    def update(s, dt):
        s.mv.update(dt)


class Ground(pg.sprite.DirtySprite):
    def __init__(s, id: int, pos: vec):
        pg.sprite.DirtySprite.__init__(
            s, [groups["ground"], groups["player collide"], groups["light collide"], groups["all"]])
        s.id = id
        s.pos: vec = pos
