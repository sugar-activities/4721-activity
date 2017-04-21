#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, os, datetime
from control import Servicios, resource
from pygame.locals import *

class Personaje(pygame.sprite.Sprite):
    
    def __init__(self, x_inicial, y_inicial, anch, sex, imagen):
        self.x = x_inicial
        self.y = y_inicial
        self.ancho = anch
        self.sexo = sex
        self.nombre = ""
        self.colegio = ""
        self.edad = ""
        
        self.imagenOriginal = imagen
        
        self.imagen = self.imagenOriginal
        self.alto = self.ancho * self.imagen.get_height() / self.imagen.get_width()
        self.imagen = pygame.transform.smoothscale(self.imagen, (self.ancho, self.alto))
        
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        
        self.rect.left, self.rect.top = (self.x, self.y)
        
        resource.set_images_path(os.path.join("imagenes", "verdad"))
        
        self.imgDer1MOriginal = resource.get_image("Der1.png")
        self.imgDer2MOriginal = resource.get_image("Der2.png")
        self.imgDer3MOriginal = resource.get_image("Der4.png")
            
        self.imgIzq1MOriginal = resource.get_image("Izq1.png")
        self.imgIzq2MOriginal = resource.get_image("Izq2.png")
        self.imgIzq3MOriginal = resource.get_image("Izq4.png")
         
        self.imgArr1MOriginal = resource.get_image("Espalda1.png")
        self.imgArr2MOriginal = resource.get_image("Espalda2.png")
        self.imgArr3MOriginal = resource.get_image("Espalda4.png")
            
        self.imgAbj1MOriginal = resource.get_image("Frente1.png")
        self.imgAbj2MOriginal = resource.get_image("Frente2.png")
        self.imgAbj3MOriginal = resource.get_image("Frente4.png")
        
        self.imgDer1M = pygame.transform.smoothscale(self.imgDer1MOriginal, (self.ancho, self.alto))
        self.imgDer2M = pygame.transform.smoothscale(self.imgDer2MOriginal, (self.ancho, self.alto))
        self.imgDer3M = pygame.transform.smoothscale(self.imgDer3MOriginal, (self.ancho, self.alto))
        self.imgIzq1M = pygame.transform.smoothscale(self.imgIzq1MOriginal, (self.ancho, self.alto))
        self.imgIzq2M = pygame.transform.smoothscale(self.imgIzq2MOriginal, (self.ancho, self.alto))
        self.imgIzq3M = pygame.transform.smoothscale(self.imgIzq3MOriginal, (self.ancho, self.alto))
        self.imgArr1M = pygame.transform.smoothscale(self.imgArr1MOriginal, (self.ancho, self.alto))
        self.imgArr2M = pygame.transform.smoothscale(self.imgArr2MOriginal, (self.ancho, self.alto))
        self.imgArr3M = pygame.transform.smoothscale(self.imgArr3MOriginal, (self.ancho, self.alto))
        self.imgAbj1M = pygame.transform.smoothscale(self.imgAbj1MOriginal, (self.ancho, self.alto))
        self.imgAbj2M = pygame.transform.smoothscale(self.imgAbj2MOriginal, (self.ancho, self.alto))
        self.imgAbj3M = pygame.transform.smoothscale(self.imgAbj3MOriginal, (self.ancho, self.alto))
        
        self.imgDer1FOriginal = resource.get_image("Nina_Camina-09.png")
        self.imgDer2FOriginal = resource.get_image("Nina_Camina-10.png")
        self.imgDer3FOriginal = resource.get_image("Nina_Camina-12.png")
         
        self.imgIzq1FOriginal = resource.get_image("Nina_Camina-05.png")
        self.imgIzq2FOriginal = resource.get_image("Nina_Camina-06.png")
        self.imgIzq3FOriginal = resource.get_image("Nina_Camina-08.png")
           
        self.imgArr1FOriginal = resource.get_image("Nina_Camina-13.png")
        self.imgArr2FOriginal = resource.get_image("Nina_Camina-14.png")
        self.imgArr3FOriginal = resource.get_image("Nina_Camina-16.png")
             
        self.imgAbj1FOriginal = resource.get_image("Nina_Camina-01.png")
        self.imgAbj2FOriginal = resource.get_image("Nina_Camina-02.png")
        self.imgAbj3FOriginal = resource.get_image("Nina_Camina-04.png")
        
        self.imgDer1F = pygame.transform.smoothscale(self.imgDer1FOriginal, (self.ancho, self.alto))
        self.imgDer2F = pygame.transform.smoothscale(self.imgDer2FOriginal, (self.ancho, self.alto))
        self.imgDer3F = pygame.transform.smoothscale(self.imgDer3FOriginal, (self.ancho, self.alto))
        self.imgIzq1F = pygame.transform.smoothscale(self.imgIzq1FOriginal, (self.ancho, self.alto))
        self.imgIzq2F = pygame.transform.smoothscale(self.imgIzq2FOriginal, (self.ancho, self.alto))
        self.imgIzq3F = pygame.transform.smoothscale(self.imgIzq3FOriginal, (self.ancho, self.alto))
        self.imgArr1F = pygame.transform.smoothscale(self.imgArr1FOriginal, (self.ancho, self.alto))
        self.imgArr2F = pygame.transform.smoothscale(self.imgArr2FOriginal, (self.ancho, self.alto))
        self.imgArr3F = pygame.transform.smoothscale(self.imgArr3FOriginal, (self.ancho, self.alto))
        self.imgAbj1F = pygame.transform.smoothscale(self.imgAbj1FOriginal, (self.ancho, self.alto))
        self.imgAbj2F = pygame.transform.smoothscale(self.imgAbj2FOriginal, (self.ancho, self.alto))
        self.imgAbj3F = pygame.transform.smoothscale(self.imgAbj3FOriginal, (self.ancho, self.alto))
        
        if self.sexo == "M":
            self.imgDer1 = self.imgDer1M
            self.imgDer2 = self.imgDer2M
            self.imgDer3 = self.imgDer3M

            self.imgIzq1 = self.imgIzq1M
            self.imgIzq2 = self.imgIzq2M
            self.imgIzq3 = self.imgIzq3M

            self.imgArr1 = self.imgArr1M
            self.imgArr2 = self.imgArr2M
            self.imgArr3 = self.imgArr3M

            self.imgAbj1 = self.imgAbj1M
            self.imgAbj2 = self.imgAbj2M
            self.imgAbj3 = self.imgAbj3M 
        else:
            self.imgDer1 = self.imgDer1F
            self.imgDer2 = self.imgDer2F
            self.imgDer3 = self.imgDer3F

            self.imgIzq1 = self.imgIzq1F
            self.imgIzq2 = self.imgIzq2F
            self.imgIzq3 = self.imgIzq3F

            self.imgArr1 = self.imgArr1F
            self.imgArr2 = self.imgArr2F
            self.imgArr3 = self.imgArr3F

            self.imgAbj1 = self.imgAbj1F
            self.imgAbj2 = self.imgAbj2F
            self.imgAbj3 = self.imgAbj3F
        
    
    def setImagen(self, imagen):
        self.imagenOriginal = imagen
        self.imagen = self.imagenOriginal
        self.alto = self.ancho * self.imagen.get_height() / self.imagen.get_width()
        self.imagen = pygame.transform.smoothscale(self.imagen, (self.ancho, self.alto))
        
        
    
    def setSexo(self, sexo):
        self.sexo = sexo
        if self.sexo == "M":
            self.imgDer1 = self.imgDer1M
            self.imgDer2 = self.imgDer2M
            self.imgDer3 = self.imgDer3M

            self.imgIzq1 = self.imgIzq1M
            self.imgIzq2 = self.imgIzq2M
            self.imgIzq3 = self.imgIzq3M

            self.imgArr1 = self.imgArr1M
            self.imgArr2 = self.imgArr2M
            self.imgArr3 = self.imgArr3M

            self.imgAbj1 = self.imgAbj1M
            self.imgAbj2 = self.imgAbj2M
            self.imgAbj3 = self.imgAbj3M 
        else:
            self.imgDer1 = self.imgDer1F
            self.imgDer2 = self.imgDer2F
            self.imgDer3 = self.imgDer3F

            self.imgIzq1 = self.imgIzq1F
            self.imgIzq2 = self.imgIzq2F
            self.imgIzq3 = self.imgIzq3F

            self.imgArr1 = self.imgArr1F
            self.imgArr2 = self.imgArr2F
            self.imgArr3 = self.imgArr3F

            self.imgAbj1 = self.imgAbj1F
            self.imgAbj2 = self.imgAbj2F
            self.imgAbj3 = self.imgAbj3F
    def setAncho(self, ancho):
        
        self.ancho = ancho
        
        self.imagen = self.imagenOriginal
        self.alto = self.ancho * self.imagen.get_height() / self.imagen.get_width()
        self.imagen = pygame.transform.smoothscale(self.imagen, (self.ancho, self.alto))
        
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        
        self.rect.left, self.rect.top = (self.x, self.y)
        
        self.controlDibujo = 0
        self.auxControlDibujo = 0
        
        if self.sexo == "M":
            self.imgDer1M = pygame.transform.smoothscale(self.imgDer1MOriginal, (self.ancho, self.alto))
            self.imgDer2M = pygame.transform.smoothscale(self.imgDer2MOriginal, (self.ancho, self.alto))
            self.imgDer3M = pygame.transform.smoothscale(self.imgDer3MOriginal, (self.ancho, self.alto))
            self.imgIzq1M = pygame.transform.smoothscale(self.imgIzq1MOriginal, (self.ancho, self.alto))
            self.imgIzq2M = pygame.transform.smoothscale(self.imgIzq2MOriginal, (self.ancho, self.alto))
            self.imgIzq3M = pygame.transform.smoothscale(self.imgIzq3MOriginal, (self.ancho, self.alto))
            self.imgArr1M = pygame.transform.smoothscale(self.imgArr1MOriginal, (self.ancho, self.alto))
            self.imgArr2M = pygame.transform.smoothscale(self.imgArr2MOriginal, (self.ancho, self.alto))
            self.imgArr3M = pygame.transform.smoothscale(self.imgArr3MOriginal, (self.ancho, self.alto))
            self.imgAbj1M = pygame.transform.smoothscale(self.imgAbj1MOriginal, (self.ancho, self.alto))
            self.imgAbj2M = pygame.transform.smoothscale(self.imgAbj2MOriginal, (self.ancho, self.alto))
            self.imgAbj3M = pygame.transform.smoothscale(self.imgAbj3MOriginal, (self.ancho, self.alto))
            
            self.imgDer1 = self.imgDer1M
            self.imgDer2 = self.imgDer2M
            self.imgDer3 = self.imgDer3M

            self.imgIzq1 = self.imgIzq1M
            self.imgIzq2 = self.imgIzq2M
            self.imgIzq3 = self.imgIzq3M

            self.imgArr1 = self.imgArr1M
            self.imgArr2 = self.imgArr2M
            self.imgArr3 = self.imgArr3M

            self.imgAbj1 = self.imgAbj1M
            self.imgAbj2 = self.imgAbj2M
            self.imgAbj3 = self.imgAbj3M 
        else:
            self.imgDer1F = pygame.transform.smoothscale(self.imgDer1FOriginal, (self.ancho, self.alto))
            self.imgDer2F = pygame.transform.smoothscale(self.imgDer2FOriginal, (self.ancho, self.alto))
            self.imgDer3F = pygame.transform.smoothscale(self.imgDer3FOriginal, (self.ancho, self.alto))
            self.imgIzq1F = pygame.transform.smoothscale(self.imgIzq1FOriginal, (self.ancho, self.alto))
            self.imgIzq2F = pygame.transform.smoothscale(self.imgIzq2FOriginal, (self.ancho, self.alto))
            self.imgIzq3F = pygame.transform.smoothscale(self.imgIzq3FOriginal, (self.ancho, self.alto))
            self.imgArr1F = pygame.transform.smoothscale(self.imgArr1FOriginal, (self.ancho, self.alto))
            self.imgArr2F = pygame.transform.smoothscale(self.imgArr2FOriginal, (self.ancho, self.alto))
            self.imgArr3F = pygame.transform.smoothscale(self.imgArr3FOriginal, (self.ancho, self.alto))
            self.imgAbj1F = pygame.transform.smoothscale(self.imgAbj1FOriginal, (self.ancho, self.alto))
            self.imgAbj2F = pygame.transform.smoothscale(self.imgAbj2FOriginal, (self.ancho, self.alto))
            self.imgAbj3F = pygame.transform.smoothscale(self.imgAbj3FOriginal, (self.ancho, self.alto))
            
            self.imgDer1 = self.imgDer1F
            self.imgDer2 = self.imgDer2F
            self.imgDer3 = self.imgDer3F

            self.imgIzq1 = self.imgIzq1F
            self.imgIzq2 = self.imgIzq2F
            self.imgIzq3 = self.imgIzq3F

            self.imgArr1 = self.imgArr1F
            self.imgArr2 = self.imgArr2F
            self.imgArr3 = self.imgArr3F

            self.imgAbj1 = self.imgAbj1F
            self.imgAbj2 = self.imgAbj2F
            self.imgAbj3 = self.imgAbj3F
    
    def setX(self, x):
        self.x = x
        self.rect.left, self.rect.top = (self.x, self.y)
    
    def setY(self, y):
        self.y = y
        self.rect.left, self.rect.top = (self.x, self.y)
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setNombre(self, nombre):
        self.nombre = nombre
        
    def setColegio(self, colegio):
        self.colegio = colegio
        
    def setEdad(self, edad):
        self.edad = edad
    
    def dibujar(self, pantalla):
        self.imagen = self.imagenOriginal
        self.alto = self.ancho * self.imagen.get_height() / self.imagen.get_width()
        self.imagen = pygame.transform.smoothscale(self.imagen, (self.ancho, self.alto))
        pantalla.blit(self.imagen, (self.rect))
    
    def dibujarMov(self, pantalla, direccion):
        
        if direccion == "der":
        
            if self.controlDibujo == 0:
                self.imagen = self.imgDer1
                        
            if self.controlDibujo == 1:
                self.imagen = self.imgDer2
                        
            if self.controlDibujo == 2:
                self.imagen = self.imgDer3
                    
            if self.controlDibujo <= 2:
                self.auxControlDibujo += 1
                if self.auxControlDibujo == 5:
                    self.auxControlDibujo = 0
                    self.controlDibujo += 1
            else:
                self.controlDibujo = 0
        
        elif direccion == "izq":
            if self.controlDibujo == 0:
                self.imagen = self.imgIzq1
                        
            if self.controlDibujo == 1:
                self.imagen = self.imgIzq2
                        
            if self.controlDibujo == 2:
                self.imagen = self.imgIzq3
                    
            if self.controlDibujo <= 2:
                self.auxControlDibujo += 1
                if self.auxControlDibujo == 5:
                    self.auxControlDibujo = 0
                    self.controlDibujo += 1
            else:
                self.controlDibujo = 0
        
        elif direccion == "arriba":
            if self.controlDibujo == 0:
                self.imagen = self.imgArr1
                        
            if self.controlDibujo == 1:
                self.imagen = self.imgArr2
                        
            if self.controlDibujo == 2:
                self.imagen = self.imgArr3
                    
            if self.controlDibujo <= 2:
                self.auxControlDibujo += 1
                if self.auxControlDibujo == 5:
                    self.auxControlDibujo = 0
                    self.controlDibujo += 1
            else:
                self.controlDibujo = 0
        
        elif direccion == "abajo":
            if self.controlDibujo == 0:
                self.imagen = self.imgAbj1
                        
            if self.controlDibujo == 1:
                self.imagen = self.imgAbj2
                        
            if self.controlDibujo == 2:
                self.imagen = self.imgAbj3
                    
            if self.controlDibujo <= 2:
                self.auxControlDibujo += 1
                if self.auxControlDibujo == 5:
                    self.auxControlDibujo = 0
                    self.controlDibujo += 1
            else:
                self.controlDibujo = 0
    
                
        self.rect = self.imagen.get_rect()
        self.rect.left, self.rect.top = (self.x, self.y)
        
        pantalla.blit(self.imagen, (self.rect))

  
