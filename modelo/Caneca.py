#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, os
from control import Servicios
class Caneca(pygame.sprite.Sprite):
    
    def __init__(self, x, y, anch, caneca):
        self.x = x 
        self.y = y
        self.ancho = anch
        
        self.x2 = x 
        self.y2 = y
        self.ancho2 = anch
        
        self.xInfo = x 
        self.yInfo = y
        self.anchoInfo = anch
        
        self.caneca = caneca
        self.dirImagenes = os.path.join("imagenes", "rectitud", "canecas")
        
        if caneca==1:
            self.imagenOriginal = Servicios.cargarImagen("caneca_azul.png", self.dirImagenes)
            self.imagenOriginalInfo = Servicios.cargarImagen("caneca_azul_info.png", self.dirImagenes)
        if caneca==2:
            self.imagenOriginal = Servicios.cargarImagen("caneca_blanca.png", self.dirImagenes)
            self.imagenOriginalInfo = Servicios.cargarImagen("caneca_blanca_info.png", self.dirImagenes)
        if caneca==3:
            self.imagenOriginal = Servicios.cargarImagen("caneca_gris.png", self.dirImagenes)
            self.imagenOriginalInfo = Servicios.cargarImagen("caneca_gris_info.png", self.dirImagenes)
            
        self.imagen = self.imagenOriginal
            
        self.alto = self.ancho * self.imagenOriginal.get_height() / self.imagenOriginal.get_width()
        
        self.imagen = pygame.transform.smoothscale(self.imagenOriginal, (self.ancho, self.alto))
        
        self.rect = self.imagen.get_rect()
        self.rect.left, self.rect.top = (self.x, self.y)
        
        
        
        self.imagen2 = self.imagenOriginal
            
        self.alto2 = self.ancho2 * self.imagenOriginal.get_height() / self.imagenOriginal.get_width()
        
        self.imagen2 = pygame.transform.smoothscale(self.imagenOriginal, (self.ancho2, self.alto2))
        
        self.rect2 = self.imagen2.get_rect()
        self.rect2.left, self.rect2.top = (self.x2, self.y2)
        
        
        
        self.imagenInfo = self.imagenOriginalInfo 
          
        self.altoInfo = self.anchoInfo * self.imagenOriginalInfo .get_height() / self.imagenOriginalInfo .get_width()
        
        self.imagenInfo  = pygame.transform.smoothscale(self.imagenOriginalInfo , (self.anchoInfo, self.altoInfo))
        
        self.rectInfo  = self.imagenInfo .get_rect()
        self.rectInfo .left, self.rectInfo .top = (self.xInfo, self.yInfo)
        
    def setAncho(self, ancho):
        self.ancho = ancho
        self.alto = self.ancho * self.imagenOriginal.get_height() / self.imagenOriginal.get_width()
        self.imagen = pygame.transform.smoothscale(self.imagenOriginal, (self.ancho, self.alto))
        
    
    def setAncho2(self, ancho):
        self.ancho2 = ancho
        self.alto2 = self.ancho2 * self.imagenOriginal.get_height() / self.imagenOriginal.get_width()
        self.imagen2 = pygame.transform.smoothscale(self.imagenOriginal, (self.ancho2, self.alto2))
    
    def setAnchoInfo(self, ancho):
        self.anchoInfo = ancho
        self.altoInfo = self.anchoInfo * self.imagenOriginalInfo.get_height() / self.imagenOriginalInfo.get_width()
        self.imagenInfo = pygame.transform.smoothscale(self.imagenOriginalInfo, (self.anchoInfo, self.altoInfo))
        
    def setCoord(self, x, y):
        self.x = x
        self.y = y
        self.rect = self.imagen.get_rect()
        self.rect.left, self.rect.top = (self.x, self.y)
        
    def setCoord2(self, x, y):
        self.x2 = x
        self.y2 = y
        self.rect2 = self.imagen2.get_rect()
        self.rect2.left, self.rect2.top = (self.x2, self.y2)
        
    def setCoordInfo(self, x, y):
        self.xInfo = x
        self.yInfo = y
        self.rectInfo = self.imagenInfo.get_rect()
        self.rectInfo.left, self.rectInfo.top = (self.xInfo, self.yInfo)
            
            