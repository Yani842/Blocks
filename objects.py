import pygame as pg
import vars as vr
import physics as ph

class Player(pg.sprite.DirtySprite):
    def __init__(s, id:int, pos:vr.Vec):
        pg.sprite.DirtySprite.__init__(s, [vr.groups["player"]])
        s.id = id
        s.pos: vr.Vec = pos
        s.mv = ph.movement(s)
        
    def update(s, dt):
        s.mv.update(dt)

class Wall(pg.sprite.DirtySprite):
    def __init__(s, id:int, pos:vr.Vec):
        pg.sprite.DirtySprite.__init__(s, [vr.groups["walls"], vr.groups["player collide"]])
        s.id = id
        s.pos: vr.Vec = pos


if __name__ == "__main__":
    import main as m
    m.init()
    m.gameMainLoop()
    pg.quit()