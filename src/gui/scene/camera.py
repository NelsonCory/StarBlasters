import pygame

class Camera:

	def __init__(self, x = 0, y = 0):
		self.__x = x
		self.__y = y
		self.__width = 0
		self.__height = 0

	# Accessors ------------------------------------------------------------------------------------

	def get_dimensions(self):
		return self.__width, self.__height

	def get_offset(self):
		self.__nx = self.__width / 2 - self.__x
		self.__ny = self.__height / 2 - self.__y
		return self.__nx, self.__ny

	def get_position(self):
		return self.__x, self.__y

	def get_rect(self):
		return pygame.Rect(self.__x, self.__y, self.__width, self.__height)

	# Mutators -------------------------------------------------------------------------------------

	def set_dimensions(self, width, height):
		self.__width = width
		self.__height = height

	def set_position(self, x, y):
		self.__x = x
		self.__y = y
