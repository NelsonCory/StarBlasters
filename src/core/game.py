from . event_manager import *
import pygame
from . ship_controller import *

class Game():

	# Initialize pygame here
	def __init__(self):
		pygame.init()

		self.__event_manager = EventManager()
		self.__done = False
		self.__clock = pygame.time.Clock()
		self.__control = ShipController()

	# Main loop, returns exit code
	def run(self):
		# Main loop
		while not self.__done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.__done = True
				elif event.type == pygame.KEYDOWN:
					self.__control.receive_event(event)
					# for controller in self.__screen.get_scene().get_controllers():
						# controller.receive_event(event)
			dt = self.__clock.tick(60) / 1000.0
		return 0


	def exit(self):
		self.__done = True
