import arcade.sprite
import Adapter
from math import exp

MASS = 46
cte = 0.2
k = 0.005
minSpeed = 0.01
class GameBall(arcade.sprite.Sprite):
	"""docstring for GameBall"""
	def __init__(self, imgfile, scale, xi, yi):
		super().__init__(imgfile, scale)
		self.mass = MASS
		self.center_x = xi
		self.center_y = yi
		self.linv = 0
		self.angle = 0
		self.collisionTime = 10000
	def collide(self, angle, vlin, mass):
		self.linv = cte*vlin*mass/self.mass
		self.collisionTime = 0
	def update(self, delta_time):
		print (self.linv)
		if(self.collisionTime < 9999):
			self.collisionTime += delta_time
		self.dissipate()
		VX, VY = Adapter.pol2lin(self.linv, self.angle)
		self.center_x += VX*delta_time
		self.center_y += VY*delta_time

	def dissipate(self):
		self.linv = self.linv*exp(-k*self.collisionTime)
		if(self.linv < minSpeed):
			self.linv = 0
			self.collisionTime = 10000

# VX e^-kt