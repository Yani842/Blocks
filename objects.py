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
        

class Ground(pg.sprite.DirtySprite):
    def __init__(s, id:int, pos:vr.Vec):
        pg.sprite.DirtySprite.__init__(s, [vr.groups["ground"], vr.groups["player collide"]])
        s.id = id
        s.pos: vr.Vec = pos


if __name__ == "__main__":
    import main as m
    main = m.Main()
    main.init()
    main.run()
    pg.quit()