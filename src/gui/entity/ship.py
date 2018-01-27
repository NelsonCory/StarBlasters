from . entity import *
from core.event_manager import *
from core.resource_manager import *
import math
import pygame

class Ship(Entity):

	def __init__(self, ship_controller, gun_controller):
		super(Ship, self).__init__()
		self.__ship_controller = ship_controller
		self.__gun_controller = gun_controller
		self.__position = (0, 0)
		self.__acceleration = (0, 0)
		self.__velocity = (0, 0)
		self.__gun_rot = 0
		self.__resource_manager = ResourceManager.get_instance()
		self.set_texture(self.__resource_manager.get_image("graphics/ship"))
		self.__gun_image = self.__resource_manager.get_image("graphics/gun")
		EventManager.get_instance().subscribe("ship_move", self.on_accelerate)

	def tick(self, dt):
		pass

	def draw(self, screen, cx, cy):
		screen.blit(self.get_texture(), self.__position)

	def on_accelerate(self, delta):
		pass
