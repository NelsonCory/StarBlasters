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
		self.add_entity(Asteroid(3))
		self.add_entity(Asteroid(2))
		self.add_entity(Asteroid(1))

	def tick(self, dt):
		super(World, self).tick(dt)
		camera = self.get_camera()
		x, y, width, height = self.__ship.get_rect()
		self.get_camera().set_x(x-(640 - width/2))
		self.get_camera().set_y(y-(360 - height/2))

