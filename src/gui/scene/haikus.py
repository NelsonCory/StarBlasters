from . scene import *
from core.resource_manager import *
from core.event_manager import *
import random

# Note:
# Haiku selection is a bit funky, TODO - fix that

first_lines = ("Space is quite scary", \
	"Unblemished and clear", \
	"Is it cold in space?", \
	"Don't let that hit us", \
	)
second_lines = ("Also, it is beautiful", \
	"Space is uninterrupted", \
	"I don't know, but you tell me", \
	"Oh, great, now there's a hull breach", \
	)
third_lines = ("Mostly scary though", \
	"Then suddenly rocks", \
	"Because you just died", \
	"Learn to shoot lasers", \
	)

class Haikus(Scene):
	

	

	def __init__(self):
		super(Haikus, self).__init__()
		self.set_camera(Camera())
		self.__font = self.__font = ResourceManager.get_instance().get_font("fonts/Roboto-Regular", 50)
		self.__chosen_haiku = random.randint(0,len(first_lines)-1) #this ensures a different haiku can be selected every time the haiku screen is called

	def __del__(self):
		pass

	def draw(self, screen):

		image = ResourceManager.get_instance().get_image("graphics/background_2")
		screen.blit(image,(0,0))
		super(Haikus, self).draw(screen)
		#fix this

		line_one = self.__font.render(first_lines[self.__chosen_haiku], False, (255, 255, 255))
		line_two = self.__font.render(second_lines[self.__chosen_haiku], False, (255, 255, 255))
		line_three = self.__font.render(third_lines[self.__chosen_haiku], False, (255, 255, 255))
		screen.blit(line_one, (150, 200))
		screen.blit(line_two, (150, 250))
		screen.blit(line_three, (150, 300))
		EventManager.get_instance().send("main_menus", None, 4)
		
	
