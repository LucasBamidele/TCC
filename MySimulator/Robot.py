import arcade.sprite
import Adapter
class RobotPlayer(arcade.sprite.Sprite):
	"""docstring for RobotPlayer"""
	def __init__(self, imgfile, scale, xi, yi, linV, angV, anglei,mass = 300):
		super().__init__(imgfile, scale)
		self.mass = mass
		self.center_x = xi
		self.center_y = yi
		self.lx = xi
		self.ly = yi
		self.linV = 0
		self.angV = 0
		self.isfree = True
		#self.angle = anglei
		self.limitTop = False
		self.limitBottom = False
		self.limitLeft = False
		self.limitRight = False
	def setFree(self, st):
		self.isfree = st
	def isFree(self):
		return self.isfree
	def getPosition(self):
		return (self.center_x, self.center_y)

	def getLinearVelocity(self):
		return self.linV
	
	def getAngularVelocity(self):
		return self.angV
	
	def getAngle(self):
		return self.angle
	
	def getPolarVelocity(self):
		return(self.linV, self.angV, self.angle)
	
	def updateVelocities(self, linV, angV):
		self.linV = linV
		self.angV = angV
	def limitPositioning(self):
		pass
	def updatePosition(self, delta_time):
		VX, VY = Adapter.pol2lin(self.linV, self.angle)
		self.center_x += VX*delta_time
		self.center_y += VY*delta_time
		self.angle += self.angV*delta_time

		