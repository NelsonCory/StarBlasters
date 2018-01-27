from . entity import *
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
		self.__ship_image = self.__resource_manager.get_image("graphics/ship")
		self.__gun_image = self.__resource_manager.get_image("graphics/gun")

	def tick(self, dt):
		pass

	def draw(self, screen, cx, cy):
		screen.blit(self.__ship_image, self.__position)