class PersonajePacman(pygame.sprite.Sprite):

    def __init__(self, centro, sex):
        pygame.sprite.Sprite.__init__(self) 
        
        self.poderoso = False
        
        """Cuanto me voy a mover"""
        self.x_dist = 1
        self.y_dist = 1
        """que tanto me estoy moviendo"""
        self.xMove = 0
        self.yMove = 0
        
        if sex == "M":
        
            resource.set_images_path(os.path.join("imagenes", "verdad"))
            imgDer1 = resource.get_image("Der1.png")
            imgDer2 = resource.get_image("Der2.png")
            imgDer3 = resource.get_image("Der4.png")
            imgDer1 = pygame.transform.smoothscale(imgDer1, (25, 40))
            imgDer2 = pygame.transform.smoothscale(imgDer2, (25, 40))
            imgDer3 = pygame.transform.smoothscale(imgDer3, (25, 40))
            
            
            
            self.imgDers = [imgDer1, imgDer2, imgDer1, imgDer3]
            
            imgIzq1 = resource.get_image("Izq1.png")
            imgIzq2 = resource.get_image("Izq2.png")
            imgIzq3 = resource.get_image("Izq4.png")
            imgIzq1 = pygame.transform.smoothscale(imgIzq1, (25, 40))
            imgIzq2 = pygame.transform.smoothscale(imgIzq2, (25, 40))
            imgIzq3 = pygame.transform.smoothscale(imgIzq3, (25, 40))
            self.imgIzqs = [imgIzq1, imgIzq2, imgIzq1, imgIzq3]
            
            imgArr1 = resource.get_image("Espalda1.png")
            imgArr2 = resource.get_image("Espalda2.png")
            imgArr3 = resource.get_image("Espalda4.png")
            imgArr1 = pygame.transform.smoothscale(imgArr1, (25, 40))
            imgArr2 = pygame.transform.smoothscale(imgArr2, (25, 40))
            imgArr3 = pygame.transform.smoothscale(imgArr3, (25, 40))
            self.imgArrs = [imgArr1, imgArr2, imgArr1, imgArr3]
            
            imgAbj1 = resource.get_image("Frente1.png")
            imgAbj2 = resource.get_image("Frente2.png")
            imgAbj3 = resource.get_image("Frente4.png")
            imgAbj1 = pygame.transform.smoothscale(imgAbj1, (25, 40))
            imgAbj2 = pygame.transform.smoothscale(imgAbj2, (25, 40))
            imgAbj3 = pygame.transform.smoothscale(imgAbj3, (25, 40))
            self.imgAbjs = [imgAbj1, imgAbj2, imgAbj1, imgAbj3]
            
        else:
            resource.set_images_path(os.path.join("imagenes", "verdad"))
            imgDer1 = resource.get_image("Nina_Camina-09.png")
            imgDer2 = resource.get_image("Nina_Camina-10.png")
            imgDer3 = resource.get_image("Nina_Camina-12.png")
            imgDer1 = pygame.transform.smoothscale(imgDer1, (25, 40))
            imgDer2 = pygame.transform.smoothscale(imgDer2, (25, 40))
            imgDer3 = pygame.transform.smoothscale(imgDer3, (25, 40))
            
            
            
            self.imgDers = [imgDer1, imgDer2, imgDer1, imgDer3]
            
            imgIzq1 = resource.get_image("Nina_Camina-05.png")
            imgIzq2 = resource.get_image("Nina_Camina-06.png")
            imgIzq3 = resource.get_image("Nina_Camina-08.png")
            imgIzq1 = pygame.transform.smoothscale(imgIzq1, (25, 40))
            imgIzq2 = pygame.transform.smoothscale(imgIzq2, (25, 40))
            imgIzq3 = pygame.transform.smoothscale(imgIzq3, (25, 40))
            self.imgIzqs = [imgIzq1, imgIzq2, imgIzq1, imgIzq3]
            
            imgArr1 = resource.get_image("Nina_Camina-13.png")
            imgArr2 = resource.get_image("Nina_Camina-14.png")
            imgArr3 = resource.get_image("Nina_Camina-16.png")
            imgArr1 = pygame.transform.smoothscale(imgArr1, (25, 40))
            imgArr2 = pygame.transform.smoothscale(imgArr2, (25, 40))
            imgArr3 = pygame.transform.smoothscale(imgArr3, (25, 40))
            self.imgArrs = [imgArr1, imgArr2, imgArr1, imgArr3]
            
            imgAbj1 = resource.get_image("Nina_Camina-01.png")
            imgAbj2 = resource.get_image("Nina_Camina-02.png")
            imgAbj3 = resource.get_image("Nina_Camina-04.png")
            imgAbj1 = pygame.transform.smoothscale(imgAbj1, (25, 40))
            imgAbj2 = pygame.transform.smoothscale(imgAbj2, (25, 40))
            imgAbj3 = pygame.transform.smoothscale(imgAbj3, (25, 40))
            self.imgAbjs = [imgAbj1, imgAbj2, imgAbj1, imgAbj3]
        
        self.image = imgAbj1
        self.rect = self.image.get_rect()
        self.rect.center = centro
        
        self.anim_pacmanCurrent = self.imgAbjs
        self.animFrame = 0;
        
        self.starttime = datetime.datetime.now()
            
    def MoveKeyDown(self, key):
        """This function sets the xMove or yMove variables that will
        then move the snake when update() function is called.  The
        xMove and yMove values will be returned to normal when this 
        keys MoveKeyUp function is called."""
        
        if (key == K_RIGHT):
            self.xMove = 4
            self.yMove = 0
        elif (key == K_LEFT):
            self.xMove = -4
            self.yMove = 0
        elif (key == K_UP):
            self.yMove = -4
            self.xMove = 0
        elif (key == K_DOWN):
            self.yMove = 4
            self.xMove = 0
    
    def MoveKeyUp(self, key):
        """This function resets the xMove or yMove variables that will
        then move the snake when update() function is called.  The
        xMove and yMove values will be returned to normal when this 
        keys MoveKeyUp function is called."""
        
        if (key == K_RIGHT):
            self.xMove = 0
        elif (key == K_LEFT):
            self.xMove = 0
        elif (key == K_UP):
            self.yMove = 0
        elif (key == K_DOWN):
            self.yMove = 0
            
    def update(self, block_group):
        
        endtime = datetime.datetime.now()
        
        if(endtime - self.starttime).total_seconds() >= 0.1:
            if self.xMove > 0:
                self.anim_pacmanCurrent = self.imgDers
            elif self.xMove < 0:
                self.anim_pacmanCurrent = self.imgIzqs
            elif self.yMove > 0:
                self.anim_pacmanCurrent = self.imgAbjs
            elif self.yMove < 0:
                self.anim_pacmanCurrent = self.imgArrs
                
            self.image = self.anim_pacmanCurrent[self.animFrame]
                
            if not self.yMove == 0 or not self.xMove == 0:
                    # only Move mouth when pacman is moving
                self.animFrame += 1 
                
            if self.animFrame == 4:
                    # wrap to beginning
                self.animFrame = 0
            self.starttime = datetime.datetime.now()
             
        
        

        self.rect.move_ip(self.xMove, self.yMove)
        """IF we hit a block, don't move - reverse the movement"""
        if pygame.sprite.spritecollide(self, block_group, False):
            self.rect.move_ip(-self.xMove, -self.yMove) 
        
                  
        

