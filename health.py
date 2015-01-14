import pygame, sys , math
from pygame.locals import *
from Tank import *

class health(pygame.sprite.Sprite):
        def _init_(self,tank):
		self.health = Tank(health)
		self.filled100 = pygame.image.load('statsbar/statbar100.png')
		self.filled90 = pygame.image.load('statsbar/statbar90.png')
		self.filled80 = pygame.image.load('statsbar/statbar80.png')
		self.filled70 = pygame.image.load('statsbar/statbar70.png')
		self.filled60 = pygame.image.load('statsbar/statbar60.png')
		self.filled50 = pygame.image.load('statsbar/statbar50.png')
		self.filled40 = pygame.image.load('statsbar/statbar40.png')
		self.filled30 = pygame.image.load('statsbar/statbar30.png')
		self.filled20 = pygame.image.load('statsbar/statbar20.png')
		self.filled10 = pygame.image.load('statsbar/statbar10.png')

	def showBar(self, health):
		if self.health >= 100:
			retun self.filled100
		elif self.health >= 90:
			retun self.filled90
		elif self.health >= 80:
			retun self.filled80
		elif self.health >= 70:
			retun self.filled70
		elif self.health >= 60:
			retun self.filled60
		elif self.health >= 50:
			retun self.filled50
		elif self.health >= 40:
			retun self.filled40
		elif self.health >= 30:
			retun self.filled30
		elif self.health >= 20:
			retun self.filled20
		elif self.health >= 10:
			retun self.filled10
		#else:
			#GAME OVER
