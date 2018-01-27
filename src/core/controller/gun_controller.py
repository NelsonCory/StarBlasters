from core.controller.controller import *
from core.event_manager import *
import pygame

class GunController(Controller):

	def __init__(self):
		super(GunController, self).__init__()

		#set up joystick
		if(pygame.joystick.get_count == 2):
			self.__joystick = pygame.joystick.Joystick(1) #first joystick
			self.__joystick.init()
			self.__axes = self.__joystick.get_numaxes()