import pygame

class Screen:

	def __init__(self, resolution=(1280, 720)):
		self.__resolution = resolution
		self.__surface = pygame.display.set_mode(resolution)
		self.__scene = None

	def draw(self):
		self.__scene.draw(self)

	def tick(self, dt):
		self.__scene.tick(dt)

	def get_resolution(self):
		return self.__resolution

	def get_scene(self):
		return self.__scene

	def set_scene(self, scene):
		if self.__scene:
			del self.__scene
		self.__scene = scene
		self.__scene.ready()



