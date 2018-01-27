import pygame

class Screen:

	def __init__(self, resolution=(1280, 720)):
		self.__resolution = resolution
		self.__surface = pygame.display.set_mode(resolution)
		self.__scene = None

	def blit(self, *args, **kwargs):
		self.__surface.blit(*args, **kwargs)

	def draw(self):
		self.__surface.fill((0, 0, 0))
		self.__scene.draw(self)
		pygame.display.flip()

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
