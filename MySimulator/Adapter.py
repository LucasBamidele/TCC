import strat
import random
from math import cos, sin,pi, atan
import Robot
import strat
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
	def __init__(self, Strategy):
		self.strat1 = Strategy

	def update(self, delta_time, X =0, Y=0, ang=0):
		self.strat1.update(delta_time)
		
	def strat2sim(self):
		return 
	def sim2strat(self):
		print (self.VX)
		#process
		pass

		
		