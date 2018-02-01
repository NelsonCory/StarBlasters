from . scene import *
from core.controller.menu_controller import *
from core.resource_manager import *
from core.score_database import *

class MainMenu(Scene):

	def __init__(self):
		super(MainMenu, self).__init__()
		self.__menu_controller = MenuController()
		self.add_controller(self.__menu_controller)
		self.set_camera(Camera())
		self.__font = self.__font = ResourceManager.get_instance().get_font("fonts/Roboto-Regular", 50)
		self.__music = ResourceManager.get_instance().get_music("music/main_menu_theme")
		self.__music.play(-1, 0)

	def __del__(self):
		self.__music.stop()

	def draw(self, screen):
		image = ResourceManager.get_instance().get_image("graphics/menu_prompt")
		screen.blit(image,(0,0))
		super(MainMenu, self).draw(screen)
		text = self.__font.render("Top Score:", False, (255, 255, 255))
		text_rect = text.get_rect()
		score_value = ScoreDatabase.get_instance().get_scores()[0]
		score = self.__font.render(str(score_value), False, (255, 255, 255))
		score_rect = score.get_rect()
		x_offset = (text_rect.width - score_rect.width)/2
		screen.blit(text, (80, 40))
		screen.blit(score, (80+x_offset, 110))
