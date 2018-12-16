"""
Strategy should be developed here
"""
from random import randint
import Robot
SCREEN_WIDTH = 600
class Strategy(object):
	"""docstring for Strategy"""
	def __init__(self, SCALE):
		self.SCALE = 3
		SPRITE_SCALE_ROBOT = 1.5
		self.robot1 = Robot.RobotPlayer("imgs/robo1.png", SPRITE_SCALE_ROBOT, SCREEN_WIDTH/2 - 80, SCREEN_WIDTH/2 + 100,
		10, 10, 0)
		self.robot2 = Robot.RobotPlayer("imgs/robo2.png", SPRITE_SCALE_ROBOT, SCREEN_WIDTH/2 - 80, SCREEN_WIDTH/2,
		10, 10, 0)
		self.robot3 = Robot.RobotPlayer("imgs/robo3.png", SPRITE_SCALE_ROBOT, SCREEN_WIDTH/2 - 80, SCREEN_WIDTH/2 - 100,
		10, 10, 0)
		self.stop = 1
	"""
	Update function
	Must be used send velocities to the robot.
	Feedback (position from robots or other 
	"""
	def update(self, delta_time, robot4 = None, robot5 = None, robot6 = None):
		#calculos loucos aqui
		linv1, linv2, linv3 = randint(-10, 10)*self.SCALE, self.stop*10*self.SCALE, randint(0,0)*self.SCALE
		angv1, angv2, angv3 = 0, 0, 0
		#velocidades = [(linv1, angv1), (linv2, angv2),(linv3, angv3)]
		if(self.robot1.isFree()):
			self.robot1.updateVelocities(linv1, angv1)
			self.robot1.updatePosition(delta_time)
		else :
			pass
		if(self.robot2.isFree()):
			self.robot2.updateVelocities(linv2, angv2)
			self.robot2.updatePosition(delta_time)
		else :
			self.stop = 0
			self.robot2.updateVelocities(0,0)
		if(self.robot3.isFree()):
			self.robot3.updateVelocities(linv3, angv3)
			self.robot3.updatePosition(delta_time)
		else :
			pass

		
		


