import pygame as pg
import data as da
import physics as ph


class Player(pg.sprite.DirtySprite):
    def __init__(s, id: int, pos: da.Vec):
        pg.sprite.DirtySprite.__init__(s, [da.groups["player"]])
        s.id = id
        s.pos: da.Vec = pos
        s.mv = ph.Movement(s)

    def update(s, dt):
        s.mv.update(dt)


class Ground(pg.sprite.DirtySprite):
    def __init__(s, id: int, pos: da.Vec):
        pg.sprite.DirtySprite.__init__(
            s, [da.groups["ground"], da.groups["player collide"]])
        s.id = id
        s.pos: da.Vec = pos


if __name__ == "__main__":
    import main as m
    main = m.Main()
    main.init()
    main.run()
    pg.quit()
