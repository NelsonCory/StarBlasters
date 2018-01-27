from core.event_manager import *
from utils.vector import *
import pygame

class ShipController():

	def __init__(self):
		super(ShipController, self).__init__()
		self.__key_delta = [
			0, 0, 0, 0 # Up Down Left Right
		]
		self.__joy_delta = [0, 0] # x, y
		self.__dirty = False

		#set up joystick
		self.__joystick = pygame.joystick.Joystick(0) #first joystick
		self.__joystick.init()
		self.__axes = self.__joystick.get_numaxes()

	def key_press(self, event):
		if event.key == (pygame.K_w):
			self.__key_delta[0] = 1
		if event.key == (pygame.K_s):
			self.__key_delta[1] = 1
		if event.key == (pygame.K_a):
			self.__key_delta[2] = 1
		if event.key == (pygame.K_d):
			self.__key_delta[3] = 1
		if event.key in (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d):
			self.__dirty = True

	def key_release(self, event):
		if event.key == (pygame.K_w):
			self.__key_delta[0] = 0
		if event.key == (pygame.K_s):
			self.__key_delta[1] = 0
		if event.key == (pygame.K_a):
			self.__key_delta[2] = 0
		if event.key == (pygame.K_d):
			self.__key_delta[3] = 0
		if event.key in (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d):
			self.__dirty = True

	def update(self):
		if not self.__dirty:
			return
		key_vector = normalize([
			-self.__key_delta[2] + self.__key_delta[3],
			-self.__key_delta[0] + self.__key_delta[1]
		])

		if key_vector == (0.0, 0.0):
			dx, dy = self.__joy_delta
		else:
			dx, dy = key_vector
		self.__dirty = False
		EventManager.get_instance().send("ship_move", (dx, dy))

	def receive_joy(self):
		self.__joy_delta = (self.__axes[0], self.__axes[1])
		#print(self.__joy_delta) #DEBUG
