#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, os, random

class Pieza(pygame.sprite.Sprite):

    def __init__(self, imagen, x,y, pos):
        pygame.sprite.Sprite.__init__(self) 
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.x = x
        self.y = y
        self.posicionCorrecta = self.rect.center

       
       
        