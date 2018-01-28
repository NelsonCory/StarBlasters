from . entity import *
from core.event_manager import *
from core.resource_manager import *
from utils.vector import *
import math
import pygame
import random

class Asteroid(Entity):

	def __init__(self, size=None, position=(0, 0)):
		super(Asteroid, self).__init__()
		if size == None:
			self.__size = random.randint(3, 3)
		else:
			self.__size = size
		angle = random.uniform(0, 2*math.pi)
		speed = random.randint(500, 500)
		self.__velocity = scale_vec(speed, (math.cos(angle), math.sin(angle)))
		self.set_position(position)
		self.__resource_manager = ResourceManager.get_instance()
		self.set_texture(self.__resource_manager.get_image("graphics/asteroid_%d" % size))
		EventManager.get_instance().subscribe("damage", self.split)

	def tick(self, dt):
		self.set_position(add_vecs(self.get_position(), scale_vec(dt, self.__velocity)))

	def draw(self, screen, cx, cy):
		pos = add_vecs(self.get_position(), (cx, cy))
		screen.blit(self.get_texture(), pos)

	def split(self, *args):
		scene = self.get_scene()
		if self.__size > 1:
			scene.add_entity(Asteroid(self.__size - 1, self.get_position()))
			scene.add_entity(Asteroid(self.__size - 1, self.get_position()))
		EventManager.get_instance().unsubscribe("damage", self.split)
		scene.remove_entity(self)
