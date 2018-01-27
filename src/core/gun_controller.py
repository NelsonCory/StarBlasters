from . event_manager import *
import pygame

class GunController:

    def __init__(self):

    def receive_event(self, event):
        em = EventManager.get_instance()

        if event.key == (pygame.K_w):
            em.send("shoot_up", -1)

        elif event.key == (pygame.K_a):
            em.send("shoot_left", -1)

        elif event.key == (pygame.K_s):
            em.send("shoot_down", 1)

        elif event.key == (pygame.K_d):
            em.send("shoot_right", 1)
