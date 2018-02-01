from . hud import *
from core.resource_manager import *
import pygame

class GameHud(Hud):

	SCORE_FONT_SIZE = 30

	def __init__(self, world):
		super(GameHud, self).__init__(world)
		self.__font = ResourceManager.get_instance().get_font("fonts/Roboto-Regular", GameHud.SCORE_FONT_SIZE)

	def draw(self, screen):
		score = self.get_world().get_score()
		label = self.__font.render("Score: %d" % score, False, (255, 255, 255))
		screen.blit(label, (20, 20))
