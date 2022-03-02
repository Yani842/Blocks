import pygame as pg
from data import *
import data as da
import physics as ph
import render as rd

class Player(pg.sprite.DirtySprite):
    def __init__(self, id: int, pos: vec):
        pg.sprite.DirtySprite.__init__(self, [groups["player"], groups["all"], groups["update"], groups["jelly collide"]])
        self.id: int = id
        self.pos: vec = pos
        self.mv: ph.Movement = ph.Movement(self, 50, groups["player collide"], groups["friction"], {groups["ground"]: 4}, 5/2, True, animations["ghost idle"])

    def update(self, dt: float):
        self.mv.update(dt)


class NoLogic(pg.sprite.DirtySprite):
    def __init__(self, id: int, pos: vec, groups: list[pg.sprite.Group]):
        pg.sprite.DirtySprite.__init__(self, groups)
        self.id: int = id
        self.pos: vec = pos


class Jelly(pg.sprite.DirtySprite):
    def __init__(self, id: int, pos: vec):
        pg.sprite.DirtySprite.__init__(self, [groups["jellys"], groups["all"], groups["update"], groups["player collide"]])
        self.id: int = id
        self.pos: vec = pos
        self.mv: ph.Movement = ph.Movement(self, 20, groups["jelly collide"], groups["friction"], {groups["ground"]: 5, groups["player"]: 6}, 4, False, animations["jelly idle"])

    def ai(s):
        pl = da.currentPlayer
        if not s.rect.bottom == pl.rect.top:
            if s.pos.x > pl.pos.x: # left
                s.mv.addAcc(vec(-1,0))
                rd.render.setAnimationSameFrame(s.id, animations["jelly left"])
            if s.pos.x < pl.pos.x: # right
                s.mv.addAcc(vec(1,0))
                rd.render.setAnimationSameFrame(s.id, animations["jelly right"])
        else:
            s.mv.lock()
        if s.mv.getCollision().x:
            s.mv.jump()
        
    def update(s, dt: float):
        s.ai()
        s.mv.update(dt)