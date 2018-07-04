from core.event_manager import *
import pygame

class ShipController():

	def __init__(self):
		super(ShipController, self).__init__()
		self.__key_delta = [
			0, 0, 0, 0 # Up Down Left Right
		]
		self.__joy_delta = [0, 0] # x, y
		self.__is_boosted = False
		self.__recently_boosted = False
		self.__dirty = False

		#set up joystick
		try:
			self.__joystick = pygame.joystick.Joystick(0) #first joystick
			self.__joystick.init()
			self.__axes = self.__joystick.get_numaxes()
		except:
			print("ERROR: NOT ENOUGH JOYSTICKS - ShipController")

	def key_press(self, event):

		if event.key == (pygame.K_e) and not self.__is_boosted and not self.__recently_boosted:
			self.__is_boosted = True
			self.__boost_start = time.time()
			print("boost start")

		if event.key == (pygame.K_w):
			self.__key_delta[0] = 1
		if event.key == (pygame.K_s):
			self.__key_delta[1] = 1
		if event.key == (pygame.K_a):
			self.__key_delta[2] = 1
		if event.key == (pygame.K_d):
			self.__key_delta[3] = 1
		if event.key in (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_e):
			self.__dirty = True
		if event.key == (pygame.K_ESCAPE):
			EventManager.get_instance().send("main_menus", None)

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

		# Handle Ship Player's Speed Boost
		if self.__is_boosted and time.time() > self.__boost_start + 1:
			self.__is_boosted = False
			self.__recently_boosted = True
			self.__boost_cooldown_start = time.time()
		if self.__recently_boosted and time.time() > self.__boost_cooldown_start + 5:
			self.__recently_boosted = False
			
		#if not self.__dirty:
		#	return
		if not self.__is_boosted:
			dx = min(-self.__key_delta[2], self.__joy_delta[0]) + max(self.__key_delta[3], self.__joy_delta[0])
			dy = min(-self.__key_delta[0], self.__joy_delta[1]) + max(self.__key_delta[1], self.__joy_delta[1])
		else:
			dx = 2 * ( min(-self.__key_delta[2], self.__joy_delta[0]) + max(self.__key_delta[3], self.__joy_delta[0]) )
			dy = 2 * ( min(-self.__key_delta[0], self.__joy_delta[1]) + max(self.__key_delta[1], self.__joy_delta[1]) )
			print(dx, dy)


		self.__dirty = False
		EventManager.get_instance().send("ship_move", (dx, dy))

	def receive_joy(self, event):
		if event.type == pygame.JOYBUTTONDOWN:
			if self.__joystick.get_button(1):
				EventManager.get_instance().send("main_menus", None)
			if self.__joystick.get_button(0):
				self.__is_boosted = True
				self.__boost_start = time.time()

		axis_x = self.__joystick.get_axis(0)
		axis_y = self.__joystick.get_axis(1)
		self.__joy_delta = (axis_x, axis_y)
		self.__dirty = True
