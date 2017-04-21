#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, os, sys
from modelo import Boton, CampoTexto, Cursor
from control import Servicios
from pygame.locals import *

class VentanaPersonaje(object):
    
    def __init__(self, ventPadre, cursor, screen, clock, anchoVentana, altoVentana):
        
        self.ventanaPadre = ventPadre
        
        self.nombre = ""
        self.colegio = ""
        self.edad = ""
        
        self.ancho = anchoVentana
        self.alto = altoVentana
        
        self.dirImagenes = os.path.join("imagenes", "personajes")
        
        self.cursor = cursor
        self.screen = screen
        self.clock = clock
        
        imgBtnNino = Servicios.cargarImagen("boton_nino.png", self.dirImagenes)
        imgBtnNinoSelec = Servicios.cargarImagen("boton_nino_selec.png", self.dirImagenes)
    
        imgBtnNina = Servicios.cargarImagen("boton_nina.png", self.dirImagenes)
        imgBtnNinaSelec = Servicios.cargarImagen("boton_nina_selec.png", self.dirImagenes)
        
        imgBtnRegresar = Servicios.cargarImagen("boton_regresar.png", "imagenes")
        imgBtnRegresarSelec = Servicios.cargarImagen("boton_regresar_selec.png", "imagenes")
        
        imgBtnGuardar = Servicios.cargarImagen("boton_personaje.png", self.dirImagenes)
        imgBtnGuardarSelec = Servicios.cargarImagen("boton_personaje_selec.png", self.dirImagenes)
        
        self.letreroIncorrecto = pygame.image.load(os.path.join("imagenes", "personajes", "letreroIncorrecto.png")).convert_alpha()
        self.transparente = pygame.image.load(os.path.join("imagenes", "transparente.png")).convert_alpha()
        self.botonContinuar = Boton.BotonContinuar()
        self.mouse = Cursor.Mouse()
        
        self.initFont()
        
        self.personaje = self.ventanaPadre.personaje
        
        self.anchoPersonaje = 300
        
        
        self.numPersonaje = 1
        
        self.origen_x = 450
        self.origen_y = 100
        
        self.btnNino = Boton.Boton(imgBtnNino, imgBtnNinoSelec, 600 - 220, self.origen_y - 50)
        self.btnNina = Boton.Boton(imgBtnNina, imgBtnNinaSelec, 600 + 3, self.origen_y - 50)
        
        self.btnRegresar = Boton.Boton(imgBtnRegresar, imgBtnRegresarSelec, (self.ancho - 214 - 10), 10)
        
        self.btnGuardar = Boton.Boton(imgBtnGuardar, imgBtnGuardarSelec, (self.ancho - 330 - 10), (self.alto - 74 - 10))
        
    def initFont(self):
        pygame.font.init()
        rutaFuente = os.path.join("fuentes", "PatrickHand-Regular.ttf")
        self.fuenteGrande = pygame.font.Font(rutaFuente, 40)  # tamaño de la fuente
        self.fuente = pygame.font.Font(rutaFuente, 35)  # tamaño de la fuente
    
    def run(self):
        
        fondo = Servicios.cargarImagen("Fondo.jpg", os.path.join("imagenes"), False)
        
        fuenteTitulo = pygame.font.SysFont("helvetica", 30, True)
        fuenteTexto = pygame.font.SysFont("helvetica", 20)
        fuenteTextoN = pygame.font.SysFont("helvetica", 20, True)
        
        if self.personaje.sexo == "M":
            carpetaImg = "nino"
        else:
            carpetaImg = "nina"
        
        self.personaje.setAncho(self.anchoPersonaje)
        self.personaje.setX(self.origen_x)
        self.personaje.setY(self.origen_y)
        
        nombreSelec = False
        colegioSelec = False
        edadSelec = False
        
        faltaInfo = False
        
        xI = 650
        yI = 100
        
        yI2 = 300
        
        yI3 = 500
        
        
        self.campoNombre = CampoTexto.CampoTexto(xI - 200, yI3 + 160, 520, 30, 28)
        self.campoColegio = CampoTexto.CampoTexto(xI - 200, yI3 + 195, 520, 30, 28)
        self.campoEdad = CampoTexto.CampoTexto(xI - 200, yI3 + 230, 50, 30, 28)
        
        salir = False
        
        while salir == False:
            
            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:
                    
                    print event.key
                    
                    if edadSelec:
                        
                        longitud = len(self.edad)
                        nuevo = ""
                        cont = 0
                        for t in self.edad:
                            if(cont < longitud - 1):
                                nuevo = nuevo + t
                            cont += 1  
                        self.edad = nuevo  
                        
                        if longitud <= 2:
                        
                            if event.key == K_1:
                                self.edad = self.edad + "1"
                            if event.key == K_2:
                                self.edad = self.edad + "2"
                            if event.key == K_3:
                                self.edad = self.edad + "3"
                            if event.key == K_4:
                                self.edad = self.edad + "4"
                            if event.key == K_5:
                                self.edad = self.edad + "5"
                            if event.key == K_6:
                                self.edad = self.edad + "6"
                            if event.key == K_7:
                                self.edad = self.edad + "7"
                            if event.key == K_8:
                                self.edad = self.edad + "8"
                            if event.key == K_9:
                                self.edad = self.edad + "9"
                            if event.key == K_0:
                                self.edad = self.edad + "0"
                            
                        if event.key == K_BACKSPACE:
                            longitud = len(self.edad)
                            nuevo = ""
                            cont = 0
                            for t in self.edad:
                                if(cont < longitud - 1):
                                    nuevo = nuevo + t
                                cont += 1  
                            self.edad = nuevo
                        
                        self.edad = self.edad + "|" 
                    
                    if colegioSelec:
                        
                        longitud = len(self.colegio)
                        nuevo = ""
                        cont = 0
                        for t in self.colegio:
                            if(cont < longitud - 1):
                                nuevo = nuevo + t
                            cont += 1  
                        self.colegio = nuevo
                        
                        if longitud <= 33:
                        
                            if event.key == K_a:
                                self.colegio = self.colegio + "A"
                            if event.key == K_b:
                                self.colegio = self.colegio + "B"
                            if event.key == K_c:
                                self.colegio = self.colegio + "C"
                            if event.key == K_d:
                                self.colegio = self.colegio + "D"
                            if event.key == K_e:
                                self.colegio = self.colegio + "E"
                            if event.key == K_f:
                                self.colegio = self.colegio + "F"
                            if event.key == K_g:
                                self.colegio = self.colegio + "G"
                            if event.key == K_h:
                                self.colegio = self.colegio + "H"
                            if event.key == K_i:
                                self.colegio = self.colegio + "I"
                            if event.key == K_j:
                                self.colegio = self.colegio + "J"
                            if event.key == K_k:
                                self.colegio = self.colegio + "K"
                            if event.key == K_l:
                                self.colegio = self.colegio + "L"
                            if event.key == K_m:
                                self.colegio = self.colegio + "M"
                            if event.key == K_n:
                                self.colegio = self.colegio + "N"
                            if event.key == K_o:
                                self.colegio = self.colegio + "O"
                            if event.key == K_p:
                                self.colegio = self.colegio + "P"
                            if event.key == K_q:
                                self.colegio = self.colegio + "Q"
                            if event.key == K_r:
                                self.colegio = self.colegio + "R"
                            if event.key == K_s:
                                self.colegio = self.colegio + "S"
                            if event.key == K_t:
                                self.colegio = self.colegio + "T"
                            if event.key == K_u:
                                self.colegio = self.colegio + "U"
                            if event.key == K_v:
                                self.colegio = self.colegio + "V"
                            if event.key == K_w:
                                self.colegio = self.colegio + "W"
                            if event.key == K_x:
                                self.colegio = self.colegio + "X"
                            if event.key == K_y:
                                self.colegio = self.colegio + "Y"
                            if event.key == K_z:
                                self.colegio = self.colegio + "Z"
                            if event.key == K_SPACE:
                                self.colegio = self.colegio + " "
                                
                        if event.key == K_BACKSPACE:
                            longitud = len(self.colegio)
                            nuevo = ""
                            cont = 0
                            for t in self.colegio:
                                if(cont < longitud - 1):
                                    nuevo = nuevo + t
                                cont += 1  
                            self.colegio = nuevo
                        
                        self.colegio = self.colegio + "|" 
                        
                    #-----------------------------------------
                    if nombreSelec:
                        
                        longitud = len(self.nombre)
                        nuevo = ""
                        cont = 0
                        for t in self.nombre:
                            if(cont < longitud - 1):
                                nuevo = nuevo + t
                            cont += 1  
                        self.nombre = nuevo  
                        
                        if longitud <= 33:
                        
                            if event.key == K_a:
                                self.nombre = self.nombre + "A"
                            if event.key == K_b:
                                self.nombre = self.nombre + "B"
                            if event.key == K_c:
                                self.nombre = self.nombre + "C"
                            if event.key == K_d:
                                self.nombre = self.nombre + "D"
                            if event.key == K_e:
                                self.nombre = self.nombre + "E"
                            if event.key == K_f:
                                self.nombre = self.nombre + "F"
                            if event.key == K_g:
                                self.nombre = self.nombre + "G"
                            if event.key == K_h:
                                self.nombre = self.nombre + "H"
                            if event.key == K_i:
                                self.nombre = self.nombre + "I"
                            if event.key == K_j:
                                self.nombre = self.nombre + "J"
                            if event.key == K_k:
                                self.nombre = self.nombre + "K"
                            if event.key == K_l:
                                self.nombre = self.nombre + "L"
                            if event.key == K_m:
                                self.nombre = self.nombre + "M"
                            if event.key == K_n:
                                self.nombre = self.nombre + "N"
                            if event.key == K_o:
                                self.nombre = self.nombre + "O"
                            if event.key == K_p:
                                self.nombre = self.nombre + "P"
                            if event.key == K_q:
                                self.nombre = self.nombre + "Q"
                            if event.key == K_r:
                                self.nombre = self.nombre + "R"
                            if event.key == K_s:
                                self.nombre = self.nombre + "S"
                            if event.key == K_t:
                                self.nombre = self.nombre + "T"
                            if event.key == K_u:
                                self.nombre = self.nombre + "U"
                            if event.key == K_v:
                                self.nombre = self.nombre + "V"
                            if event.key == K_w:
                                self.nombre = self.nombre + "W"
                            if event.key == K_x:
                                self.nombre = self.nombre + "X"
                            if event.key == K_y:
                                self.nombre = self.nombre + "Y"
                            if event.key == K_z:
                                self.nombre = self.nombre + "Z"
                            if event.key == K_SPACE:
                                self.nombre = self.nombre + " "
                        if event.key == K_BACKSPACE:
                            longitud = len(self.nombre)
                            nuevo = ""
                            cont = 0
                            for t in self.nombre:
                                if(cont < longitud - 1):
                                    nuevo = nuevo + t
                                cont += 1  
                            self.nombre = nuevo
                        
                        self.nombre = self.nombre + "|"   
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    
                    if self.cursor.colliderect(self.campoNombre.rect2):
                        nombreSelec = True
                        longitud = len(self.nombre)
                        if longitud < 1:
                            self.nombre = self.nombre + "|"
                        else:
                            ultimo = self.nombre[longitud - 1]
                            if ultimo != "|":
                                self.nombre = self.nombre + "|"
                        print "dentro"
                    else:
                        nombreSelec = False
                        print "fuera"
                        longitud = len(self.nombre)
                        if  longitud > 0:
                            ultimo = self.nombre[longitud - 1]
                            if ultimo == "|":
                                nuevo = ""
                                cont = 0
                                for t in self.nombre:
                                    if(cont < longitud - 1):
                                        nuevo = nuevo + t
                                    cont += 1  
                                self.nombre = nuevo  
                                
                    if self.cursor.colliderect(self.campoColegio.rect2):
                        colegioSelec = True
                        longitud = len(self.colegio)
                        if longitud < 1:
                            self.colegio = self.colegio + "|"
                        else:
                            ultimo = self.colegio[longitud - 1]
                            if ultimo != "|":
                                self.colegio = self.colegio + "|"
                        print "dentro"
                    else:
                        colegioSelec = False
                        print "fuera"
                        longitud = len(self.colegio)
                        if  longitud > 0:
                            ultimo = self.colegio[longitud - 1]
                            if ultimo == "|":
                                nuevo = ""
                                cont = 0
                                for t in self.colegio:
                                    if(cont < longitud - 1):
                                        nuevo = nuevo + t
                                    cont += 1  
                                self.colegio = nuevo  
                                
                    if self.cursor.colliderect(self.campoEdad.rect2):
                        edadSelec = True
                        longitud = len(self.edad)
                        if longitud < 1:
                            self.edad = self.edad + "|"
                        else:
                            ultimo = self.edad[longitud - 1]
                            if ultimo != "|":
                                self.edad = self.edad + "|"
                        print "dentro"
                    else:
                        edadSelec = False
                        print "fuera"
                        longitud = len(self.edad)
                        if  longitud > 0:
                            ultimo = self.edad[longitud - 1]
                            if ultimo == "|":
                                nuevo = ""
                                cont = 0
                                for t in self.edad:
                                    if(cont < longitud - 1):
                                        nuevo = nuevo + t
                                    cont += 1  
                                self.edad = nuevo  
                    
                    if self.cursor.colliderect(self.personaje.rect):
                        print "click en personaje"
                    
                    self.mouse.rect.center = pygame.mouse.get_pos()
                        
                    if pygame.sprite.collide_rect(self.botonContinuar, self.mouse):
                            faltaInfo = False
                    
                    if self.cursor.colliderect(self.btnGuardar.rect):
                        if self.nombre == "" or self.colegio == "" or self.edad == "":
                            faltaInfo = True
                        else:
                            salir = True
                            self.personaje.setNombre(self.nombre)
                            self.personaje.setColegio(self.colegio)
                            self.personaje.setEdad(self.edad)
                            self.ventanaPadre.setPersonaje(self.personaje, self.personaje.imagen)
                            self.ventanaPadre.tablero.run()
                    
                    if self.cursor.colliderect(self.btnRegresar.rect):
                        salir = True
                        self.ventanaPadre.run()
                    
                    if self.cursor.colliderect(self.btnNina.rect):
                        self.personaje.setSexo("F")
                        
                        imagen = Servicios.cargarImagen("Nina_Camina-01.png", os.path.join("imagenes", "verdad"))
                        self.personaje.setImagen(imagen)
                    
                    if self.cursor.colliderect(self.btnNino.rect):
                        self.personaje.setSexo("M")
                        
                        imagen = Servicios.cargarImagen("Frente1.png", os.path.join("imagenes", "verdad"))
                        self.personaje.setImagen(imagen)
                            
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.clock.tick(60)
            
            self.cursor.update()
            
            self.screen.blit(fondo, (0, 0))
            
            self.personaje.dibujar(self.screen)
                     
            self.btnNino.update(self.screen, self.cursor)
            self.btnNina.update(self.screen, self.cursor)
            
            self.btnRegresar.update(self.screen, self.cursor)
            
            self.btnGuardar.update(self.screen, self.cursor)
            
            textoCabeza = self.fuenteGrande.render("Elige a tu personaje:", 1, (255, 255, 255))
            
            self.screen.blit(textoCabeza, (10, 10))
            
            textoNombre = self.fuente.render("Nombre: ", 1, (255, 255, 255))
            self.screen.blit(textoNombre, (xI - 320, yI3 + 150))
            
            textoColegio = self.fuente.render("Colegio: ", 1, (255, 255, 255))
            self.screen.blit(textoColegio, (xI - 317, yI3 + 185))
            
            textoEdad = self.fuente.render("Edad: ", 1, (255, 255, 255))
            self.screen.blit(textoEdad, (xI - 290, yI3 + 220))
             
            self.campoNombre.setText(self.nombre)
            self.campoColegio.setText(self.colegio)
            self.campoEdad.setText(self.edad)
            
            self.screen.blit(self.campoNombre.image, (self.campoNombre.x, self.campoNombre.y))
            self.screen.blit(self.campoColegio.image, (self.campoColegio.x, self.campoColegio.y))
            self.screen.blit(self.campoEdad.image, (self.campoEdad.x, self.campoEdad.y))
            
            if faltaInfo:
                self.screen.blit(self.transparente, (0, 0))
                self.screen.blit(self.letreroIncorrecto, (382, 198))
                self.botonContinuar.rect.center = (600, 560)
                self.screen.blit(self.botonContinuar.image, self.botonContinuar.rect)
            
            pygame.display.update()
            
            
