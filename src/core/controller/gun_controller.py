from . controller import *
from core.event_manager import *
import pygame

class GunController(Controller):

	def __init__(self):
		super(GunController, self).__init__()

		self.__key_delta = [
			0, 0 #Left Right
		]
		self.__joy_delta = [0, 0] # x, y

		self.__dirty = False

		#set up joystick
		try:
			self.__joystick = pygame.joystick.Joystick(1) #first joystick
			self.__joystick.init()
			self.__axes = self.__joystick.get_numaxes()
			self.__buttons = self.__joystick.get_numbuttons()
		except:
			print("ERROR: NOT ENOUGH JOYSTICKS- GunController")

	def key_press(self, event):
		if event.key == pygame.K_LEFT:
			self.__key_delta[0] = 1
		if event.key == pygame.K_RIGHT:
			self.__key_delta[1] = 1
		if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
			self.__dirty = True

	def key_release(self, event):
		if event.key == pygame.K_LEFT:
			self.__key_delta[0] = 0
		if event.key == pygame.K_RIGHT:
			self.__key_delta[1] = 0
		if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
			self.__dirty = True

	def fire_gun(self, event):

		#keyboard
		if event.key == pygame.K_SPACE:
			pass

		#controller
		try:
			if(self.__buttons[0]): #if the "A" button is down
				pass
		except:
			print("ERROR: NOT ENOUGH JOYSTICKS- fire_gun")

	def update(self):
		if not self.__dirty:
			return
		delta = self.__key_delta[0] - self.__key_delta[1]
		EventManager.get_instance().send("gun_rotate", delta)
