import pygame

class Entity():

	def __init__(self):
		self.__position = (0, 0)
		self.__texture = None
		self.__scene = None

	def draw(self, screen, cx, cy):
		pass

	def tick(self, dt):
		pass

	def get_position(self):
		return self.__position

	def set_position(self, position):
		self.__position = position

	def get_rect(self):
		rect = self.__texture.get_rect()
		return pygame.Rect(self.__position[0], self.__position[1], rect[2], rect[3])

	def get_scene(self):
		return self.__scene

	def set_scene(self, scene):
		self.__scene = scene

	def set_texture(self, texture):
		self.__texture = texture

	def get_texture(self):
		return self.__texture
