from . scene import *
from core.camera import *
from core.controller.gun_controller import *
from core.controller.ship_controller import *
from core.event_manager import *
from gui.entity.asteroid import *
from gui.entity.ship import *
import random
from utils.vector import *

class World(Scene):

	MIN_ASTEROIDS = 10

	def __init__(self):
		super(World, self).__init__()

		self.__backgrounds = [
			ResourceManager.get_instance().get_image("graphics/background_1"),
			ResourceManager.get_instance().get_image("graphics/background_2"),
			ResourceManager.get_instance().get_image("graphics/background_3")
		]
		self.__background_size = (3000, 2000)
		self.__seed = int(time.time())
		self.__ship_controller = ShipController()
		self.__gun_controller = GunController()
		self.__ship = Ship(self.__ship_controller, self.__gun_controller)
		self.__score = 0
		self.__alive = True
		self.__ready = False
		self.set_camera(Camera())
		self.add_controller(self.__ship_controller)
		self.add_controller(self.__gun_controller)
		self.add_entity(self.__ship)
		EventManager.get_instance().subscribe("award_score", self.award_score)
		EventManager.get_instance().subscribe("death", self.on_death)
		EventManager.get_instance().subscribe("scene_ready", self.on_start)
		EventManager.get_instance().subscribe("activate_asteroids", self.on_ready)

		self.__music = ResourceManager.get_instance().get_music("music/game_intro")
		self.__music.play()

	def tick(self, dt):
		super(World, self).tick(dt)
		if self.__alive:
			x, y, width, height = self.__ship.get_rect()
			self.get_camera().set_x(x-(640 - width/2))
			self.get_camera().set_y(y-(360 - height/2))
		if self.__ready:
			while len(self.get_entities()) < World.MIN_ASTEROIDS:
				self.spawn_asteroid()

	def draw(self, screen):
		camera = self.get_camera()
		cx = -camera.get_x()/2
		cy = -camera.get_y()/2
		chunk_coords = cx//self.__background_size[0], cy//self.__background_size[1]
		print(chunk_coords)
		background = self.get_background(chunk_coords[0], chunk_coords[1])
		screen.blit(background, (cx, cy))
		super(World, self).draw(screen)

	def get_background(self, x, y):
		v = (int(x) << 16) + int(y) + self.__seed
		random.seed(v)
		bg = self.__backgrounds[random.randrange(0, len(self.__backgrounds))]
		random.seed(None)
		return bg

	def spawn_asteroid(self):
		prect = self.get_processing_rect()
		crect = self.get_camera().get_rect()
		x, y = crect.x, crect.y
		bounds = pygame.Rect(x, y, 200, 200)
		while crect.colliderect(bounds):
			x = random.randrange(prect.x, prect.x+prect.width)
			y = random.randrange(prect.y, prect.y+prect.height)
			bounds = pygame.Rect(x, y, 200, 200)
		self.add_entity(Asteroid(None, (x, y)))

	def award_score(self, value):
		self.__score += value

	def on_death(self, event):
		print("You dead")
		self.__alive = False
		self.__ship.kill()
		EventManager.get_instance().unsubscribe("death", self.on_death)
		print("You dead. Final score:", self.__score)

	def on_start(self, event):
		EventManager.get_instance().send("activate_asteroids", None, 6.84)

	def on_ready(self, event):
		self.__music = ResourceManager.get_instance().get_music("music/game_music")
		self.__music.play(-1, 0)	
		self.__ready = True
