import GUI
import arcade
import Adapter

def main():
	SCREEN_WIDTH = 600
	SCREEN_HEIGHT = 600
	myAdapter = Adapter.Adapter(0)
	simulation = GUI.MySimulation(SCREEN_WIDTH, SCREEN_HEIGHT, myAdapter)
	simulation.setup()
	arcade.run()
if __name__ == '__main__':
	main()