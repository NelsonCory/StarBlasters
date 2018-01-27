import pygame
class Camera:
    
	def __init__(self,x,y, width = 1280, height = 720):
		self._x = x
		self._y = y
		self._width = width
		self._height = height

	def get_offset(self):
		self._nx = self._width / 2 - self._x
		self._ny = self._height / 2 - self._y
		return self._nx, self._ny

	#get pygame rect object
	def getRect(self):
		return pygame.Rect(self._x,self._y,self._width,self._height)
		
	def get_x(self):
		return self._x

	def get_y(self):
		return self._y

	def set_x(self, x):
		self._x = x

	def set_y(self, y):
		self._y = y