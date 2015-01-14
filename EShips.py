import pygame, sys , math
from pygame.locals import *
from Tank import *

class ETank(pygame.sprite.Sprite):

    def __init__(self,X,Y):
        self.health = 100
        self.posX = X
        self.posY = Y
        self.shipw = 150
        self.shiph = 100
        self.shipList =[Tank(X,Y)]
        self.shipImages = pygame.image.load('enemies/ship.png')
        self.shipList[0].setImages(self.shipImages,self.attackImages)
        self.clock = 1
        self.moveX = -1
        self.moveY = 0
        self.limit = 5

    def getX(self):
        return self.posX


    def getY(self):
        return self.posY
    
    def moveTank(self,maxX,maxY):
        self.clock += 1
        if self.clock > 80 and len(self.tankList) < self.limit :
            self.clock = 0
            self.tankList.append(Tank(self.posX,self.posY))
            self.tankList[len(self.tankList)-1].setImages(self.tankImages,self.attackImages)  
        
        for i in range(0,len(self.tankList)-1):
            self.tankList[i].IsInBounds(maxX,maxY,self.moveX,self.moveY)


    def getCount(self):
        return len(self.tankList)-1
        
    def drawTank(self,screen):
        for i in range(0,len(self.tankList)-1):
            screen.blit(self.tankList[i].getImage(),(self.tankList[i].getX(),self.tankList[i].getY()))  
        pygame.display.update()    

