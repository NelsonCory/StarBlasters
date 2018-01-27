from . event_manager import *
import pygame

class ShipController:

    def __init__(self):
        pass

    def receive_event(self, event):
        em = EventManager.get_instance()

        if event.key == (pygame.K_w):
            em.send("ship_up", -1)

        elif event.key == (pygame.K_a):
            em.send("ship_left", -1)

        elif event.key == (pygame.K_s):
            em.send("ship_down", 1)

        elif event.key == (pygame.K_d):
            em.send("ship_right", 1)
