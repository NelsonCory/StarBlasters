from . entity import *

class Ship(Entity):

	def __init__(self, ship_controller, gun_controller):
		super(Ship, self).__init__()
		self.__ship_controller = ship_controller
		self.__gun_controller = gun_controller

	def tick(self, dt):
		pass

	def draw(self, screen, cx, cy):
		pass
