import os
import pygame

class ResourceManager:

	__instance = None

	def __init__(self, path):
		self.__base_path = os.path.dirname(path) + "/res/"
		self.__graphics = {}
		self.__sounds = {}
		for file in os.listdir(self.__base_path + "graphics/"):
			key = "graphics/" + os.path.splitext(os.path.basename(file))[0]
			surface = pygame.image.load(os.path.join(self.__base_path, "graphics/" + file))
			self.__graphics[key] = surface
		for file in os.listdir(self.__base_path + "sounds/"):
			key = "sounds/" + os.path.splitext(file)[0]
			sound = pygame.mixer.Sound(os.path.join(self.__base_path, "sounds/" + file))
			self.__sounds[key] = sound

		ResourceManager.__instance = self

	@staticmethod
	def get_instance():
		return ResourceManager.__instance

	def get_image(self, key):
		return self.__graphics[key]

	def get_sound(self, key):
		return self.__sounds[key]
