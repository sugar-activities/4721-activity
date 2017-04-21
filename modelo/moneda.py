#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, os, datetime
from control import resource

class Moneda(pygame.sprite.Sprite):

    def __init__(self,imagen, centro, interseccion, poderosa):
        pygame.sprite.Sprite.__init__(self) 
        self.image = imagen
        
        self.comida = False
        resource.set_images_path(os.path.join("imagenes", "verdad"))
                                 
        self.image2 = resource.get_image("moneda2.png")
        self.rect = self.image.get_rect()
        self.rect.center = centro
        self.interseccion = interseccion
        self.poderosa = poderosa
        self.startTime = None
        
        if poderosa:
            self.image = resource.get_image("StarBig_On.png")
            self.image3 = self.image
            self.rect = self.image.get_rect()
            self.rect.center = centro
            
    
    def update(self):
        if self.poderosa and self.comida:
            endtime = datetime.datetime.now()
            
            if (endtime-self.startTime).total_seconds()>10:
                self.comida = False
                self.image = self.image3