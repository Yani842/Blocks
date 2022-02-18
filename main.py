import pygame as pg
import vars as vr
import render as rd
import loads as ld

def init():
    pg.init()
    vr.Screen = pg.display.set_mode((800, 600), pg.HWSURFACE | pg.DOUBLEBUF)
    vr.Render = rd.render()
    vr.Clock = pg.time.Clock()
    ld.loadObjectsFromJson("levels/level1.json")
    
def inputs():
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

def update():
    DT = vr.Clock.get_time()
    for obj in vr.objects:
        obj.update(DT)
    vr.Render.update(DT)

def gameMainLoop():
    while vr.Run:
        inputs()
        update()
        vr.Render.render()
        DT = vr.Clock.tick()
        pg.display.set_caption(f"{vr.Clock.get_fps():.2f}")

if __name__ == '__main__':
    init()
    gameMainLoop()
    pg.quit()