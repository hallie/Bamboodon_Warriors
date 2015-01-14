import pygame, sys , math
from pygame.locals import *
from sound import *
from Tank import *
from ETank import *

class SpriteManager(pygame.sprite.Sprite):

    def __init__(self,plTank,etank,aPandas):
        self.player = plTank
        self.ETanks = etank
        self.PandaList = aPandas
        #self.Aliens = alien
      #spritecollide(sprite, group, dokill) 
#>>> for bomb in sprite.spritecollide(player, bombs, 1):
#    ...     boom_sound.play()
#    ...     Explosion(bomb, 0)

    def do_collide(self,enemyList):
        for enemy in enemyList.getList():
            otherRect = pygame.Rect(enemy.getX(),enemy.getY(), enemy.getWidth(), enemy.getHeight())
            #if self.player.getRect().colliderect(otherRect) #self.player.collide(otherRect):
            if self.player.getRect().colliderect(otherRect) == True:
                self.player.setHP(enemy.getDmg())
            for shot in self.player.getCannon():
                #if self.player.getRect().colliderect(otherRect) #self.player.collide(otherRect):
                if shot.getRect().colliderect(otherRect) == True:
                    enemy.setHP(shot.getDmg()) 

    def checkAllCollide(self):
        self.do_collide(self.ETanks)
        self.do_collide(self.PandaList)