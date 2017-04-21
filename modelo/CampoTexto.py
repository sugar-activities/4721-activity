#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

class CampoTexto(pygame.sprite.Sprite):
    
    def __init__(self, x, y, ancho, alto, tamLetra):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.tamLetra = tamLetra
        
        self.initFont()
        self.initImage()
        self.initGroup()


    def initFont(self):
        pygame.font.init()
        self.font = pygame.font.Font(None, self.tamLetra)  # tamaño de la fuente

    def initImage(self):
        self.image = pygame.Surface((self.ancho, self.alto))  # tamaño del campo de texto
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.top = 0 ; self.rect.left = 0
        self.rect2 = self.image.get_rect()
        self.rect2.top = self.y ; self.rect2.left = self.x

    def setText(self, text):
        # tmp = pygame.display.get_surface()
        self.initImage()
        x_pos = self.rect.left + 5
        y_pos = self.rect.top + 5

        for t in text:
            x = self.font.render(t, False, (0, 0, 0))
            self.image.blit(x, (x_pos, y_pos))
            x_pos += self.tamLetra * 0.55  # espaciado entre letras

            if (x_pos > self.image.get_width() - 5):
                x_pos = self.rect.left + 5
                y_pos += self.tamLetra * 0.55  # espaciado entre lineas

    def initGroup(self):
        self.group = pygame.sprite.GroupSingle()
        self.group.add(self)
