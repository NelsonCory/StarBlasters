from core.event_manager import *
import pygame

class MenuController():

	def __init__(self):
		super(MenuController, self).__init__()

		#set up joystick 1
		try:
			self.__joystick = pygame.joystick.Joystick(0) #first joystick
			self.__joystick.init()
			self.__buttons = self.__joystick.get_button(3)
		except:
			print("ERROR: NOT ENOUGH JOYSTICKS - ShipController")
		
		#set up joystick 2
		try:
			self.__joystick2 = pygame.joystick.Joystick(1)
			self.__joystick2.init()
			self.__buttons2 = self.__joystick2.get_button(3)
		except:
			pass
	def key_release(self, event):
		#go to world, keyboard command
		if event.key == pygame.K_SPACE:
			EventManager.get_instance().send("on_start", None)
		
		
	def update(self):
		if not self.__dirty:
			return

	def receive_joy(self):
		#joystick2
		try:
			if(self.__buttons[0]):
				EventManager.get_instance().send("on_start", None)
		except:
			print("ERROR - menuController, receive view")
		#joystick2
		try:
			if(self.__buttons2[0]):
				EventManager.get_instance().send("on_start", None)
		except:
			pass
			