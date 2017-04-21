#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

class Planta(pygame.sprite.Sprite):
     
    # Constructor. Pass in the color of the block, 
    # and its x and y position
    def __init__(self,imagen):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self) 
        
        #imagenes
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = imagen
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values 
        # of rect.x and rect.y
        self.rect = self.image.get_rect()