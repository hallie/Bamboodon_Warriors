import pygame, sys , math
from pygame.locals import *
from Tank import *

#Alien = alienAttack(gameWidth*3/4, groundHeight-50)
#Alien.moveAlien(gameWidth,gameHeight)

class alienAttack(pygame.sprite.Sprite):

    def __init__(self,X,Y):
        self.health = 100
        self.posX = X
        self.posY = Y
        self.alienw = 267
        self.alienh = 306
        self.alienImages = pygame.image.load('enemies/ship.png')
        self.attackImage = pygame.image.load('enemies/ship.png')
        self.damage = 5

    def getDmg(self):
        return self.damage
        
    def getX(self):
        return self.posX

    

    def getY(self):
        return self.posY
    
    def IsInBounds(self,maxX,maxY,moveX,moveY):
        if self.posX + moveX >= 0 and self.posX + self.alienw + moveX  <= maxX:
            self.posX = self.posX + moveX + 15
           
        if self.posY + moveY >= 0 and self.posY + self.alienh + moveY  <= maxY:
            self.posY = self.posY + moveY + 15
             
    def getImage(self):
        return self.alienImages

class alienList():
    def __init__(self,X,Y):
	self.alienList = []
        self.clock = 0
        self.posX = X
        self.posY = Y
        self.moveX = -2
        self.moveY = 0
	self.limit = 2

    def moveAlien(self,maxX,maxY):
        self.clock = self.clock + 1
        if self.clock > 80 and len(self.alienList) < self.limit :
            self.clock = 0
            self.alienList.append(alienAttack(self.posX,self.posY))
            
        for tempAlien in self.alienList:
            tempAlien.IsInBounds(maxX,maxY,self.moveX,self.moveY)

    def getCount(self):
        return len(self.alienList)-1
        
    def drawAlien(self,screen):
        for i in range(0,len(self.alienList)-1):
            screen.blit(self.alienList[i].getImage(),(self.alienList[i].getX(),self.alienList[i].getY()))

