from . hud import *
import pygame

class GameHud(Hud):

	SCORE_FONT_SIZE = 30

	def __init__(self, world):
		super(GameHud, self).__init__(world)
		self.__font = pygame.font.SysFont("Roboto", GameHud.SCORE_FONT_SIZE)

	def draw(self, screen):
		score = self.get_world().get_score()
		label = self.__font.render("Score: %d" % score, False, (255, 255, 255))
		screen.blit(label, (20, 20))
