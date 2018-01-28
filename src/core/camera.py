import pygame
class Camera:

	def __init__(self, x = 0, y = 0, width = 1280, height = 720):
		self.__x = x
		self.__y = y
		self.__width = width
		self.__height = height

	def get_offset(self):
		self.__nx = self.__width / 2 - self.__x
		self.__ny = self.__height / 2 - self.__y
		return self.__nx, self.__ny

	#get pygame rect object
	def get_rect(self):
		return pygame.Rect(self.__x,self.__y,self.__width,self.__height)

	def get_position(self):
		return self.__x, self.__y

	def get_x(self):
		return self.__x

	def get_y(self):
		return self.__y

	def set_x(self, x):
		self.__x = x

	def set_y(self, y):
		self.__y = y
