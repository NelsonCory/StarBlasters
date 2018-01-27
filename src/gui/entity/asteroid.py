from . entity import *
from utils.vector import *
import math
import pygame
import random

class Asteroid(Entity):

	def __init__(self, size=None):
		super(Asteroid, self).__init__()
		self.__size = random.randint(1, 3)
		angle = random.uniform(0, 2*math.pi)
		speed = random.randint(50, 100)
		self.__velocity = scale_vec(speed, (math.cos(angle), math.sin(angle)))

	def tick(self, dt):
		self.set_position(add_vecs(self.get_position, scale_vec(dt, self.__velocity)))

	def draw(self, screen, cx, cy):
		pass
