from . scene import *
from core.camera import *
from core.controller.gun_controller import *
from core.controller.ship_controller import *
from gui.entity.asteroid import *
from gui.entity.ship import *
from utils.vector import *

class World(Scene):

	MAX_ENTITIES = 70

	def __init__(self):
		super(World, self).__init__()

		self.__bg = ResourceManager.get_instance().get_image("graphics/background_1")
		self.__ship_controller = ShipController()
		self.__gun_controller = GunController()
		self.__ship = Ship(self.__ship_controller, self.__gun_controller)
		self.set_camera(Camera())
		self.add_controller(self.__ship_controller)
		self.add_controller(self.__gun_controller)
		self.add_entity(self.__ship)
		EventManager.get_instance().subscribe("world_ready")

	def tick(self, dt):
		super(World, self).tick(dt)
		camera = self.get_camera()
		x, y, width, height = self.__ship.get_rect()
		self.get_camera().set_x(x-(640 - width/2))
		self.get_camera().set_y(y-(360 - height/2))

	def draw(self, screen):
		camera = self.get_camera()
		cx  = camera.get_x()
		cy  = camera.get_y()

		screen.blit(self.__bg, (-cx/2, -cy/2))
		super(World, self).draw(screen)

	def init_asteroids(self):
		pass

