from . entity import *
from core.event_manager import *
from core.resource_manager import *
from utils.vector import *
import math
import pygame

class Ship(Entity):

	ACCELERATION = 5

	def __init__(self, ship_controller, gun_controller):
		super(Ship, self).__init__()
		self.__ship_controller = ship_controller
		self.__gun_controller = gun_controller
		self.set_position((0, 0))
		self.__acceleration = (0, 0)
		self.__velocity = (0, 0)
		self.__gun_rot = 3*math.pi/2
		self.__resource_manager = ResourceManager.get_instance()
		self.set_texture(self.__resource_manager.get_image("graphics/mothership"))
		self.__gun_image = self.__resource_manager.get_image("graphics/mothership_gun")
		self.__glow1 = self.__resource_manager.get_image("graphics/mothership_brightness_2")
		EventManager.get_instance().subscribe("ship_move", self.on_accelerate)

		self.__glow_phase = 0

	def tick(self, dt):
		self.__glow_phase += dt*5
		self.__velocity = add_vecs(self.__velocity, scale_vec(dt, self.__acceleration))
		self.set_position(add_vecs(self.get_position(), self.__velocity))
		print(self.__velocity)

	def draw(self, screen, cx, cy):
		pos = add_vecs(self.get_position(), (cx, cy))
		screen.blit(self.get_texture(), pos)
		screen.blit_alpha(self.__glow1, pos, (math.sin(self.__glow_phase)/2+0.5)*255)

		ship_radius = self.get_texture().get_rect().width / 2
		gun_radius = ship_radius + 20
		gun_center = scale_vec(gun_radius, (math.cos(self.__gun_rot), math.sin(self.__gun_rot)))
		rotated_gun = pygame.transform.rotate(self.__gun_image, self.__gun_rot - math.pi/2)
		gun_loc = add_vecs(gun_center, scale_vec(0.5, self.__gun_image.get_rect().size))
		screen.blit(self.__gun_image, gun_loc)

	def on_accelerate(self, delta):
		self.__acceleration = scale_vec(Ship.ACCELERATION, delta)
