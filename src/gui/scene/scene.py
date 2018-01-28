from core.event_manager import *
from core.camera import *
from core.controller.ship_controller import *

class Scene:

	PROCESSING_SCALE_FACTOR = 3

	def __init__(self):
		self.__camera = None
		self.__controllers = []
		self.__entities = []

	def add_entity(self, entity):
		entity.set_scene(self)
		self.__entities.append(entity)

	def remove_entity(self, entity):
		self.__entities.remove(entity)

	def add_controller(self, controller):
		self.__controllers.append(controller)

	def remove_controller(self, controller):
		self.__controllers.remove(controller)

	def draw(self, screen):
		camera_rect = self.__camera.get_rect()
		for e in self.__entities:
			e_rect = e.get_rect()
			if camera_rect.colliderect(e_rect):
				e.draw(screen, -camera_rect.left, -camera_rect.top)

	def tick(self, dt):
		process_rect = self.get_processing_rect()
		to_despawn = []
		for e in self.__entities:
			e_rect = e.get_rect()
			if process_rect.colliderect(e_rect):
				e.tick(dt)
			else:
				to_despawn.append(e)
		for e in to_despawn:
			self.remove_entity(e)
			del e

	def get_controllers(self):
		return self.__controllers

	def get_entities(self):
		return self.__entities

	def get_processing_rect(self):
		x, y, width, height = self.__camera.get_rect()
		x -= width
		y -= height
		width *= 3
		height *= 3
		return pygame.Rect(x, y, width, height)


	def ready(self):
		EventManager.get_instance().send("scene_ready", self)

	def get_camera(self):
		return self.__camera

	def set_camera(self, camera):
		self.__camera = camera

