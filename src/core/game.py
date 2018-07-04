# Grant the ability to get the current game instance across the program
def get_game_instance():
	return Game.get_instance()

from . event_manager import *
from . resource_manager import *
from . score_database import *
from gui.scene.main_menu import *
from gui.scene.world import *
from gui.scene.haikus import *
from gui.screen import *
import pygame

class Game():

	RESOLUTION = (1280, 720)

	__instance = None

	@staticmethod
	def get_instance():
		return Game.__instance

	# Initialize pygame here
	def __init__(self, path):
		Game.__instance = self
		self.init_pygame()
		self.__event_manager = EventManager()
		self.__resource_manager = ResourceManager(path)
		self.__score_database = ScoreDatabase(path)
		self.__score_database.load()
		self.__screen = Screen(Game.RESOLUTION)
		self.__done = False
		self.__clock = pygame.time.Clock()

		self.__event_manager.subscribe("on_start", self.on_start)
		self.__event_manager.subscribe("main_menus", self.set_main_menu)
		self.__event_manager.subscribe("haikus", self.set_haikus)

	def init_pygame(self):
		pygame.mixer.pre_init(44100, -16, 2, 2048)
		pygame.mixer.init()
		pygame.init()
		pygame.mouse.set_visible(False) #CHECK ON MACHINE

	# Main loop, returns exit code
	def run(self):
		dt = 0
		self.__screen.set_scene(MainMenu())
		# Main loop
		while not self.__done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.__done = True
				elif event.type == pygame.KEYDOWN:
					for controller in self.__screen.get_scene().get_controllers():
						controller.key_press(event)
				elif event.type == pygame.KEYUP:
					for controller in self.__screen.get_scene().get_controllers():
						controller.key_release(event)
				elif event.type == pygame.JOYAXISMOTION or event.type == pygame.JOYBUTTONDOWN:
					for controller in self.__screen.get_scene().get_controllers():
						controller.receive_joy(event)


			for controller in self.__screen.get_scene().get_controllers():
				controller.update()
			self.__event_manager.dispatch()
			self.__screen.tick(dt)
			self.__screen.draw()

			dt = self.__clock.tick(60) / 1000.0
		return 0

	def on_start(self, event):
		self.__screen.set_scene(World())

	def exit(self):
		self.__done = True

	def set_main_menu(self, event):
		self.__screen.set_scene(MainMenu())

	def set_haikus(self, event):
		self.__screen.set_scene(Haikus())

	# Accessors ------------------------------------------------------------------------------------

	def get_screen(self):
		return self.__screen
