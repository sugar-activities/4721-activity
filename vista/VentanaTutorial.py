#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, os
from control import Servicios
from modelo import Boton
from pygame.locals import *


class VentanaTutorial(object):
    
    def __init__(self, ventPadre, cursor, screen, clock, anchoVentana, altoVentana):
        
        self.dirImagenes = os.path.join("imagenes", "tutorial")
        
        self.menu = ventPadre
        
        self.ancho = anchoVentana
        self.alto = altoVentana
        
        self.cursor = cursor
        self.screen = screen
        self.clock = clock
        
        #imagen1 = Servicios.cargarImagen(os.path.join("tuto1.png"), self.dirImagenes)
        #imagen2 = Servicios.cargarImagen(os.path.join("tuto2.png"), self.dirImagenes)
        #imagen3 = Servicios.cargarImagen(os.path.join("tuto3.png"), self.dirImagenes)
        #imagen4 = Servicios.cargarImagen(os.path.join("tuto4.png"), self.dirImagenes)
        #imagen5 = Servicios.cargarImagen(os.path.join("tuto5.png"), self.dirImagenes)
        imagen6 = Servicios.cargarImagen(os.path.join("tuto6.png"), self.dirImagenes)
        
        self.listaImagenes = [imagen6]
        
        self.imagenActual = self.listaImagenes[0]
        
        imgBtnRegresar = Servicios.cargarImagen("boton_regresar.png", "imagenes")
        imgBtnRegresarSelec = Servicios.cargarImagen("boton_regresar_selec.png", "imagenes")
        self.btnRegresar = Boton.Boton(imgBtnRegresar, imgBtnRegresarSelec, (self.ancho - 214 - 10), 10)
        
        imgBtnAnterior = Servicios.cargarImagen("boton_anterior.png", self.dirImagenes)
        imgBtnAnteriorSelec = Servicios.cargarImagen("boton_anterior_selec.png", self.dirImagenes)
        self.btnAnterior = Boton.Boton(imgBtnAnterior, imgBtnAnteriorSelec, 500, 700)
        
        imgBtnSiguiente = Servicios.cargarImagen("boton_siguiente.png", self.dirImagenes)
        imgBtnSiguienteSelec = Servicios.cargarImagen("boton_siguiente_selec.png", self.dirImagenes)
        self.btnSiguiente = Boton.Boton(imgBtnSiguiente, imgBtnSiguienteSelec, 600, 700)

   
    def run(self):
        
        fondo = Servicios.cargarImagen("Fondo.jpg", os.path.join("imagenes"), False)
        
        contador = 0
        termino = False
        
        while termino == False:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.cursor.colliderect(self.btnRegresar.rect):
                        self.menu.run()
                    
                    if self.cursor.colliderect(self.btnAnterior.rect):
                        if contador > 0:
                            contador -= 1
                    
                    if self.cursor.colliderect(self.btnSiguiente.rect):
                        if contador < len(self.listaImagenes) - 1:
                            contador += 1
                        else:
                            termino = True
                            self.menu.ventPersonaje.run()
                            
                        
        
            self.clock.tick(60)
            
            self.cursor.update()
            
            self.screen.blit(fondo, (0, 0))
            
            self.screen.blit(self.listaImagenes[contador], (0, 0))
               
            self.btnRegresar.update(self.screen, self.cursor)
            self.btnAnterior.update(self.screen, self.cursor)
            self.btnSiguiente.update(self.screen, self.cursor)
            
            pygame.display.update()
