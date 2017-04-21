#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, os, random, datetime

class Monstruo2(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load(os.path.join("imagenes", "verdad", "monstruos_-01B.png")).convert_alpha()
        self.image2 = pygame.image.load(os.path.join("imagenes", "verdad", "monstruos_-02B.png")).convert_alpha()
        self.image3 = pygame.image.load(os.path.join("imagenes", "verdad", "monstruos_-03B.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [(13*40+20)+172.8,(6*40+20)+37.3]
        
        self.direction = random.randint(1,4)
        self.dist = 4
        
        self.animFrame = 0;
        
        self.anim_Current = [self.image, self.image2, self.image3]
        
        self.arriba = True
        
        self.starttime = datetime.datetime.now()
        
        
    def reincio(self):
        self.rect.center = [(13*40+20)+172.8,(6*40+20)+37.3]
        self.direction = random.randint(1,4)
        
    def update(self,bloques,monedas):
       
        
        endtime = datetime.datetime.now()
        
        if(endtime - self.starttime).total_seconds() >= 0.2:
            
            self.image = self.anim_Current[self.animFrame]
            
            if self.arriba:
                self.animFrame += 1
            else:
                self.animFrame-=1 
            
            if self.animFrame == 2:
                # wrap to beginning
                self.arriba = False
            elif self.animFrame == 0:
                self.arriba = True
            self.starttime = datetime.datetime.now()
        
        xMove,yMove = 0,0
        
        if self.direction==1:
            xMove = -self.dist
        elif self.direction==2:
            yMove = -self.dist
        elif self.direction==3:
            xMove = self.dist
        elif self.direction==4:
            yMove = self.dist
        
        self.rect.move_ip(xMove,yMove) #Move the Rect
        
        
        lstCols = pygame.sprite.spritecollide(self, monedas, False)

        for m in lstCols:
            if m.interseccion and m.rect.center == self.rect.center:
                
                if(self.direction == 1):
                    numbers = [1,2,4]
                    self.direction = random.choice(numbers)
                elif(self.direction == 2):
                    numbers = [1,2,3]
                    self.direction = random.choice(numbers)
                elif(self.direction == 3):
                    numbers = [2,3,4]
                    self.direction = random.choice(numbers)
                elif(self.direction == 4):
                    numbers = [1,3,4]
                    self.direction = random.choice(numbers)
        
                #self.rect.move_ip(xMove,yMove) #Move the Rect
        
        
        if pygame.sprite.spritecollideany(self, bloques):

            self.rect.move_ip(-xMove,-yMove)

            if(self.direction == 1):
                numbers = [1,2,4]
                self.direction = random.choice(numbers)
            elif(self.direction == 2):
                numbers = [1,2,3]
                self.direction = random.choice(numbers)
            elif(self.direction == 3):
                numbers = [2,3,4]
                self.direction = random.choice(numbers)
            elif(self.direction == 4):
                numbers = [1,3,4]
                self.direction = random.choice(numbers)
                
                