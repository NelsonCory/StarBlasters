import pygame


class Game():

	# Initialize pygame here
	def __init__(self):
		pygame.init()

		self.__done = False
		self.__clock = pygame.time.Clock()

	# Main loop, returns exit code
	def run(self):
		# Main loop
		while not self.__done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.__done = True
			dt = self.__clock.tick(60) / 1000.0
		return 0


	def exit(self):
		self.__done = True
