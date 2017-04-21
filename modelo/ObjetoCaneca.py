#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, os
from control import Servicios
class ObjetoCaneca(pygame.sprite.Sprite):
    
    def __init__(self, x, y, anch, caneca, obj):
        self.x = x
        self.y = y
        self.ancho = anch
        self.caneca = caneca
        self.objeto = obj
        self.nombre = ""
        
        if self.caneca == 1:
            self.dirImagenes = os.path.join("imagenes", "rectitud", "objetos", "CanecaAzul")
            if self.objeto == 1:
                self.nombre = "Balde plastico"
            if self.objeto == 2:
                self.nombre = "Bolsa plastica"
            if self.objeto == 3:
                self.ancho = self.ancho / 2
                self.nombre = "Botella plastica"
            if self.objeto == 4:
                self.nombre = "Vaso plastico"
        if self.caneca == 2:
            self.dirImagenes = os.path.join("imagenes", "rectitud", "objetos", "CanecaBlanca")
    
            if self.objeto == 1:
                self.ancho = self.ancho / 2
                self.nombre = "Botella de vidrio"
            if self.objeto == 2:
                self.nombre = "Lata de sardinas"
            if self.objeto == 3:
                self.ancho = self.ancho / 2
                self.nombre = "Vaso de vidrio"
            if self.objeto == 4:
                self.nombre = "Vidrio roto"
        if self.caneca == 3:
            self.dirImagenes = os.path.join("imagenes", "rectitud", "objetos", "CanecaGris")
            if self.objeto == 1:
                self.nombre = "Caja de carton"
            if self.objeto == 2:
                self.nombre = "Papel"
            if self.objeto == 3:
                self.nombre = "Periodico"
            if self.objeto == 4:
                self.nombre = "Rollo de carton"
        
        if self.objeto == 1:
            self.imagenOriginal = Servicios.cargarImagen("objeto1.png", self.dirImagenes)
            
        if self.objeto == 2:
            self.imagenOriginal = Servicios.cargarImagen("objeto2.png", self.dirImagenes)
            
        if self.objeto == 3:
            self.imagenOriginal = Servicios.cargarImagen("objeto3.png", self.dirImagenes)
            
        if self.objeto == 4:
            self.imagenOriginal = Servicios.cargarImagen("objeto4.png", self.dirImagenes)
            
        self.imagen = self.imagenOriginal
         
         
            
        self.alto = self.ancho * self.imagenOriginal.get_height() / self.imagenOriginal.get_width()
        
        self.imagen = pygame.transform.smoothscale(self.imagenOriginal, (self.ancho, self.alto))
        
        self.rect = self.imagen.get_rect()
        self.rect.left, self.rect.top = (self.x, self.y)
        
    def setAncho(self, ancho):
        self.ancho = ancho
        
        if self.caneca == 1:
            if self.objeto == 3:
                self.ancho = self.ancho / 2
        if self.caneca == 2:
            if self.objeto == 1 or self.objeto == 3:
                self.ancho = self.ancho / 2
        
        self.alto = self.ancho * self.imagenOriginal.get_height() / self.imagenOriginal.get_width()
        self.imagen = pygame.transform.smoothscale(self.imagenOriginal, (self.ancho, self.alto))
        
    def setCoord(self, x, y):
        self.x = x
        self.y = y
        self.rect = self.imagen.get_rect()
        self.rect.left, self.rect.top = (self.x, self.y)
        
