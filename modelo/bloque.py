#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

class Bloque(pygame.sprite.Sprite):

    def __init__(self,imagen, centro):
        pygame.sprite.Sprite.__init__(self) 
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.center = centro