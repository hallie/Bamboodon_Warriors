import pygame, sys , math
from pygame.locals import *
from sound import *
from Projectile import *

class Tank(pygame.sprite.Sprite):

    def __init__(self,X,Y, rtime):
        pygame.sprite.Sprite.__init__(self,{})
        self.health = 50
        self.fireRate = 0.5 # fire rate is every half second
        self.posX = X
        self.posY = Y
        self.mySound = Sound()
        self.tankImages = [pygame.image.load('tanks/p1tank-str0.png'),pygame.image.load('tanks/p1tank-med0.png'),pygame.image.load('tanks/p1tank-high0.png')]
        self.attackImages = [pygame.image.load('tanks/p1tank-str1.png'),pygame.image.load('tanks/p1tank-med1.png'),pygame.image.load('tanks/p1tank-high1.png')]
        self.imageIndex = 0
        self.image = self.tankImages[self.imageIndex]

        self.imageWidth =168
        self.imageHeight = 71
        self.cannon = []
        self.speedX = 100
        self.speedY = 100
        self.damage = 5
        self.reloadMax = rtime
        self.reloadTime = rtime

    #get the list of cannon projectiles
    def getCannon(self):
        return self.cannon

    #gets reload time
    def getRelTime(self):
        return self.reloadTime

    def getHP(self):
        return self.health

    def setHP(self,damage):
        self.health -= damage
        if(self.health < 0):
            self.health = 0
    #gets the Damage from hitting the tank    
    def getDmg(self):
        return self.damage
        
        #returns the tanks x position
    def getX(self):
        return self.posX

     #returns the tanks Y position
    def getY(self):
        return self.posY

    def getWidth(self):
        return self.imageWidth

    

    def getRect(self):
        return pygame.Rect(self.posX,self.posY, self.imageWidth, self.imageHeight)

    def setImages(self,tnkimages,atckimages):
        self.tankImages = tnkimages
        self.attackImages = atckimages
        
    def getHeight(self):
        return self.imageHeight

    def getImage(self):
        return self.tankImages[self.imageIndex]
    
    #this function allows the tank to move while keeping it in teh bounds
    def IsInBounds(self,maxX,maxY,moveX,moveY):
        if self.health > 0:
            if self.posX + moveX >= 0 and self.posX + self.imageWidth + moveX  <= maxX:
                self.posX = self.posX + moveX
            if self.posY + moveY >= 0 and self.posY + self.imageHeight + moveY  <= maxY:
                self.posY = self.posY + moveY

    def moveByKeyBoard(self,screenW,screenH):
        self.image = self.tankImages[self.imageIndex]
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                #Press 1 to turn the cannon angle upwards
                #Press 2 to turn the cannon angle downwards
                if event.key == K_1:
                   self.imageIndex = self.imageIndex + 1
                   if self.imageIndex >= len(self.tankImages):
                        self.imageIndex = len(self.tankImages)-1
                elif event.key == K_2:
                   self.imageIndex = self.imageIndex - 1
                   if self.imageIndex < 0:
                        self.imageIndex = 0
                if event.key == K_d :
                    self.mySound.play("tank_movement")
                    self.IsInBounds(screenW,screenH,self.speedX,0)
                elif event.key == K_a :
                    self.mySound.play("tank_movement")
                    self.IsInBounds(screenW,screenH,-self.speedX,0)
                elif event.key == K_s :
                    self.mySound.play("tank_movement")
                    self.IsInBounds(screenW,screenH,0,self.speedY)
                elif event.key == K_w :
                    self.mySound.play("tank_movement")
                    self.IsInBounds(screenW,screenH,0,-self.speedY)
                if event.key == K_SPACE and self.reloadTime >= self.reloadMax:
                    self.mySound.play("explosion_tank")
                    self.cannon.append(Projectile(self.posX +self.imageWidth , self.posY))
                    self.cannon[len(self.cannon)-1].startShot()
                    self.image = self.attackImages[self.imageIndex]
                    self.reloadTime = 0 #Reload Time is like a timer for when this works again
        if(self.reloadTime<self.reloadMax):
                       self.reloadTime+=1
        for i in range(0,len(self.cannon)-1):
                    self.cannon[i].IsInBounds(screenW,screenH,20,0)
    
    def moveAI(self,screenW,screenH,moveX,moveY):
        self.image = self.tankImages[self.imageIndex]
        if self.reloadTime >= self.reloadMax:
            self.cannon.append(Projectile(self.posX +self.imageWidth * -1 , self.posY))
            self.cannon[len(self.cannon)-1].startShot()
            self.image = self.attackImages[self.imageIndex]
            self.reloadTime = 0 #Reload Time is like a timer for when this works again

        if(self.reloadTime<self.reloadMax):
           self.reloadTime = self.reloadMax
           
        for i in range(0,len(self.cannon)-1):
            self.cannon[i].IsInBounds(screenW,screenH,-10,0)
        self.IsInBounds(screenW,screenH,moveX,moveY)
        
        

    def collide(self,otherRect):
        self.getRect().colliderect(otherRect)
        
    def drawTank(self,screen):
        screen.blit(self.image,(self.posX,self.posY))
        for i in range(0,len(self.cannon)-1):
            self.cannon[i].draw_Projectile(screen)
        #pygame.display.update()
