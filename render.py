import pygame as pg
import os.path as op
import data as da

def importImages(imagePath, sizeX = 32, sizeY = 32):
    images = []
    for path in imagePath:
        image = pg.image.load(op.join("data/images/", path)).convert_alpha()
        images.append(pg.transform.scale(image, (sizeX, sizeY)))
    return images

class Animation:
    def __init__(s, images, rate, oneCycle):
        s.images = images
        s.length = len(images)-1
        s.rate = rate
        s.oneCycle = oneCycle
        s.noAnimation = False


class Render:
    def __init__(s):
        # [pointInRate, currentFrame, animation, doOWAEnded, id]
        s.objectStates = []

    def init(s):
        da.animations = {
            "playerIdle": Animation(
                importImages(
                    ["player/"+str(i)+".png" for i in range(1, 16)]),
                0.04,
                False),
            "ground": Animation(
                importImages(
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

    def render(s, screen):
        screen.fill((0, 0, 0))
        for obj in s.objectStates:
            if obj[1] >= 0:
                # pos[0]-da.Scroll[0], pos[1]-da.Scroll[1]
                screen.blit(obj[2].images[obj[1]], da.objects[obj[4]].rect)
        pg.display.flip()

    def setAnimation(s, id, animation):
        if len(s.objectStates) <= id:
            da.objects[id].rect = animation.images[0].get_rect()
            da.objects[id].rect.x, da.objects[id].rect.y = da.objects[id].pos
            s.objectStates.append([0, 0, animation, False, id])
        else:
            da.objects[id].rect = animation.images[0].get_rect()
            da.objects[id].rect.x, da.objects[id].rect.y = da.objects[id].pos
            s.objectStates[id] = [0, 0, animation, False, id]

    def setAnimationSameFrame(s, id, animation):
        da.objects[id].rect = animation[0].get_rect()
        da.objects[id].rect.x, da.objects[id].rect.y = da.objects[id].pos
        s.objectStates[id][2] = animation

render = Render()

if __name__ == "__main__":
    import main as m
    main = m.Main()
    main.init()
    main.run()
    pg.quit()