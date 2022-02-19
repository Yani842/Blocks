import pygame as pg
import vars as vr
import render as rd
import loads as ld

class Main:
    def init(s):
        pg.init()
        vr.Screen = pg.display.set_mode((800, 600), pg.HWSURFACE | pg.DOUBLEBUF)
        vr.Render = rd.render()
        s.Clock = pg.time.Clock()
        s.dt = 0;
        ld.loadObjectsFromJson("levels/level1.json")
        
    def inputs(s):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                vr.Run = False

        pl = vr.currentPlayer
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            pl.mv.addAcc(vr.Vec(-1,0)) #left
        if keys[pg.K_d]:
            pl.mv.addAcc(vr.Vec(1,0)) #right
        if keys[pg.K_w]:
            pl.mv.addAcc(vr.Vec(0,-1)) #up
        if keys[pg.K_s]:
            pl.mv.addAcc(vr.Vec(0,1)) #down
        if keys[pg.K_SPACE]:
            pl.mv.jump()

    def update(s):
        for obj in vr.objects:
            obj.update(s.dt)
        vr.Render.update(s.dt)

    def run(s):
        while vr.Run:
            s.inputs()
            s.update()
            vr.Render.render()
            s.dt = s.Clock.tick(60) / 1000
            pg.display.set_caption(f"{s.Clock.get_fps():.2f}")

if __name__ == '__main__':
    main = Main()
    main.init()
    main.run()
    pg.quit()