"""
This is a (much) simple GUI for simulating a 2D soccer stuff
Python 3.6 is needed to the arcade library work
"""
import arcade
import random
import time
import Adapter
#Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCALE = 3
BASE_WIDTH = 150*SCALE
BASE_HEIGHT = 130*SCALE
GOAL_WIDTH = 10*SCALE
GOAL_HEIGHT = 40*SCALE
PENALTY_WIDTH = 15*SCALE
PENALTY_HEIGHT = 70*SCALE
SPRITE_SCALE_ROBOT = 0.5*SCALE
SPRITE_SCALE_BALL = 0.2*SCALE
#Drawing
class MySimulation(arcade.Window):
	def __init__(self, width, height, adapter):
		super().__init__(width, height)
		self.sentido = 1
		self.bola = None
		self.robot1 = None
		self.robot2 = None
		self.robot3 = None
		self.adapter = adapter
	def setup(self):

		self.robot_list = arcade.SpriteList()
		self.robot1 = arcade.Sprite("imgs/robo1.png", SPRITE_SCALE_ROBOT)
		self.robot2 = arcade.Sprite("imgs/robo2.png", SPRITE_SCALE_ROBOT)
		self.robot3 = arcade.Sprite("imgs/robo3.png", SPRITE_SCALE_ROBOT)

		self.bola = arcade.Sprite("imgs/bola.png", SPRITE_SCALE_BALL)
		self.bola.alpha = 255
		self.bola.center_x = SCREEN_WIDTH/2
		self.bola.center_y = SCREEN_HEIGHT/2


		self.robot1.center_x = SCREEN_WIDTH/2 - 80
		self.robot1.center_y = SCREEN_WIDTH/2 + 100

		self.robot2.center_x = SCREEN_WIDTH/2 - 80
		self.robot2.center_y = SCREEN_WIDTH/2

		self.robot3.center_x = SCREEN_WIDTH/2 - 80
		self.robot3.center_y = SCREEN_WIDTH/2 - 100

		self.robot_list.append(self.robot1)
		self.robot_list.append(self.robot2)
		self.robot_list.append(self.robot3)

	def drawField(self):

		arcade.draw_rectangle_outline(SCREEN_WIDTH/2,
		                              SCREEN_HEIGHT/2,
		                              BASE_WIDTH,
		                              BASE_HEIGHT,
		                              arcade.color.WHITE, 5)
		arcade.draw_rectangle_outline(SCREEN_WIDTH/2 - BASE_WIDTH/2 - GOAL_WIDTH/2,
		                              SCREEN_HEIGHT/2,
		                              GOAL_WIDTH,
		                              GOAL_HEIGHT,
		                              arcade.color.WHITE, 5)
		arcade.draw_rectangle_outline(SCREEN_WIDTH/2 + BASE_WIDTH/2 + GOAL_WIDTH/2,
		                              SCREEN_HEIGHT/2,
		                              GOAL_WIDTH,
		                              GOAL_HEIGHT,
		                              arcade.color.WHITE, 5)
		arcade.draw_circle_outline(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 20*SCALE, arcade.color.WHITE, 5)

		arcade.draw_line(SCREEN_WIDTH/2, 
			SCREEN_HEIGHT/2 - BASE_HEIGHT/2, SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + BASE_HEIGHT/2, arcade.color.WHITE,5)

		arcade.draw_rectangle_outline(SCREEN_WIDTH/2 - BASE_WIDTH/2 + PENALTY_WIDTH/2,
		                              SCREEN_HEIGHT/2,
		                              PENALTY_WIDTH,
		                              PENALTY_HEIGHT,
		                              arcade.color.WHITE, 5)
		arcade.draw_rectangle_outline(SCREEN_WIDTH/2 + BASE_WIDTH/2 - PENALTY_WIDTH/2,
		                              SCREEN_HEIGHT/2,
		                              PENALTY_WIDTH,
		                              PENALTY_HEIGHT,
		                              arcade.color.WHITE, 5)

		arcade.draw_arc_outline(SCREEN_WIDTH/2 - BASE_WIDTH/2 + PENALTY_WIDTH,
								SCREEN_HEIGHT/2,
								5*SCALE,
								10*SCALE,
								arcade.color.WHITE,
								270,
								450,
								5)


		arcade.draw_arc_outline(SCREEN_WIDTH/2 + BASE_WIDTH/2 - PENALTY_WIDTH,
								SCREEN_HEIGHT/2,
								5*SCALE,
								10*SCALE,
								arcade.color.WHITE,
								90,
								270,
								5)

	def on_draw(self):
		arcade.start_render()
		self.drawField()
		self.robot_list.draw()
		self.bola.draw()

	def on_update(self, delta_time):
		curr_x = (self.robot2.get_points()[0][0] + self.robot2.get_points()[1][0])/2
		curr_y = (self.robot2.get_points()[0][1] + self.robot2.get_points()[2][1])/2
		self.adapter.update(delta_time, curr_x, curr_y, self.robot1.angle)
		self.robot2.angle = self.adapter.ang

		#self.robot1.angle += 45
		#exit()
		#hit = arcade.check_for_collision(self.robot2, self.bola)

		self.robot2.set_position(self.adapter.X, self.adapter.Y)
		#self.robot1.set_position(self.robot1.get_)
		
def main():



	simulation = MySimulation(SCREEN_WIDTH, SCREEN_HEIGHT)
	simulation.setup()
	

	#arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "test")
	#arcade.start_render()


	#drawField()
	#createSprites()


	#arcade.finish_render()
	arcade.run()

if __name__ == '__main__':
	main()
