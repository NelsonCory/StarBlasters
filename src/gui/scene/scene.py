from core.event_manager import *
from core.camera import *
from core.controller.ship_controller import *

class Scene:

	def __init__(self):
		self.__camera = None
		self.__controllers = []
		self.__entities = []

	def add_entity(self, entity):
		entity.set_scene(self)
		self.__entities.append(entity)

	def add_controller(self, controller):
		self.__controllers.append(controller)

	def draw(self, screen):
		camera_rect = self.__camera.get_rect()
		for e in self.__entities:
			e_rect = e.get_rect()
			if camera_rect.colliderect(e_rect):
				e.draw(screen, -camera_rect.left, -camera_rect.top)

	def tick(self, dt):
		scale_factor = 3
		camera_rect = self.__camera.get_rect()
		process_rect = camera_rect.inflate(scale_factor, scale_factor)
		for e in self.__entities:
			e_rect = e.get_rect()
			if process_rect.colliderect(e_rect):
				e.tick(dt)

	def get_controllers(self):
		return self.__controllers

	def ready(self):
		EventManager.get_instance().send("scene_ready", self)

	def get_camera(self):
		return self.__camera

	def set_camera(self, camera):
		self.__camera = camera

