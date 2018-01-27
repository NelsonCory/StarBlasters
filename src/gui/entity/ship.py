from . entity import *
from core.event_manager import *
from core.resource_manager import *
from utils.vector import *
import math
import pygame

class Ship(Entity):

	def __init__(self, ship_controller, gun_controller):
		super(Ship, self).__init__()
		self.__ship_controller = ship_controller
		self.__gun_controller = gun_controller
		self.set_position((0, 0))
		self.__acceleration = (0, 0)
		self.__velocity = (0, 0)
		self.__gun_rot = 0
		self.__resource_manager = ResourceManager.get_instance()
		self.set_texture(self.__resource_manager.get_image("graphics/mothership"))
		self.__gun_image = self.__resource_manager.get_image("graphics/gun")
		self.__glow1 = self.__resource_manager.get_image("graphics/mothership_brightness_2")
		EventManager.get_instance().subscribe("ship_move", self.on_accelerate)

		self.__glow_phase = 0

	def tick(self, dt):
		self.__glow_phase += dt*5

	def draw(self, screen, cx, cy):
		pos = add_vecs(self.get_position(), (cx, cy))
		screen.blit(self.get_texture(), pos)
		screen.blit_alpha(self.__glow1, pos, (math.sin(self.__glow_phase)/2+0.5)*255)

	def on_accelerate(self, delta):
		self.__acceleration = delta
