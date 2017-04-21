#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, os, sys, Amor, pazSemillas, Rectitud, pacman, puzzle, time
from modelo import Cursor, Boton, MensajeEmergente
from control import Servicios  # , pyaudio
from pygame.locals import *
from sys import byteorder
from array import array

class VentanaMandala(object):
    
    def __init__(self, cursor, screen, clock, anchoVentana, altoVentana, tipo, padre):
        '''
        1:"Flor"  
        2:"Hojas"  
        3:"Nino"
        4:"Sol"
        5:"Flor2"
        '''
        self.tipo = tipo
        
        self.ancho = anchoVentana
        self.alto = altoVentana
        self.cursor = Cursor.Cursor()
        
        self.cursor2 = cursor
        
        self.screen = screen
        self.clock = clock
        self.tablero = padre
        
        self.initFont()
        
        self.paz = None
        self.amor = None
        self.rectitud = None
        self.verdad = None
        self.noViolencia = None
        
        self.msjInicio = MensajeEmergente.MensajeInicial(40, "Silencio")
        self.msjGanaste = MensajeEmergente.MensajeGanaste(28, "Silencio")
        
        self.dirImagenes = os.path.join("imagenes", "mandalas")
        
        self.imgColor = Servicios.cargarImagen("Mandala_%s.png" % (self.tipo), self.dirImagenes)
        
        self.imgSinColor = Servicios.cargarImagen("Mandala_%s_ByN.png" % (self.tipo), self.dirImagenes)
        
        self.imgRojoSelec = Servicios.cargarImagen("Paleta_Rojo_Selec.png", self.dirImagenes)
        
        self.imgAmarilloSelec = Servicios.cargarImagen("Paleta_Amarillo_Selec.png", self.dirImagenes)
        
        self.imgAzulSelec = Servicios.cargarImagen("Paleta_Azul_Selec.png", self.dirImagenes)
        
        self.imgMoradoSelec = Servicios.cargarImagen("Paleta_Morado_Selec.png", self.dirImagenes)
        
        self.imgNaranjaSelec = Servicios.cargarImagen("Paleta_Naranja_Selec.png", self.dirImagenes)
        
        self.imgVerdeSelec = Servicios.cargarImagen("Paleta_Verde_Selec.png", self.dirImagenes)
        
        ancho = 24
        self.imgPincel = Servicios.cargarImagen("Pincel.png", self.dirImagenes)
        altoImg = ancho * self.imgPincel.get_height() / self.imgPincel.get_width()
        self.imgPincel = pygame.transform.smoothscale(self.imgPincel, (ancho, altoImg))
        
        self.imgRojoSel = Servicios.cargarImagen("Mandala_%s_Rojo_Seleccionado.png" % (self.tipo), self.dirImagenes)
        
        self.imgAmarilloSel = Servicios.cargarImagen("Mandala_%s_Amarillo_Seleccionado.png" % (self.tipo), self.dirImagenes)
        
        self.imgAzulSel = Servicios.cargarImagen("Mandala_%s_Azul_Seleccionado.png" % (self.tipo), self.dirImagenes)
        
        self.imgMoradoSel = Servicios.cargarImagen("Mandala_%s_Morado_Seleccionado.png" % (self.tipo), self.dirImagenes)
        
        self.imgNaranjaSel = Servicios.cargarImagen("Mandala_%s_Naranja_Seleccionado.png" % (self.tipo), self.dirImagenes)
        
        self.imgVerdeSel = Servicios.cargarImagen("Mandala_%s_Verde_Seleccionado.png" % (self.tipo), self.dirImagenes)
       
        self.x = self.ancho - (self.ancho / 2) - (self.imgColor.get_width() / 2)
        self.y = self.alto - (self.alto / 2) - (self.imgColor.get_height() / 2) - 20
        
        sumarAX = self.x
        sumarAY = self.y
        
        self.areaRojo = Rect(750 + sumarAX, 165 + sumarAY, 44, 44) 
        self.areaAmarillo = Rect(745 + sumarAX, 115 + sumarAY, 44, 44) 
        self.areaAzul = Rect(773 + sumarAX, 76 + sumarAY, 44, 41) 
        self.areaMorado = Rect(820 + sumarAX, 65 + sumarAY, 44, 44) 
        self.areaNaranja = Rect(868 + sumarAX, 85 + sumarAY, 44, 44) 
        self.areaVerde = Rect(883 + sumarAX, 137 + sumarAY, 44, 44) 
          
        xBotones = 850
        yInicial = 380
        deltaY = 70
        
        imgBtnArea1 = Servicios.cargarImagen("boton_area1.png", self.dirImagenes)
        imgBtnArea1Selec = Servicios.cargarImagen("boton_area1_selec.png", self.dirImagenes)
        
        self.btnArea1 = Boton.Boton(imgBtnArea1, imgBtnArea1Selec, xBotones, yInicial)
        
        imgBtnArea2 = Servicios.cargarImagen("boton_area2.png", self.dirImagenes)
        imgBtnArea2Selec = Servicios.cargarImagen("boton_area2_selec.png", self.dirImagenes)
        
        self.btnArea2 = Boton.Boton(imgBtnArea2, imgBtnArea2Selec, xBotones, yInicial + deltaY)
        
        imgBtnArea3 = Servicios.cargarImagen("boton_area3.png", self.dirImagenes)
        imgBtnArea3Selec = Servicios.cargarImagen("boton_area3_selec.png", self.dirImagenes)
        
        self.btnArea3 = Boton.Boton(imgBtnArea3, imgBtnArea3Selec, xBotones, yInicial + 2 * deltaY)
        
        imgBtnArea4 = Servicios.cargarImagen("boton_area4.png", self.dirImagenes)
        imgBtnArea4Selec = Servicios.cargarImagen("boton_area4_selec.png", self.dirImagenes)
        
        self.btnArea4 = Boton.Boton(imgBtnArea4, imgBtnArea4Selec, xBotones, yInicial + 3 * deltaY)
        
        imgBtnArea5 = Servicios.cargarImagen("boton_area5.png", self.dirImagenes)
        imgBtnArea5Selec = Servicios.cargarImagen("boton_area5_selec.png", self.dirImagenes)
        
        self.btnArea5 = Boton.Boton(imgBtnArea5, imgBtnArea5Selec, xBotones, yInicial + 4 * deltaY)
        
        imgBtnArea6 = Servicios.cargarImagen("boton_area6.png", self.dirImagenes)
        imgBtnArea6Selec = Servicios.cargarImagen("boton_area6_selec.png", self.dirImagenes)
     
        self.btnArea6 = Boton.Boton(imgBtnArea6, imgBtnArea6Selec, xBotones, yInicial + 5 * deltaY)
        
        imgBtnRegresar = Servicios.cargarImagen("boton_regresar.png", "imagenes")
        imgBtnRegresarSelec = Servicios.cargarImagen("boton_regresar_selec.png", "imagenes")
        
        self.btnRegresar = Boton.Boton(imgBtnRegresar, imgBtnRegresarSelec, (self.ancho - 214 - 10), 10)
        
        imgBtnAyuda = Servicios.cargarImagen("BotonesAyuda.png", os.path.join("imagenes", "citas"))
        imgBtnAyudaSelec = Servicios.cargarImagen("BotonesAyuda_selec.png", os.path.join("imagenes", "citas"))
        
        self.btnAyuda = Boton.Boton(imgBtnAyuda, imgBtnAyudaSelec, 5, 750)
        
    def initFont(self):
        pygame.font.init()
        rutaFuente = os.path.join("fuentes", "PatrickHand-Regular.ttf")
        self.fuenteGrande = pygame.font.Font(rutaFuente, 40)  # tamaño de la fuente
        # self.fuente = pygame.font.Font(rutaFuente, 35)  # tamaño de la fuente    
        
        
        
    def setTipo(self, tipo):    
        self.tipo = tipo

        
        self.imgColor = Servicios.cargarImagen("Mandala_%s.png" % (self.tipo), self.dirImagenes)
        
        self.imgSinColor = Servicios.cargarImagen("Mandala_%s_ByN.png" % (self.tipo), self.dirImagenes)
        
        self.imgRojoSel = Servicios.cargarImagen("Mandala_%s_Rojo_Seleccionado.png" % (self.tipo), self.dirImagenes)
        
        self.imgAmarilloSel = Servicios.cargarImagen("Mandala_%s_Amarillo_Seleccionado.png" % (self.tipo), self.dirImagenes)
        
        self.imgAzulSel = Servicios.cargarImagen("Mandala_%s_Azul_Seleccionado.png" % (self.tipo), self.dirImagenes)
        
        self.imgMoradoSel = Servicios.cargarImagen("Mandala_%s_Morado_Seleccionado.png" % (self.tipo), self.dirImagenes)
        
        self.imgNaranjaSel = Servicios.cargarImagen("Mandala_%s_Naranja_Seleccionado.png" % (self.tipo), self.dirImagenes)
        
        self.imgVerdeSel = Servicios.cargarImagen("Mandala_%s_Verde_Seleccionado.png" % (self.tipo), self.dirImagenes)
        
    def run(self):
        
        inicio = True
        juego = False
        gano = False
        
        pasoSonidoExito = False
        
        fondo = Servicios.cargarImagen("Fondo.jpg", os.path.join("imagenes"), False)
        
        color = None
        
        area = None
        
        imgArea1 = None
        imgArea2 = None
        imgArea3 = None
        imgArea4 = None
        imgArea5 = None
        imgArea6 = None
        
        area1Correcto = False
        area2Correcto = False
        area3Correcto = False
        area4Correcto = False
        area5Correcto = False
        area6Correcto = False
        
        pasoSilencio = False
        
        segundos = 0
        frames = 0
        silencio = True
        
        fuenteTitulo = pygame.font.SysFont("helvetica", 30, True)
        fuenteTexto = pygame.font.SysFont("helvetica", 20)
        fuenteTextoN = pygame.font.SysFont("helvetica", 20, True)
        
        textoColorear = self.fuenteGrande.render("Selecciona primero un area y luego un color para colorear", 1, (255, 255, 255))
        
        salir = False
        
        while salir == False:
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    
                    if self.cursor.colliderect(self.btnRegresar.rect):
                        pygame.mouse.set_visible(True)
                        salir = True
                        self.tablero.sonido.play(-1)
                        self.tablero.run()
                        
                        
                    if self.cursor.colliderect(self.btnAyuda.rect):
                        self.screen.blit(self.imgColor, (self.x, self.y))
                        pygame.display.update()
                        pygame.time.delay(2000)
                        
                    if self.cursor.colliderect(self.msjInicio.btn.rect):
                        self.msjInicio.visible = False
                        inicio = False
                        juego = True
                        
                    if self.cursor.colliderect(self.msjGanaste.btn.rect):
                        if self.tipo == "Flor":
                            self.tablero.pasoSilencioAmor = True
                        if self.tipo == "Sol":
                            self.tablero.pasoSilencioRectitud = True
                        if self.tipo == "Hojas":
                            self.tablero.pasoSilencioPaz = True
                        if self.tipo == "Nino":
                            self.tablero.pasoSilencioVerdad = True
                        if self.tipo == "Flor2":
                            self.tablero.pasoSilencioNoViolencia = True
                        self.msjGanaste.visible = False
                        self.tablero.sonido.play(-1)
                        salir = True
                        self.tablero.run()
                    
                    if self.cursor.colliderect(self.areaRojo):
                        color = "Rojo"
                        # print "Click en ", color
                        ancho = 24
                        self.imgPincel = Servicios.cargarImagen("Pincel_Rojo.png", self.dirImagenes)
                        altoImg = ancho * self.imgPincel.get_height() / self.imgPincel.get_width()
                        self.imgPincel = pygame.transform.smoothscale(self.imgPincel, (ancho, altoImg))
                        
                        if area is not None:
                            if area == 1:
                                imgArea1 = Servicios.cargarImagen("Mandala_%s_Naranja_%s.png" % (self.tipo, color), self.dirImagenes)
                                area1Correcto = False    
                            elif area == 2:
                                imgArea2 = Servicios.cargarImagen("Mandala_%s_Amarillo_%s.png" % (self.tipo, color), self.dirImagenes)
                                area2Correcto = False
                            elif area == 3:
                                imgArea3 = Servicios.cargarImagen("Mandala_%s_Verde_%s.png" % (self.tipo, color), self.dirImagenes)
                                area3Correcto = False
                            elif area == 4:
                                imgArea4 = Servicios.cargarImagen("Mandala_%s_Azul_%s.png" % (self.tipo, color), self.dirImagenes)
                                area4Correcto = False
                            elif area == 5:
                                imgArea5 = Servicios.cargarImagen("Mandala_%s_Morado_%s.png" % (self.tipo, color), self.dirImagenes)
                                area5Correcto = False
                            elif area == 6:
                                imgArea6 = Servicios.cargarImagen("Mandala_%s_Rojo_%s.png" % (self.tipo, color), self.dirImagenes)
                                area6Correcto = True
                        
                        
                    elif self.cursor.colliderect(self.areaAmarillo):
                        color = "Amarillo"
                        # print "Click en ", color
                        ancho = 24
                        self.imgPincel = Servicios.cargarImagen("Pincel_Amarillo.png", self.dirImagenes)
                        altoImg = ancho * self.imgPincel.get_height() / self.imgPincel.get_width()
                        self.imgPincel = pygame.transform.smoothscale(self.imgPincel, (ancho, altoImg))

                        if area is not None:
                        
                            if area == 1:
                                imgArea1 = Servicios.cargarImagen("Mandala_%s_Naranja_%s.png" % (self.tipo, color), self.dirImagenes)
                                area1Correcto = False
                            elif area == 2:
                                imgArea2 = Servicios.cargarImagen("Mandala_%s_Amarillo_%s.png" % (self.tipo, color), self.dirImagenes)
                                area2Correcto = True
                            elif area == 3:
                                imgArea3 = Servicios.cargarImagen("Mandala_%s_Verde_%s.png" % (self.tipo, color), self.dirImagenes)
                                area3Correcto = False
                            elif area == 4:
                                imgArea4 = Servicios.cargarImagen("Mandala_%s_Azul_%s.png" % (self.tipo, color), self.dirImagenes)
                                area4Correcto = False
                            elif area == 5:
                                imgArea5 = Servicios.cargarImagen("Mandala_%s_Morado_%s.png" % (self.tipo, color), self.dirImagenes)
                                area5Correcto = False
                            elif area == 6:
                                imgArea6 = Servicios.cargarImagen("Mandala_%s_Rojo_%s.png" % (self.tipo, color), self.dirImagenes)
                                area6Correcto = False
                    
                    elif self.cursor.colliderect(self.areaAzul):
                        color = "Azul"
                        # print "Click en ", color
                        ancho = 24
                        self.imgPincel = Servicios.cargarImagen("Pincel_Azul.png", self.dirImagenes)
                        altoImg = ancho * self.imgPincel.get_height() / self.imgPincel.get_width()
                        self.imgPincel = pygame.transform.smoothscale(self.imgPincel, (ancho, altoImg))

                        if area is not None:
                        
                            if area == 1:
                                imgArea1 = Servicios.cargarImagen("Mandala_%s_Naranja_%s.png" % (self.tipo, color), self.dirImagenes)
                                area1Correcto = False
                            elif area == 2:
                                imgArea2 = Servicios.cargarImagen("Mandala_%s_Amarillo_%s.png" % (self.tipo, color), self.dirImagenes)
                                area2Correcto = False
                            elif area == 3:
                                imgArea3 = Servicios.cargarImagen("Mandala_%s_Verde_%s.png" % (self.tipo, color), self.dirImagenes)
                                area3Correcto = False
                            elif area == 4:
                                imgArea4 = Servicios.cargarImagen("Mandala_%s_Azul_%s.png" % (self.tipo, color), self.dirImagenes)
                                area4Correcto = True
                            elif area == 5:
                                imgArea5 = Servicios.cargarImagen("Mandala_%s_Morado_%s.png" % (self.tipo, color), self.dirImagenes)
                                area5Correcto = False
                            elif area == 6:
                                imgArea6 = Servicios.cargarImagen("Mandala_%s_Rojo_%s.png" % (self.tipo, color), self.dirImagenes)
                                area6Correcto = False
                    
                    elif self.cursor.colliderect(self.areaMorado):
                        color = "Morado"
                        # print "Click en ", color
                        ancho = 24
                        self.imgPincel = Servicios.cargarImagen("Pincel_Morado.png", self.dirImagenes)
                        altoImg = ancho * self.imgPincel.get_height() / self.imgPincel.get_width()
                        self.imgPincel = pygame.transform.smoothscale(self.imgPincel, (ancho, altoImg))

                        if area is not None:
                        
                            if area == 1:
                                imgArea1 = Servicios.cargarImagen("Mandala_%s_Naranja_%s.png" % (self.tipo, color), self.dirImagenes)
                                area1Correcto = False
                            elif area == 2:
                                imgArea2 = Servicios.cargarImagen("Mandala_%s_Amarillo_%s.png" % (self.tipo, color), self.dirImagenes)
                                area2Correcto = False
                            elif area == 3:
                                imgArea3 = Servicios.cargarImagen("Mandala_%s_Verde_%s.png" % (self.tipo, color), self.dirImagenes)
                                area3Correcto = False
                            elif area == 4:
                                imgArea4 = Servicios.cargarImagen("Mandala_%s_Azul_%s.png" % (self.tipo, color), self.dirImagenes)
                                area4Correcto = False
                            elif area == 5:
                                imgArea5 = Servicios.cargarImagen("Mandala_%s_Morado_%s.png" % (self.tipo, color), self.dirImagenes)
                                area5Correcto = True
                            elif area == 6:
                                imgArea6 = Servicios.cargarImagen("Mandala_%s_Rojo_%s.png" % (self.tipo, color), self.dirImagenes)
                                area6Correcto = False
                        
                    elif self.cursor.colliderect(self.areaNaranja):
                        color = "Naranja"
                        # print "Click en ", color
                        ancho = 24
                        self.imgPincel = Servicios.cargarImagen("Pincel_Naranja.png", self.dirImagenes)
                        altoImg = ancho * self.imgPincel.get_height() / self.imgPincel.get_width()
                        self.imgPincel = pygame.transform.smoothscale(self.imgPincel, (ancho, altoImg))

                        if area is not None:
                        
                            if area == 1:
                                imgArea1 = Servicios.cargarImagen("Mandala_%s_Naranja_%s.png" % (self.tipo, color), self.dirImagenes)
                                area1Correcto = True
                            elif area == 2:
                                imgArea2 = Servicios.cargarImagen("Mandala_%s_Amarillo_%s.png" % (self.tipo, color), self.dirImagenes)
                                area2Correcto = False
                            elif area == 3:
                                imgArea3 = Servicios.cargarImagen("Mandala_%s_Verde_%s.png" % (self.tipo, color), self.dirImagenes)
                                area3Correcto = False
                            elif area == 4:
                                imgArea4 = Servicios.cargarImagen("Mandala_%s_Azul_%s.png" % (self.tipo, color), self.dirImagenes)
                                area4Correcto = False
                            elif area == 5:
                                imgArea5 = Servicios.cargarImagen("Mandala_%s_Morado_%s.png" % (self.tipo, color), self.dirImagenes)
                                area5Correcto = False
                            elif area == 6:
                                imgArea6 = Servicios.cargarImagen("Mandala_%s_Rojo_%s.png" % (self.tipo, color), self.dirImagenes)
                                area6Correcto = False
                        
                    elif self.cursor.colliderect(self.areaVerde):
                        color = "Verde"
                        # print "Click en ", color
                        ancho = 24
                        self.imgPincel = Servicios.cargarImagen("Pincel_Verde.png", self.dirImagenes)
                        altoImg = ancho * self.imgPincel.get_height() / self.imgPincel.get_width()
                        self.imgPincel = pygame.transform.smoothscale(self.imgPincel, (ancho, altoImg))

                        if area is not None:
                        
                            if area == 1:
                                imgArea1 = Servicios.cargarImagen("Mandala_%s_Naranja_%s.png" % (self.tipo, color), self.dirImagenes)
                                area1Correcto = False
                            elif area == 2:
                                imgArea2 = Servicios.cargarImagen("Mandala_%s_Amarillo_%s.png" % (self.tipo, color), self.dirImagenes)
                                area2Correcto = False
                            elif area == 3:
                                imgArea3 = Servicios.cargarImagen("Mandala_%s_Verde_%s.png" % (self.tipo, color), self.dirImagenes)
                                area3Correcto = True
                            elif area == 4:
                                imgArea4 = Servicios.cargarImagen("Mandala_%s_Azul_%s.png" % (self.tipo, color), self.dirImagenes)
                                area4Correcto = False
                            elif area == 5:
                                imgArea5 = Servicios.cargarImagen("Mandala_%s_Morado_%s.png" % (self.tipo, color), self.dirImagenes)
                                area5Correcto = False
                            elif area == 6:
                                imgArea6 = Servicios.cargarImagen("Mandala_%s_Rojo_%s.png" % (self.tipo, color), self.dirImagenes)
                                area6Correcto = False
                        
                    elif self.cursor.colliderect(self.btnArea1.rect):
                        area = 1
                        # print "Click en area", area
                        
                    elif self.cursor.colliderect(self.btnArea2.rect):
                        area = 2
                        # print "Click en area", area 
                        
                    elif self.cursor.colliderect(self.btnArea3.rect):
                        area = 3
                        # print "Click en area", area    
                        
                    elif self.cursor.colliderect(self.btnArea4.rect):
                        area = 4
                        # print "Click en area", area  
                        
                    elif self.cursor.colliderect(self.btnArea5.rect):
                        area = 5
                        # print "Click en area", area      
                        
                    elif self.cursor.colliderect(self.btnArea6.rect):
                        area = 6
                        # print "Click en area", area
                                
                    
            self.clock.tick(60)
            
            self.screen.blit(fondo, (0, 0))
            
            self.cursor.update()
            
            self.msjInicio.update(self.screen, self.cursor)
            self.msjGanaste.update(self.screen, self.cursor)
            
            if inicio:
                self.msjInicio.visible = True
                self.btnRegresar.update(self.screen, self.cursor)
            
            
            elif juego:
            
                if pasoSilencio == False:
                    
                    # pygame.mouse.set_visible(True)
                    
                    # self.screen.blit(self.imgColor, (0, 0))
                    
                    #self.screen.blit(fondo, (0, 0))
                    
                    #self.btnRegresar.update(self.screen, self.cursor)
                    
                    # THRESHOLD = 1500
                    # CHUNK_SIZE = 1024
                    # FORMAT = pyaudio.paInt16
                    # RATE = 44100
                
                    # p = pyaudio.PyAudio()
                    # stream = p.open(format=FORMAT, channels=1, rate=RATE,
                    # input=True, output=True,
                    # frames_per_buffer=CHUNK_SIZE)
            
                    # r = array('h')
                    
                    # a 60 FPS 600 frames equivalen a 10 segundos
                    
                    t = time.time()
            
                    while segundos <= 10:
                        
                        self.clock.tick(60)
                        
                        self.screen.blit(fondo, (0, 0))
                    
                        self.btnRegresar.update(self.screen, self.cursor)
                        
                        self.cursor.update()
                        
                        # little endian, signed short
                        # snd_data = array('h', stream.read(CHUNK_SIZE))
                        # if byteorder == 'big':
                            # snd_data.byteswap()
                        # r.extend(snd_data)
                            
                        # 'True' if below the 'silent' threshold
                        # silencio = max(snd_data) < THRESHOLD
                        
                        # silencio = True
                        
                        # if silencio == False:
                            # t = time.time()
    
                        # self.screen.fill(self.color)
                        
                        
                        
                        self.screen.blit(self.imgColor, (self.x, self.y))
                        
                        texto = self.fuenteGrande.render("Observa la mandala en silencio durante 10 segundos", 1, (255, 255, 255))
                        
                        textoSeg = self.fuenteGrande.render(str("Segundos restantes: %d" % (10 - segundos)), 1, (255, 255, 255))
                        
                        self.screen.blit(texto, (10, 10))
                        self.screen.blit(textoSeg, (10, 770))
                        
                        self.btnRegresar.update(self.screen, self.cursor)
                        
                        #self.screen.blit(self.imgPincel, self.cursor)
                        
                        pygame.display.update()
                        
                        segundos = time.time() - t
                        segundos = int(segundos)
                        
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            
                                if self.cursor.colliderect(self.btnRegresar.rect):
                                    pygame.mouse.set_visible(True)
                                    segundos = 11
                                    salir = True
                                    self.tablero.sonido.play(-1)
                                    self.tablero.run()
                            
                    pasoSilencio = True
    
                
                # self.cursor.update()
                
                # self.screen.blit(fondo, (0, 0))
                
                
                pygame.mouse.set_visible(False)  # hace al mouse invisible
                
                self.screen.blit(self.imgSinColor, (self.x, self.y))
                
                
                self.btnRegresar.update(self.screen, self.cursor)
                self.btnAyuda.update(self.screen, self.cursor)
                
                self.btnArea1.update(self.screen, self.cursor)
                self.btnArea2.update(self.screen, self.cursor)
                self.btnArea3.update(self.screen, self.cursor)
                self.btnArea4.update(self.screen, self.cursor)
                self.btnArea5.update(self.screen, self.cursor)
                self.btnArea6.update(self.screen, self.cursor)
                
                # self.btnColorear.update(self.screen, self.cursor)
                
                if self.cursor.colliderect(self.areaRojo):
                    self.screen.blit(self.imgRojoSelec, (self.x, self.y))
                    
                if self.cursor.colliderect(self.areaAmarillo):
                    self.screen.blit(self.imgAmarilloSelec, (self.x, self.y))
                    
                if self.cursor.colliderect(self.areaAzul):
                    self.screen.blit(self.imgAzulSelec, (self.x, self.y))
                    
                if self.cursor.colliderect(self.areaMorado):
                    self.screen.blit(self.imgMoradoSelec, (self.x, self.y))
                    
                if self.cursor.colliderect(self.areaNaranja):
                    self.screen.blit(self.imgNaranjaSelec, (self.x, self.y))
                    
                if self.cursor.colliderect(self.areaVerde):
                    self.screen.blit(self.imgVerdeSelec, (self.x, self.y)) 
                
                
                if imgArea1 != None:
                    self.screen.blit(imgArea1, (self.x, self.y))
                    
                if imgArea2 != None:
                    self.screen.blit(imgArea2, (self.x, self.y))
                    
                if imgArea3 != None:
                    self.screen.blit(imgArea3, (self.x, self.y))
                    
                if imgArea4 != None:
                    self.screen.blit(imgArea4, (self.x, self.y))
                    
                if imgArea5 != None:
                    self.screen.blit(imgArea5, (self.x, self.y))
                    
                if imgArea6 != None:
                    self.screen.blit(imgArea6, (self.x, self.y))
                
                    
                if area == 1:
                    self.screen.blit(self.imgNaranjaSel, (self.x, self.y))
                    
                if area == 2:
                    self.screen.blit(self.imgAmarilloSel, (self.x, self.y))
                    
                if area == 3:
                    self.screen.blit(self.imgVerdeSel, (self.x, self.y))
                
                if area == 4:
                    self.screen.blit(self.imgAzulSel, (self.x, self.y))
                    
                if area == 5:
                    self.screen.blit(self.imgMoradoSel, (self.x, self.y))
                    
                if area == 6:
                    self.screen.blit(self.imgRojoSel, (self.x, self.y))
                    
                
                self.screen.blit(textoColorear, (10, 10))
                
                '''
                pygame.draw.rect (self.screen , (100, 100, 100) , self.areaRojo, 2)
                
                pygame.draw.rect (self.screen , (100, 100, 100) , self.areaAmarillo, 2)
                
                pygame.draw.rect (self.screen , (100, 100, 100) , self.areaAzul, 2)
                
                pygame.draw.rect (self.screen , (100, 100, 100) , self.areaMorado, 2)
                
                pygame.draw.rect (self.screen , (100, 100, 100) , self.areaNaranja, 2)
                
                pygame.draw.rect (self.screen , (100, 100, 100) , self.areaVerde, 2)
                '''
        # gano    
                if area1Correcto and area2Correcto and area3Correcto and area4Correcto and area5Correcto and area6Correcto:
                    
                    # self.tablero.sonidoExito.play()
                    
                    # textoPaso = self.fuenteGrande.render(str("!Has coloreado la mandala correctamente!"), 1, (255, 255, 255))
                    # self.screen.blit(textoPaso, (10, 770))
                    # pygame.display.update()
                    # pygame.time.delay(2000)
                    
                    # self.tablero.sonido.play(-1)
                    juego = False
                    gano = True
                    
                    
                    
                    
                    #self.tablero.run()
                    
                
                if self.cursor.left > 0 and self.cursor.left < self.ancho and self.cursor.top > 0 and self.cursor.top < self.alto:
                    self.screen.blit(self.imgPincel, self.cursor)
                    
            elif gano:
                
                pygame.mouse.set_visible(True)
                
                if pasoSonidoExito == False:
                    self.tablero.sonidoExito.play()
                    pasoSonidoExito = True
                
                self.msjGanaste.visible = True
                
            
            pygame.display.update()
        
