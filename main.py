import pygame as pg
from data import *
import data as da
import render as rd
import loads as ld

class Main:
    def init(s):
        pg.init()
        s.width = 1024
        s.height = 768
        s.screen = pg.display.set_mode((s.width, s.height), pg.HWSURFACE | pg.DOUBLEBUF)
        s.Clock = pg.time.Clock()
        s.running = True
        s.dt = 0;
        rd.render.init(s.width, s.height)
        ld.loadObjectsFromJson("levels/level1.json")
        rd.render.setFocusedObject(da.currentPlayer)

    def inputs(s):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                s.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    s.running == False

        pl = da.currentPlayer
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            pl.mv.addAcc(vec(-1,0)) #left
        if keys[pg.K_d]:
            pl.mv.addAcc(vec(1,0)) #right
        if keys[pg.K_w]:
            pl.mv.addAcc(vec(0,-1)) #up
        if keys[pg.K_s]:
            pl.mv.addAcc(vec(0,1)) #down
        if keys[pg.K_SPACE]:
            pl.mv.jump()

    def update(s):
        for obj in groups["update"]:
            obj.update(s.dt)
        rd.render.update(s.dt)

    def run(s):
        while s.running:
            s.inputs()
            s.update()
            
            s.screen.fill((0, 0, 0))
            rd.render.render(s.screen)
            pg.display.flip()
            
            s.dt = s.Clock.tick(60) / 1000
            pg.display.set_caption(f"{s.Clock.get_fps():.2f}")

if __name__ == '__main__':
    main = Main()
    main.init()
    main.run()
    pg.quit()