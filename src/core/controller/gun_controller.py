from core.controller.controller import *
from core.event_manager import *
import pygame

class GunController(Controller):

	def __init__(self):
		super(GunController, self).__init__()
		
		self.__key_delta = [
			0, 0, 0, 0 #Up Down Left Right
		]
		self.__joy_delta = [0, 0] # x, y
		
		#set up joystick
		try:
			self.__joystick = pygame.joystick.Joystick(1) #first joystick
			self.__joystick.init()
			self.__axes = self.__joystick.get_numaxes()
			self.__buttons = self.__joystick.get_numbuttons()
		except:
			print("ERROR: NOT ENOUGH JOYSTICKS- GunController")
		
	def key_press(self, event):
		if event.key == K_UP:
			pass
		if event.key == K_DOWN:
			pass
	
	def key_release(self, event):
		if event.key == K_UP:
			pass
		if event.key == K_DOWN:
			pass
			
	def fire_gun(self):
		
		#keyboard
		if event.key == pygame.K_SPACE:
			pass
		
		#controller
		try:
			if(self.__buttons[0]): #if the "A" button is down
				pass
		except:
			print("ERROR: NOT ENOUGH JOYSTICKS- fire_gun")
			
	