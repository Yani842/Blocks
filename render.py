import pygame as pg
import os.path as op
import vars as vr
import loads as ld


class animation:
    def __init__(s, images, rate, oneCycle):
        s.images = images
        s.length = len(images)-1
        s.rate = rate
        s.oneCycle = oneCycle
        s.noAnimation = False


class render:
    def __init__(s):
        # [pointInRate, currentFrame, animation, doOWAEnded, id]
        s.objectStates = []
        vr.animations = {
            "playerIdle": animation(
                ld.importImages(
                    ["player/"+str(i)+".png" for i in range(1, 16)]),
                0.04,
                False),
            "ground": animation(
                ld.importImages(
                    ["ground/grass-1.png"], 48, 38),
                0,
                False)
        }

    def update(s, dt):
        for obj in s.objectStates:
            if obj[2].noAnimation:
                continue
            obj[0] += dt
            if obj[0] > obj[2].rate:
                obj[0] = 0
                obj[1] += 1
                if obj[1] > obj[2].length:
                    if obj[2].oneCycle:
                        obj[1] = -1
                    else:
                        obj[1] = 0

    def render(s):
        vr.Screen.fill((0, 0, 0))
        for obj in s.objectStates:
            if obj[1] >= 0:
                # pos[0]-vr.Scroll[0], pos[1]-vr.Scroll[1]
                vr.Screen.blit(obj[2].images[obj[1]], vr.objects[obj[4]].rect)
        pg.display.flip()

    def setAnimation(s, id, animation):
        if len(s.objectStates) <= id:
            vr.objects[id].rect = animation.images[0].get_rect()
            vr.objects[id].rect.x, vr.objects[id].rect.y = vr.objects[id].pos
            s.objectStates.append([0, 0, animation, False, id])
        else:
            vr.objects[id].rect = animation.images[0].get_rect()
            vr.objects[id].rect.x, vr.objects[id].rect.y = vr.objects[id].pos
            s.objectStates[id] = [0, 0, animation, False, id]

    def setAnimationSameFrame(s, id, animation):
        vr.objects[id].rect = animation[0].get_rect()
        vr.objects[id].rect.x, vr.objects[id].rect.y = vr.objects[id].pos
        s.objectStates[id][2] = animation


if __name__ == "__main__":
    import main as m
    main = m.Main()
    main.init()
    main.run()
    pg.quit()