from settings import vertical_tile_number, tile_size, screen_width, screen_height
import pygame
from tiles import AnimatedTile, StaticTile
from support import import_folder
from random import choice, randint

pygame.display.set_caption("Legend of the Wizard and Ninja")

class Sky:
	def __init__(self,horizon,style = 'level'):
		self.bg_images = []
		for i in range(1,6):
			bg_image = pygame.image.load(r'....graphics\decoration\sky\plx-' + str(i) + '.png').convert_alpha()
			self.bg_images.append(bg_image)
		self.bg_width = self.bg_images[0].get_width()
		self.bg_height = self.bg_images[0].get_height()

		self.horizon = horizon

		self.style = style
		if self.style == 'overworld':
			palm_surfaces = import_folder(r'....\graphics\overworld\palms')
			self.palms = []

			for surface in [choice(palm_surfaces) for image in range(10)]:
				x = randint(0,screen_width)
				y = (self.horizon * tile_size) + randint(50,100)
				rect = surface.get_rect(midbottom = (x,y))
				self.palms.append((surface,rect))

			cloud_surfaces = import_folder(r'....\graphics\overworld\clouds')
			self.clouds = []

			for surface in [choice(cloud_surfaces) for image in range(10)]:
				x = randint(0,screen_width)
				y = randint(0,(self.horizon * tile_size) - 100)
				rect = surface.get_rect(midbottom = (x,y))
				self.clouds.append((surface,rect))

	def draw(self,surface):
		for x in range(5):
			speed = 1
			for i in self.bg_images:
				surface.blit(i, ((x*self.bg_width) - speed,0))
				speed += 0.2

class Water:
	def __init__(self,top,level_width):
		water_start = -screen_width
		water_tile_width = 192
		tile_x_amount = int((level_width + screen_width * 2) / water_tile_width)
		self.water_sprites = pygame.sprite.Group()

		for tile in range(tile_x_amount):
			x = tile * water_tile_width + water_start
			y = top 
			sprite = AnimatedTile(50,x,y,r'....\graphics\decoration\water')
			self.water_sprites.add(sprite)

	def draw(self,surface,shift):
		self.water_sprites.update(shift)
		self.water_sprites.draw(surface)