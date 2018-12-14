import GUI
import arcade
import Adapter
import strat
import Robot
def main():
	SCREEN_WIDTH = 600
	SCREEN_HEIGHT = 600
	SCALE = 3
	strategy = strat.Strategy(SCALE)
	myAdapter = Adapter.Adapter(strategy)
	simulation = GUI.MySimulation(SCREEN_WIDTH, SCREEN_HEIGHT, myAdapter)
	simulation.setup()
	arcade.run()
if __name__ == '__main__':
	main()