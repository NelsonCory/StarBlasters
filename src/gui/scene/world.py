from . scene import *
from core.camera import *
from core.controller.gun_controller import *
from core.controller.ship_controller import *
from gui.entity.asteroid import *
from gui.entity.ship import *

class World(Scene):

	def __init__(self):
		super(World, self).__init__()

		self.__ship_controller = ShipController()
		self.__gun_controller = GunController()
		self.__ship = Ship(self.__ship_controller, self.__gun_controller)
		self.set_camera(Camera())
		self.add_controller(self.__ship_controller)
		self.add_controller(self.__gun_controller)
		self.add_entity(self.__ship)
		self.add_entity(Asteroid())

	def tick(self, dt):
		super(World, self).tick(dt)

