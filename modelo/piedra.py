#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

class Piedra(pygame.sprite.Sprite):
     
    # Constructor. Pass in the color of the block, 
    # and its x and y position
    def __init__(self,imagenes,x,y,letra,numero):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self) 
        
        #imagenes
        self.imagenes = imagenes
        self.letra = letra
        self.location = x-10,y-25
        self.numero = numero
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = self.imagenes[0]
        self.imagen = 0
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values 
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.center = x,y
        
    def update(self):
        
        if self.imagen == 0:
            self.image = self.imagenes[1]
            self.imagen = 1
        elif self.imagen == 2:
            self.image = self.imagenes[1]
            self.imagen = 1
        else:
            self.image = self.imagenes[0]
            self.imagen = 0
            
    def ayuda(self):
        
        self.image = self.imagenes[2]
        self.imagen = 2
        