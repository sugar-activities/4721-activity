#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, os
from control import Servicios

class Monstruo(pygame.sprite.Sprite):
    
    def __init__(self, x, y, ancho, tipo):
        
        self.dirImagenes = os.path.join("imagenes", "amor", "monstruossucios")
        self.tipo = tipo
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alfa = 0
        self.auxAlfa = 0
        self.imagen1 = Servicios.cargarImagen("monstruo1.png", self.dirImagenes)
        self.alto = self.ancho * self.imagen1.get_height() / self.imagen1.get_width()
        self.vivo = True
        self.controlDibujo = 0
        self.auxControlDibujo = 0
        
        if self.tipo == 1:
            self.imagen1 = Servicios.cargarImagen("monstruo1.png", self.dirImagenes)
            self.imagen2 = Servicios.cargarImagen("monstruo1B.png", self.dirImagenes)
            self.imagen3 = Servicios.cargarImagen("monstruo1C.png", self.dirImagenes)
            self.imagen4 = Servicios.cargarImagen("monstruo1D.png", self.dirImagenes)
            self.imagen5 = Servicios.cargarImagen("monstruo1E.png", self.dirImagenes)
            self.imagen6 = Servicios.cargarImagen("monstruo1F.png", self.dirImagenes)

        if self.tipo == 2:
            self.imagen1 = Servicios.cargarImagen("monstruo2.png", self.dirImagenes)
            self.imagen2 = Servicios.cargarImagen("monstruo2B.png", self.dirImagenes)
            self.imagen3 = Servicios.cargarImagen("monstruo2C.png", self.dirImagenes)
            self.imagen4 = Servicios.cargarImagen("monstruo2D.png", self.dirImagenes)
            self.imagen5 = Servicios.cargarImagen("monstruo2E.png", self.dirImagenes)
            self.imagen6 = Servicios.cargarImagen("monstruo2F.png", self.dirImagenes)


        if self.tipo == 3:
            self.imagen1 = Servicios.cargarImagen("monstruo3.png", self.dirImagenes)
            self.imagen2 = Servicios.cargarImagen("monstruo3B.png", self.dirImagenes)
            self.imagen3 = Servicios.cargarImagen("monstruo3C.png", self.dirImagenes)
            self.imagen4 = Servicios.cargarImagen("monstruo3D.png", self.dirImagenes)
            self.imagen5 = Servicios.cargarImagen("monstruo3E.png", self.dirImagenes)
            self.imagen6 = Servicios.cargarImagen("monstruo3F.png", self.dirImagenes)

        
        
        self.imagen_actual = self.imagen1
        self.rect = self.imagen_actual.get_rect()
        self.rect.left, self.rect.top = (self.x, self.y)
        
    def convertir(self):
        self.vivo = False
        #=======================================================================
        # self.imagen_actual = self.imagenCorazon
        # self.rect = self.imagen_actual.get_rect()
        # self.rect.left, self.rect.top = (self.x, self.y)
        #=======================================================================
    
    def dibujar(self, pantalla, objetivo, velocidad):
        
        if self.y > -100:
            
            if self.vivo == True:
                
                
                '''        
                if self.controlDibujo == 0:
                    self.imagen_actual = self.imagen1
                    
                if self.controlDibujo == 1:
                    self.imagen_actual = self.imagen2
                    
                if self.controlDibujo == 2:
                    self.imagen_actual = self.imagen3
                    
                if self.controlDibujo == 3:
                    self.imagen_actual = self.imagen2
                
                if self.controlDibujo <= 3:
                    self.auxControlDibujo += 1
                    if self.auxControlDibujo == 5:
                        self.auxControlDibujo = 0
                        self.controlDibujo += 1
                        if self.controlDibujo > 3:
                            self.controlDibujo = 0
                '''    
                        
                if(objetivo.x > self.x):
                    self.x += velocidad
                else:
                    self.x -= velocidad
                    # self.x=objetivo.x
                    
                if(objetivo.y > self.y):
                    self.y += velocidad
                else:
                    self.y -= velocidad
                    
            else:
                
                if self.controlDibujo == 0:
                    self.imagen_actual = self.imagen2
                    
                if self.controlDibujo == 1:
                    self.imagen_actual = self.imagen3
                    
                if self.controlDibujo == 2:
                    self.imagen_actual = self.imagen4
                    
                if self.controlDibujo == 3:
                    self.imagen_actual = self.imagen5
                    
                if self.controlDibujo == 4:
                    self.imagen_actual = self.imagen6
                
                if self.controlDibujo <= 4:
                    self.auxControlDibujo += 1
                    if self.auxControlDibujo == 5:
                        self.auxControlDibujo = 0
                        self.controlDibujo += 1
                
                self.y -= velocidad
            
            self.rect = self.imagen_actual.get_rect()
            self.rect.left, self.rect.top = (self.x, self.y)
             
            pantalla.blit(self.imagen_actual, (self.rect))
            
           
        
    #===========================================================================
    # def setAncho(self, ancho):
    #    self.ancho = ancho
    #    self.imagenAlfa0 = Servicios.cargarImagen("monstruo1_0.png", self.dirImagenes)
    #    self.alto = self.ancho * self.imagenAlfa0.get_height() / self.imagenAlfa0.get_width()
    #    
    #    if self.tipo == 1:
    #        self.imagenAlfa0 = Servicios.cargarImagen("monstruo1_0.png", self.dirImagenes)
    #        self.imagenAlfa0 = pygame.transform.smoothscale(self.imagenAlfa0, (self.ancho, self.alto))
    #        self.imagenAlfa1 = Servicios.cargarImagen("monstruo1_1.png", self.dirImagenes)
    #        self.imagenAlfa1 = pygame.transform.smoothscale(self.imagenAlfa1, (self.ancho, self.alto))
    #        self.imagenAlfa2 = Servicios.cargarImagen("monstruo1_2.png", self.dirImagenes)
    #        self.imagenAlfa2 = pygame.transform.smoothscale(self.imagenAlfa2, (self.ancho, self.alto))
    #        self.imagenAlfa3 = Servicios.cargarImagen("monstruo1_3.png", self.dirImagenes)
    #        self.imagenAlfa3 = pygame.transform.smoothscale(self.imagenAlfa3, (self.ancho, self.alto))
    #        self.imagenAlfa4 = Servicios.cargarImagen("monstruo1_4.png", self.dirImagenes)
    #        self.imagenAlfa4 = pygame.transform.smoothscale(self.imagenAlfa4, (self.ancho, self.alto))
    #        self.imagenAlfa5 = Servicios.cargarImagen("monstruo1_5.png", self.dirImagenes)
    #        self.imagenAlfa5 = pygame.transform.smoothscale(self.imagenAlfa5, (self.ancho, self.alto))
    #        self.imagenAlfa6 = Servicios.cargarImagen("monstruo1_6.png", self.dirImagenes)
    #        self.imagenAlfa6 = pygame.transform.smoothscale(self.imagenAlfa6, (self.ancho, self.alto))
    #        self.imagenAlfa7 = Servicios.cargarImagen("monstruo1_7.png", self.dirImagenes)
    #        self.imagenAlfa7 = pygame.transform.smoothscale(self.imagenAlfa7, (self.ancho, self.alto))
    #        self.imagenAlfa8 = Servicios.cargarImagen("monstruo1_8.png", self.dirImagenes)
    #        self.imagenAlfa8 = pygame.transform.smoothscale(self.imagenAlfa8, (self.ancho, self.alto))
    #        self.imagenAlfa9 = Servicios.cargarImagen("monstruo1_9.png", self.dirImagenes)
    #        self.imagenAlfa9 = pygame.transform.smoothscale(self.imagenAlfa9, (self.ancho, self.alto))
    #    if self.tipo == 2:
    #        self.imagenAlfa0 = Servicios.cargarImagen("monstruo2_0.png", self.dirImagenes)
    #        self.imagenAlfa0 = pygame.transform.smoothscale(self.imagenAlfa0, (self.ancho, self.alto))
    #        self.imagenAlfa1 = Servicios.cargarImagen("monstruo2_1.png", self.dirImagenes)
    #        self.imagenAlfa1 = pygame.transform.smoothscale(self.imagenAlfa1, (self.ancho, self.alto))
    #        self.imagenAlfa2 = Servicios.cargarImagen("monstruo2_2.png", self.dirImagenes)
    #        self.imagenAlfa2 = pygame.transform.smoothscale(self.imagenAlfa2, (self.ancho, self.alto))
    #        self.imagenAlfa3 = Servicios.cargarImagen("monstruo2_3.png", self.dirImagenes)
    #        self.imagenAlfa3 = pygame.transform.smoothscale(self.imagenAlfa3, (self.ancho, self.alto))
    #        self.imagenAlfa4 = Servicios.cargarImagen("monstruo2_4.png", self.dirImagenes)
    #        self.imagenAlfa4 = pygame.transform.smoothscale(self.imagenAlfa4, (self.ancho, self.alto))
    #        self.imagenAlfa5 = Servicios.cargarImagen("monstruo2_5.png", self.dirImagenes)
    #        self.imagenAlfa5 = pygame.transform.smoothscale(self.imagenAlfa5, (self.ancho, self.alto))
    #        self.imagenAlfa6 = Servicios.cargarImagen("monstruo2_6.png", self.dirImagenes)
    #        self.imagenAlfa6 = pygame.transform.smoothscale(self.imagenAlfa6, (self.ancho, self.alto))
    #        self.imagenAlfa7 = Servicios.cargarImagen("monstruo2_7.png", self.dirImagenes)
    #        self.imagenAlfa7 = pygame.transform.smoothscale(self.imagenAlfa7, (self.ancho, self.alto))
    #        self.imagenAlfa8 = Servicios.cargarImagen("monstruo2_8.png", self.dirImagenes)
    #        self.imagenAlfa8 = pygame.transform.smoothscale(self.imagenAlfa8, (self.ancho, self.alto))
    #        self.imagenAlfa9 = Servicios.cargarImagen("monstruo2_9.png", self.dirImagenes)
    #        self.imagenAlfa9 = pygame.transform.smoothscale(self.imagenAlfa9, (self.ancho, self.alto))
    #    if self.tipo == 3:
    #        self.imagenAlfa0 = Servicios.cargarImagen("monstruo3_0.png", self.dirImagenes)
    #        self.imagenAlfa0 = pygame.transform.smoothscale(self.imagenAlfa0, (self.ancho, self.alto))
    #        self.imagenAlfa1 = Servicios.cargarImagen("monstruo3_1.png", self.dirImagenes)
    #        self.imagenAlfa1 = pygame.transform.smoothscale(self.imagenAlfa1, (self.ancho, self.alto))
    #        self.imagenAlfa2 = Servicios.cargarImagen("monstruo3_2.png", self.dirImagenes)
    #        self.imagenAlfa2 = pygame.transform.smoothscale(self.imagenAlfa2, (self.ancho, self.alto))
    #        self.imagenAlfa3 = Servicios.cargarImagen("monstruo3_3.png", self.dirImagenes)
    #        self.imagenAlfa3 = pygame.transform.smoothscale(self.imagenAlfa3, (self.ancho, self.alto))
    #        self.imagenAlfa4 = Servicios.cargarImagen("monstruo3_4.png", self.dirImagenes)
    #        self.imagenAlfa4 = pygame.transform.smoothscale(self.imagenAlfa4, (self.ancho, self.alto))
    #        self.imagenAlfa5 = Servicios.cargarImagen("monstruo3_5.png", self.dirImagenes)
    #        self.imagenAlfa5 = pygame.transform.smoothscale(self.imagenAlfa5, (self.ancho, self.alto))
    #        self.imagenAlfa6 = Servicios.cargarImagen("monstruo3_6.png", self.dirImagenes)
    #        self.imagenAlfa6 = pygame.transform.smoothscale(self.imagenAlfa6, (self.ancho, self.alto))
    #        self.imagenAlfa7 = Servicios.cargarImagen("monstruo3_7.png", self.dirImagenes)
    #        self.imagenAlfa7 = pygame.transform.smoothscale(self.imagenAlfa7, (self.ancho, self.alto))
    #        self.imagenAlfa8 = Servicios.cargarImagen("monstruo3_8.png", self.dirImagenes)
    #        self.imagenAlfa8 = pygame.transform.smoothscale(self.imagenAlfa8, (self.ancho, self.alto))
    #        self.imagenAlfa9 = Servicios.cargarImagen("monstruo3_9.png", self.dirImagenes)
    #        self.imagenAlfa9 = pygame.transform.smoothscale(self.imagenAlfa9, (self.ancho, self.alto))
    #    
    # 
    #===========================================================================
