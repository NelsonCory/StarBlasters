from core.event_manager import *
import pygame

class ShipController():

	def __init__(self):
		super(ShipController, self).__init__()

	def receive_event(self, event):
		em = EventManager.get_instance()
		dx, dy = 0, 0
		if event.key == (pygame.K_w):
			dy += -1

		if event.key == (pygame.K_a):
			dx += 1

		if event.key == (pygame.K_s):
			dx += 1

		if event.key == (pygame.K_d):
			dy += 1

		em.send("ship_move", (dx, dy))
