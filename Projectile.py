import pygame, sys, math
from pygame.locals import *

class Projectile(pygame.sprite.Sprite):
        def __init__(self,X,Y):
                pygame.sprite.Sprite.__init__(self)
                self.cannonball= pygame.image.load('cannonball.png')
                self.speedX = 20
                self.speedY = 0 
                self.imageWidth= 59
                self.imageHeight= 59
                self.originX = X + self.imageWidth
                self.originY = Y
                self.posX =  self.originX
                self.posY = self.originY
                self.isShot = 0
                self.damage = 25
                self.directionX = 1
                self.directionY = 1

        def getDmg(self):
            return self.damage

        def setDirection(self,dX,dY):
            self.directionX = dX
            self.directionY = dY

        def getWidth(self):
            return self.pandaw

        def getHeight(self):
            return self.pandah

        def getX(self):
            return self.posX

        def startShot(self):
            self.isShot = 1

     #returns the tanks Y position
        def getY(self):
            return self.posY

        def getRect(self):
            return pygame.Rect(self.posX,self.posY, self.imageWidth, self.imageHeight)

        def draw_Projectile(self, screen):
            if(self.isShot == 1):
                screen.blit(self.cannonball, (self.posX, self.posY))
        
        def IsInBounds(self,maxX,maxY,moveX,moveY):
                #if self.posX + moveX >= 0 and self.posX + self.imageWidth + moveX  <= maxX:
            if self.isShot == 1:
                self.posX = (self.posX + moveX)
                if self.posX + self.imageWidth + self.speedX  > maxX:
                    self.isShot = 0
                    self.posX =  self.originX
                    self.posY = self.originY
                if self.posY + self.speedY >= 0 and self.posY + self.imageHeight + self.speedY  <= maxY:
                        self.posY = (self.posY + moveX)