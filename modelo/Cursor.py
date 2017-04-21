#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, os

class Cursor(pygame.Rect):
    
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
        
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()
        
class Mouse(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load(os.path.join("imagenes", "citas", "mouse.png")).convert_alpha()
        self.rect = self.image.get_rect()
        
