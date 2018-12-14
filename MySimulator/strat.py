"""
Strategy should be developed here
"""
from random import randint
import Robot
SCREEN_WIDTH = 600
class Strategy(object):
	"""docstring for Strategy"""
	def __init__(self, SCALE):
		self.SCALE = 0
		SPRITE_SCALE_ROBOT = 1.5
		self.robot1 = Robot.RobotPlayer("imgs/robo1.png", SPRITE_SCALE_ROBOT, SCREEN_WIDTH/2 - 80, SCREEN_WIDTH/2 + 100,
		10, 10, 0)
		self.robot2 = Robot.RobotPlayer("imgs/robo2.png", SPRITE_SCALE_ROBOT, SCREEN_WIDTH/2 - 80, SCREEN_WIDTH/2,
		10, 10, 0)
		self.robot3 = Robot.RobotPlayer("imgs/robo3.png", SPRITE_SCALE_ROBOT, SCREEN_WIDTH/2 - 80, SCREEN_WIDTH/2 - 100,
		10, 10, 0)
	"""
	Update function
	Must be used send velocities to the robot.
	Feedback (position from robots or other """
	def update(self, delta_time, robot4 = None, robot5 = None, robot6 = None):
		#calculos loucos aqui
		linv1, linv2, linv3 = randint(-10, 10)*self.SCALE, randint(-10, 10)*self.SCALE, randint(10,10)*self.SCALE
		angv1, angv2, angv3 = 360, randint(-45, 45), randint(-45, 45)
		#velocidades = [(linv1, angv1), (linv2, angv2),(linv3, angv3)]
		self.robot1.updateVelocities(linv1, angv1)
		self.robot2.updateVelocities(linv2, angv2)
		self.robot3.updateVelocities(linv3, angv3)

		self.robot1.updatePosition(delta_time)
		self.robot2.updatePosition(delta_time)
		self.robot3.updatePosition(delta_time)

