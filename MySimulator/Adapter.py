import strat
import random
from math import cos, sin,pi, atan
#adapter: Takes linear velocity and angular velocity and translates to the simulator
#Takes the current position/vel/linvel and translates to the planner


#DAR UPDATE EM VX para controlar velocidade linear
def deg2rad(deg):
	return deg*pi/180.
def rad2deg(rad):
	return rad*180/pi
def pol2lin(vlin, ang):
	vlin = float(vlin)
	ang = float(ang)
	vx, vy = vlin*cos(deg2rad(ang)), vlin*sin(deg2rad(ang))
	return vx, vy
def lin2pol(vx, vy):
	vx = float(vx)
	vy = float(vy)
	vlin, vang = sqrt(vx**2 + vy**2), atan(vy/vx)
	return vlin, vang

class Adapter(object):
	"""docstring for Adapater"""
	def __init__(self, arg):
		self.arg = arg
		self.lastX = 220
		self.lastY = 300
		self.X = 220
		self.Y = 330
		self.VX = 0
		self.VY = 0
		self.Vlin = 20
		self.Vang = 40
		self.ang = 0


	def update(self, delta_time, X, Y, ang):
		print (delta_time)
		self.VX = (X - self.lastX)/delta_time
		self.VY = (Y - self.lastY)/delta_time
		#self.sim2strat()

		self.lastX = X
		self.lastY = Y
		#mandar vlin + ang (nao Vang!!!11!) para vx e vy
		self.VX, self.VY = pol2lin(self.Vlin, self.ang)
		#print (self.VX, self.VY)
		self.X = self.X + self.VX*delta_time
		self.Y = self.Y + self.VY*delta_time
		self.ang += self.Vang*delta_time
		#print (self.ang)
		
	def strat2sim(self):
		return 
	def sim2strat(self):
		print (self.VX)
		#process
		pass

		
		