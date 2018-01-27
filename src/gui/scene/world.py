from . scene import *
from core.controller.gun_controller import *
from core.controller.ship_controller import *

class World(Scene):

	def __init__(self):
		super(World, self).__init__()
		self.__shipController = ShipController()
		self.__gunController = GunController()
		self.addController(self.__shipController)
		self.addController(self.__gunController)
