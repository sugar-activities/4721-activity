#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, os, tableroCentral, VentanaPersonaje, VentanaTutorial
from control import Servicios
from modelo import Boton, Personaje, MensajeEmergente
from pygame.locals import *


class MenuPrincipal(object):
    
    def __init__(self, cursor, screen, clock, anchoVentana, altoVentana):
        
        self.ancho = anchoVentana
        self.alto = altoVentana
    
        self.dirImagenes = os.path.join("imagenes", "menuPrincipal")
        
        self.cursor = cursor
        self.screen = screen
        self.clock = clock
        
        
        
        imgBtnJugar = Servicios.cargarImagen("boton_jugar.png", self.dirImagenes)
        imgBtnJugarSelec = Servicios.cargarImagen("boton_jugar_selec.png", self.dirImagenes)
        
        imgBtnAprender = Servicios.cargarImagen("boton_aprender.png", self.dirImagenes)
        imgBtnAprenderSelec = Servicios.cargarImagen("boton_aprender_selec.png", self.dirImagenes)
        
        imgBtnSalir = Servicios.cargarImagen("boton_salir.png", self.dirImagenes)
        imgBtnSalirSelec = Servicios.cargarImagen("boton_salir_selec.png", self.dirImagenes)
        
        xBotones = 50
        yInicial = 580
        deltaY = 75
        
        self.btnJugar = Boton.Boton(imgBtnJugar, imgBtnJugarSelec, xBotones, yInicial)
        self.btnAprender = Boton.Boton(imgBtnAprender, imgBtnAprenderSelec, xBotones, yInicial + deltaY)
        self.btnSalir = Boton.Boton(imgBtnSalir, imgBtnSalirSelec, xBotones, yInicial + deltaY + deltaY)
        
        self.personaje = None
        self.tablero = None
        self.tutorial = None
        self.ventPersonaje = None  
        
    def run(self):
        
        fondo = Servicios.cargarImagen("Fondo.jpg", os.path.join("imagenes"), False)
        logo = Servicios.cargarImagen("logo.png", self.dirImagenes)
        
        salir = False
        
        #imgLetrero = Servicios.cargarImagen("Pantalla_Citas.png", self.dirImagenes)
        
        #msj = MensajeEmergente.MensajeInicial(40, "CuentoNoViolencia")
        
        #msj = MensajeEmergente.MensajeGanaste(28, "JuegoNoViolencia")
        
        msj = MensajeEmergente.MensajeInicial(40, "CuentoNoViolencia")
        msj2 = MensajeEmergente.MensajeInicial(40, "CuentoNoViolencia")
        
        while salir == False:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    
                    if self.cursor.colliderect(msj.btn.rect):
                        msj.setVisible(False)
                        
                    if self.cursor.colliderect(msj2.btn.rect):
                        msj2.setVisible(False)
                    
                    if self.cursor.colliderect(self.btnJugar.rect):
                        msj.setVisible(True)
                    
                    if self.cursor.colliderect(self.btnAprender.rect):
                        msj2.setVisible(True)
                    
                    if self.cursor.colliderect(self.btnSalir.rect):
                        salir = True
                        pygame.quit()
                        sys.exit()
                        
            self.clock.tick(60)
            
            self.cursor.update()
            
            self.screen.blit(fondo, (0, 0))
            self.screen.blit(logo, (0, 0))
            
            #===================================================================
            # if emergenteVisible:
            #    msj.setText("Esta es una ventana emergente de prueba. Este es un texto muy largo!")
            #    self.screen.blit(msj.image, (msj.x, msj.y))
            #===================================================================
            
            
               
            self.btnJugar.update(self.screen, self.cursor)
            self.btnAprender.update(self.screen, self.cursor)
            self.btnSalir.update(self.screen, self.cursor)
            
            msj.update(self.screen, self.cursor)
            
            pygame.display.update()
            
        
