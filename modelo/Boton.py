#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, os

class Boton(pygame.sprite.Sprite):
    
    def __init__(self, imagen1, imagen2, x, y):
        self.imagen_normal = imagen1
        self.imagen_seleccion = imagen2
        self.imagen_actual = self.imagen_normal
        self.rect = self.imagen_actual.get_rect()
        self.rect.left, self.rect.top = (x, y)
        
    def update(self, pantalla, cursor):
        
        if cursor.colliderect(self.rect):
            self.imagen_actual = self.imagen_seleccion
        else:
            self.imagen_actual = self.imagen_normal
        
        pantalla.blit(self.imagen_actual, self.rect)
        
    def setCoord(self, x, y):
        self.rect = self.imagen_actual.get_rect()
        self.rect.left, self.rect.top = (x, y)
        
class BotonContinuar(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load(os.path.join("imagenes", "boton_continuar.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (600,630)
        
class BotonLimpiar(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load(os.path.join("imagenes", "citas", "botonLimpiar.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (1100,760)
        
class BotonTerminar(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load(os.path.join("imagenes", "boton_terminar.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (600,630)
        
class BotonReintentar(pygame.sprite.Sprite):


    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load(os.path.join("imagenes", "verdad", "botonReiniciar.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (600,630)
    