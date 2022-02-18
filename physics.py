import pygame as pg
import vars as vr


class movement():
    def __init__(s, obj):
        s.acc = vr.Vec(0, 0)
        s.vel = vr.Vec(0, 0)
        s.SPEED = 55
        s.obj = obj

    def getFric(s):
        s.obj.rect = s.obj.rect.inflate(2, 2)
        hits = pg.sprite.spritecollide(s.obj, vr.groups["friction"], False)
        s.obj.rect = s.obj.rect.inflate(-2, -2)

        friction = 0
        for h in hits:
            if vr.groups["frozen walls"] in h.groups:
                friction -= 0.003
            if vr.groups["sandy walls"] in h.groups:
                friction -= 0.12
        if not friction:
            friction -= 5
        return friction

    def setSpeed(s, speed):
        s.SPEED = speed

    def addAcc(s, vec):
        s.acc += s.SPEED * vec

    def collideX(s):
        if hits := pg.sprite.spritecollide(s.obj, vr.groups["player collide"], False):
            if s.vel.x > 0:  # left
                s.obj.pos.x = hits[0].rect.left - s.obj.rect.width
                s.vel.x = 0
            if s.vel.x < 0:
                s.obj.pos.x = hits[0].rect.right
                s.vel.x = 0
            s.obj.rect.x = s.obj.pos.x

    def collideY(s):
        if hits := pg.sprite.spritecollide(s.obj, vr.groups["player collide"], False):
            if s.vel.y > 0:
                s.obj.pos.y = hits[0].rect.top - s.obj.rect.height
                s.vel.y = 0
            if s.vel.y < 0:
                s.obj.pos.y = hits[0].rect.bottom
                s.vel.y = 0
            s.obj.rect.y = s.obj.pos.y

    def update(s, dt):
        s.acc.x += s.vel.x * s.getFric() * dt
        s.acc.y += s.vel.y * s.getFric() * dt
        s.vel += s.acc
        print(dt)
        s.obj.pos[0] += (s.vel.x + 0.5 * s.acc.x)*dt
        s.obj.pos.y += (s.vel.y + 0.5 * s.acc.y)*dt

        s.obj.rect.x = s.obj.pos.x
        s.collideX()
        s.obj.rect.y = s.obj.pos.y
        s.collideY()

        s.acc = vr.Vec(0, 0)


if __name__ == "__main__":
    import main as m
    m.init()
    m.gameMainLoop()
    pg.quit()
