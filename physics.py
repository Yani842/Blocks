import pygame as pg
import vars as vr

class movement():
	def __init__(s, obj):
		s.acc = vr.Vec(0,0)
		s.vel = vr.Vec(0,0)
		s.SPEED = 0.007
		s.obj = obj

	def getFric(s):
		s.obj.rect = s.obj.rect.inflate(2, 2)
		hits = pg.sprite.spritecollide(s.obj, vr.groups["friction"], False)
		s.obj.rect = s.obj.rect.inflate(-2, -2)

		friction = 0;
		for h in hits:
			if vr.groups["frozen walls"] in h.groups:
				friction -= 0.03
			if vr.groups["sandy walls"] in h.groups:
				friction -= 0.12
		if not friction:
			friction -= 0.01
		return friction

	def setSpeed(s, speed):
		s.SPEED = speed

	def addAcc(s, vec):
		s.acc += s.SPEED * vec

	def collideX(s):
		if hits := pg.sprite.spritecollide(s.obj, vr.groups["player collide"], False):
			print("collide x")
			if s.vel.x > 0:
				s.obj.pos.x = hits[0].rect.left - self.rect.width
				s.vel.x = 0
			if s.vel.x < 0:
				s.obj.pos.x = hits[0].rect.right
				s.vel.x = 0
			s.obj.rect.x = s.obj.pos.x

	def collideY(s):
		if hits := pg.sprite.spritecollide(s.obj, vr.groups["player collide"], False):
			print("collide y")
			if s.vel.y > 0:
				s.obj.pos.y = hits[0].rect.top - self.rect.height
				s.vel.y = 0
			if s.vel.y < 0:
				s.obj.pos.y = hits[0].rect.bottom
				s.vel.y = 0
			s.obj.rect.y = s.obj.pos.y

	def update(s):
		s.acc.x += s.vel.x * s.getFric()
		s.acc.y += s.vel.y * s.getFric()
		s.vel += s.acc
		s.obj.pos += s.vel + s.acc/2
		s.acc = vr.Vec(0,0)

		s.obj.rect.x = s.obj.pos.x
		s.collideX()
		s.obj.rect.y = s.obj.pos.y
		s.collideY()


if __name__ == "__main__":
	import main as m
	m.init()
	m.gameMainLoop()
	pg.quit()