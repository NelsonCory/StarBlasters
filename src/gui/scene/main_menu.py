from . scene import *
from core.controller.menu_controller import *
from core.resource_manager import *

class MainMenu(Scene):

	def __init__(self):
		super(MainMenu, self).__init__()
		self.__menu_controller = MenuController()
		self.add_controller(self.__menu_controller)
		self.set_camera(Camera())
		self.__music = ResourceManager.get_instance().get_music("music/main_menu_theme")
		self.__music.play(-1, 0)

	def __del__(self):
		self.__music.stop()

	def draw(self, screen):
		image = ResourceManager.get_instance().get_image("graphics/menu_prompt")
		screen.blit(image,(0,0))
		super(MainMenu, self).draw(screen)
