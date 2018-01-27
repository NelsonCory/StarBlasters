import pygame

class Screen:

	def __init__(self, resolution=(1280, 720)):
		self.__resolution = resolution
		self.__surface = pygame.display.set_mode(resolution)
		self.__scene = None

	def draw(self):
		self.__scene.draw(self)

	def get_resolution(self):
		return self.__resolution

