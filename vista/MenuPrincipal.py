#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, os, tableroCentral, VentanaPersonaje, VentanaTutorial
from control import Servicios, resource
from modelo import Boton, Personaje
from pygame.locals import *


class MenuPrincipal(object):
    
    def __init__(self, cursor, screen, clock, anchoVentana, altoVentana):
        
        self.ancho = anchoVentana
        self.alto = altoVentana
        
        resource.set_sounds_path(os.path.join("audios"))
        self.musicaMenu = resource.get_sound("noViolencia_instrum.ogg")
        #self.musicaMenu = Servicios.cargarSonido("noViolencia_instrum.ogg", os.path.join("audios"))
        #self.musicaJuego = Servicios.cargarSonido("musica_juego.ogg", os.path.join("audios"))
    
        self.dirImagenes = os.path.join("imagenes", "menuPrincipal")
        
        self.cursor = cursor
        self.screen = screen
        self.clock = clock
        
        imgBtnJugar = Servicios.cargarImagen("boton_jugar.png", self.dirImagenes)
        imgBtnJugarSelec = Servicios.cargarImagen("boton_jugar_selec.png", self.dirImagenes)
        
        #imgBtnAprender = Servicios.cargarImagen("boton_aprender.png", self.dirImagenes)
        #imgBtnAprenderSelec = Servicios.cargarImagen("boton_aprender_selec.png", self.dirImagenes)
        
        imgBtnSalir = Servicios.cargarImagen("boton_salir.png", self.dirImagenes)
        imgBtnSalirSelec = Servicios.cargarImagen("boton_salir_selec.png", self.dirImagenes)
        
        xBotones = 50
        yInicial = 600
        deltaY = 75
        
        self.btnJugar = Boton.Boton(imgBtnJugar, imgBtnJugarSelec, xBotones, yInicial)
        #self.btnAprender = Boton.Boton(imgBtnAprender, imgBtnAprenderSelec, xBotones, yInicial + deltaY)
        self.btnSalir = Boton.Boton(imgBtnSalir, imgBtnSalirSelec, xBotones, yInicial + deltaY)
        
        self.mostrarCreditos = True
        
        self.personaje = None
        self.tablero = None
        self.tutorial = None
        self.ventPersonaje = None  
        
    def run(self):
        
        resource.set_images_path(os.path.join("imagenes"))
        
        if self.mostrarCreditos:
            creditos = resource.get_image("Creditos.jpg", False)
            self.mostrarCreditos = False
            self.screen.blit(creditos, (0, 0))
            pygame.display.update()
        
        fondo = resource.get_image("Fondo.jpg", False)
        logo = Servicios.cargarImagen("logo.png", self.dirImagenes)
        
        if self.personaje is None:  
            imagenPersonaje = Servicios.cargarImagen("Frente1.png", os.path.join("imagenes", "verdad"))
            self.personaje = Personaje.Personaje(5, 40, 175, "M", imagenPersonaje)
            print "entro personaje"
        
        if self.tablero is None:
            self.tablero = tableroCentral.tableroCentral(self, self.cursor, self.screen, self.clock, self.ancho, self.alto)
            print "entro tablero"
            
        if self.tutorial is None:
            self.tutorial = VentanaTutorial.VentanaTutorial(self, self.cursor, self.screen, self.clock, self.ancho, self.alto)
            print "entro tutorial"
            
        if self.ventPersonaje is None:
            self.ventPersonaje = VentanaPersonaje.VentanaPersonaje(self, self.cursor, self.screen, self.clock, self.ancho, self.alto)  
            print "entro ventPersonaje"
            self.musicaMenu.play(-1) #reproducir la musica solo la primera vez que se corre
        
        #=======================================================================
        # resource.set_images_path(os.path.join("imagenes"))
        # fondo = resource.get_image("Fondo.jpg", False)
        # #fondo = Servicios.cargarImagen("Fondo.jpg", os.path.join("imagenes"), False)
        # logo = Servicios.cargarImagen("logo.png", self.dirImagenes)
        #=======================================================================
        
        salir = False
        
        while salir == False:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.cursor.colliderect(self.btnJugar.rect):
                        salir = True
                        self.ventPersonaje.run()
                    
                    #if self.cursor.colliderect(self.btnAprender.rect):
                        #salir = True
                        #self.tutorial.run()
                    
                    if self.cursor.colliderect(self.btnSalir.rect):
                        salir = True
                        pygame.quit()
                        sys.exit()
                        
            self.clock.tick(60)
            
            self.cursor.update()
            
            self.screen.blit(fondo, (0, 0))
            self.screen.blit(logo, (0, 0))
               
            self.btnJugar.update(self.screen, self.cursor)
            #self.btnAprender.update(self.screen, self.cursor)
            self.btnSalir.update(self.screen, self.cursor)
            
            pygame.display.update()
            
    
    def setPersonaje(self, personaje, imagen):
        
        self.personaje = personaje
        self.personaje.imagenOriginal = imagen
        