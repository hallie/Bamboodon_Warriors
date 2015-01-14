import pygame, sys , math
from pygame.locals import *
from Tank import *

#Panda = pandaAttack(gameWidth*3/4, groundHeight-50)
#Panda.movePanda(gameWidth,gameHeight)

class pandaAttack(pygame.sprite.Sprite):

    def __init__(self,X,Y):
        self.health = 10
        self.posX = X
        self.posY = Y
        self.pandaw = 267
        self.pandah = 306
        self.pandaImages = pygame.image.load('enemies/pandas/p2atkPanda.png')
        self.attackImage = pygame.image.load('enemies/pandas/p2slPanda.png')
        self.damage = 5

    def getDmg(self):
        return self.damage

    def getHP(self):
        return self.health

    def setHP(self,damage):
        self.health -= damage
        if(self.health < 0):
            self.health = 0

    def getX(self):
        return self.posX

    def getWidth(self):
        return self.pandaw

    def getHeight(self):
        return self.pandah

    def getY(self):
        return self.posY
    
    def IsInBounds(self,maxX,maxY,moveX,moveY):
        if self.health > 0:
            if self.posX + moveX >= 0 and self.posX + self.pandaw + moveX  <= maxX:
                self.posX = self.posX + moveX
           
            if self.posY + moveY >= 0 and self.posY + self.pandah + moveY  <= maxY:
                self.posY = self.posY + moveY
             
    def getImage(self):
        return self.pandaImages

class pandaList():
    def __init__(self,X,Y):
	self.pandaList = []
        self.clock = 0
        self.posX = X
        self.posY = Y
        self.moveX = -2
        self.moveY = 0
	self.limit = 2

    def movePanda(self,maxX,maxY):
        self.clock = self.clock + 1
        if self.clock > 50 and len(self.pandaList) < self.limit :
            self.clock = 0
            self.pandaList.append(pandaAttack(self.posX,self.posY))
            
        for tempPanda in self.pandaList:
            tempPanda.IsInBounds(maxX,maxY,self.moveX,self.moveY)

    def destroyPanda(self):
        for i in range(0, len(self.pandaList)-1):
            if self.pandaList[i].getHP() <= 0:
                self.pandaList.pop(i)

    def getCount(self):
        return len(self.pandaList)-1
        
    def getList(self):
        return self.pandaList

    def drawPanda(self,screen):
        for i in range(0,len(self.pandaList)-1):
            screen.blit(self.pandaList[i].getImage(),(self.pandaList[i].getX(),self.pandaList[i].getY()))

