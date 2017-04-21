#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, os, random
from modelo import Boton, Cursor, pieza, MensajeEmergente
from control import Servicios
from pygame.locals import *
class Puzzle(object):
    
    def __init__(self, cursor, screen, clock, padre):
        self.cursor = cursor
        bif = os.path.join("imagenes", "noViolencia", "fondoPuzzle.png")
        self.background = pygame.image.load(bif).convert()
        self.transparente = pygame.image.load(os.path.join("imagenes", "transparente.png")).convert_alpha()
        self.screen = screen
        self.clock = clock
        
        self.tablero = padre
        
        self.audio = Servicios.cargarSonido("noViolencia.ogg", os.path.join("audios", "cuentos"))
        
        self.msjInicio = MensajeEmergente.MensajeInicial(40, "CuentoNoViolencia")
        self.msjGanaste = MensajeEmergente.MensajeGanaste(28, "JuegoNoViolencia")
        
        # self.cita = fraseNoViolencia.FraseNoViolencia(self.screen, self.clock, self.cursor, self.tablero)
        
        self.mouse = Cursor.Mouse()
        self.botonContinuar = Boton.BotonContinuar()
        self.botonTerminar = Boton.BotonTerminar()
        
        #self.instrucciones = pygame.image.load(os.path.join("imagenes", "inicioNoViolencia.png")).convert_alpha()
        #self.letrero = pygame.image.load(os.path.join("imagenes", "noViolencia", "letreroGanadoPuzzle.png")).convert_alpha()
  
        self.inicio = True
        self.juego = False
        self.terminar = False
        self.gano = False
        self.unaVez = True
        
        self.piezas = pygame.sprite.Group()
        self.posiciones = []
        self.loadPiezas()
        self.seleccionada = None
        self.mezclar()
        
        imgBtnRegresar = Servicios.cargarImagen("boton_regresar.png", "imagenes")
        imgBtnRegresarSelec = Servicios.cargarImagen("boton_regresar_selec.png", "imagenes")
        
        self.btnRegresar = Boton.Boton(imgBtnRegresar, imgBtnRegresarSelec, (1200 - 214 - 10), 10)
        

        
    def mezclar(self):
        random.shuffle(self.posiciones)
        i = 0
        for x in self.piezas:
            x.rect.center = self.posiciones[i][0]
            x.x = self.posiciones[i][1]
            x.y = self.posiciones[i][2]
            i += 1
    
    def chequeo(self):
        i = 0
        for x in self.piezas:
            if x.rect.center == x.posicionCorrecta:
                i += 1

        return i == 9
            
        
        
    def reiniciar(self):
        self.inicio = True
        self.juego = False
        self.terminar = False
        self.gano = False
        self.posiciones = []
        self.seleccionada = None
        self.unaVez = True
        self.piezas.empty()
        self.loadPiezas()
        self.mezclar()
     
    
    def loadPiezas(self):
        
        x_offset = (925 / 6)
        y_offset = (625 / 6)
        iniciox = 140
        inicioy = 100
        
        for y in range(3):
            for x in range(3):
                centerPoint = [(x * ((945 / 3))) + x_offset + iniciox, (y * ((645 / 3))) + y_offset + inicioy]
                self.posiciones.append([centerPoint, x, y])
                piezaV = pieza.Pieza(pygame.image.load(os.path.join("imagenes", "noViolencia", "pieza0" + str(y + 1) + "0" + str(x + 1) + ".png")).convert(), x, y, centerPoint)
                self.piezas.add(piezaV)

    
    def run(self):
        
        
        
        self.reiniciar()
        
        # pygame.mouse.set_visible(True)
        
        pasoSonidoExito = False
        sonido2Sonando = False
        
        self.audio.play()
        
        
        while not self.terminar:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT: 
                    sys.exit()   
                                   
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.cursor.colliderect(self.btnRegresar.rect):
                        self.tablero.sonido2.stop()
                        self.audio.stop()
                        self.terminar = True
                        self.tablero.sonido.play(-1)
                        self.tablero.run()
                        
                    if self.cursor.colliderect(self.msjInicio.btn.rect):
                        self.msjInicio.visible = False
                        self.audio.stop()
                        if sonido2Sonando == False:
                            sonido2Sonando = True
                            self.tablero.sonido2.play(-1)
                        self.inicio = False
                        self.juego = True
                    
                    if self.cursor.colliderect(self.msjGanaste.btn.rect):
                        self.msjGanaste.visible = False
                        self.gano = False
                        self.terminar = True
                        # self.cita.run()
                        self.tablero.sonido2.stop()
                        self.tablero.pasoCuentoNoViolencia = True
                        self.tablero.compartir.run("NoViolencia","Juego")
                    
                        
                    self.mouse.rect.center = pygame.mouse.get_pos()
                           
                    piexas = pygame.sprite.spritecollide(self.mouse, self.piezas, False)
                    
                    #===========================================================
                    # if self.gano and pygame.sprite.collide_rect(self.botonTerminar, self.mouse):
                    #     self.gano = False
                    #     self.terminar = True
                    #     # self.cita.run()
                    #     self.tablero.sonido2.stop()
                    #     self.tablero.pasoCuentoNoViolencia = True
                    #     self.tablero.compartir.run("NoViolencia","Juego")
                    #     #self.tablero.sonido.play(-1)
                    #     #self.tablero.run()
                    #===========================================================
                    if self.juego and len(piexas) > 0:
                        for m in piexas:
                            if self.seleccionada is not None:
                                center = self.seleccionada.rect.center 
                                x2 = self.seleccionada.x
                                y2 = self.seleccionada.y
                                self.seleccionada.rect.center = m.rect.center
                                self.seleccionada.x = m.x
                                self.seleccionada.y = m.y
                                m.rect.center = center
                                m.x = x2
                                m.y = y2
                                self.seleccionada = None
                                if self.chequeo():
                                    self.juego = False
                                    self.gano = True    
                                        
                                break
                            else:
                                m.estaSeleccionada = True
                                self.seleccionada = m
                                break
                            
                    #===========================================================
                    # elif self.inicio and pygame.sprite.collide_rect(self.botonContinuar, self.mouse):
                    #     self.inicio = False
                    #     self.juego = True
                    #===========================================================
                            
            self.screen.fill((255, 255, 255))                    
            self.screen.blit(self.background, (0, 0))
            self.piezas.draw(self.screen)
            self.cursor.update()
            
            pygame.draw.line(self.screen, (255, 255, 255), (140, 100 - 3), (140 + 945 - 2, 100 - 3), 5)  # arriba
            pygame.draw.line(self.screen, (255, 255, 255), (140 - 3, 95), (140 - 3, 105 + 645 - 6), 5)  # izquierda
            pygame.draw.line(self.screen, (255, 255, 255), (140, 105 + 645 - 8), (140 + 945 - 2, 105 + 645 - 8), 5)  # abajo
            pygame.draw.line(self.screen, (255, 255, 255), (140 + 945 - 3, 105 + 645 - 7), (140 + 945 - 3, 105 - 10), 5)  # derecha
            
            pygame.draw.line(self.screen, (255, 255, 255), ((140 - 4) + (945 / 3), 95), ((140 - 4) + (945 / 3), 105 + 645 - 7), 5)
            pygame.draw.line(self.screen, (255, 255, 255), ((140 - 4) + 2 * (945 / 3), 95), ((140 - 4) + 2 * (945 / 3), 105 + 645 - 7), 5)
            
            pygame.draw.line(self.screen, (255, 255, 255), (140, (100 - 4) + (645 / 3)), (140 + 945 - 2, (100 - 4) + (645 / 3)), 5)  # horizontal
            pygame.draw.line(self.screen, (255, 255, 255), (140, (100 - 4) + 2 * (645 / 3)), (140 + 945 - 2, (100 - 4) + 2 * (645 / 3)), 5)  # horizontal
            
            for y in range(3):
                for x in range(3):
                    
                    pygame.draw.rect(self.screen, (255, 255, 255), (x * (945 / 3) + 140, y * (645 / 3) + 100, 945 / 3 - 3, 645 / 3 - 3), 5)
           
            if(self.seleccionada is not None):
                pygame.draw.rect(self.screen, (0, 0, 0), (self.seleccionada.x * (945 / 3) + 140, self.seleccionada.y * (645 / 3) + 100, 945 / 3 - 3, 645 / 3 - 3), 5)
            
            
            self.msjInicio.update(self.screen, self.cursor)
            self.msjGanaste.update(self.screen, self.cursor)

                
            
            if self.inicio:
                self.msjInicio.visible = True
                self.btnRegresar.update(self.screen, self.cursor)
                #===============================================================
                # self.screen.blit(self.transparente, (0, 0))
                # self.btnRegresar.update(self.screen, self.cursor)
                # self.screen.blit(self.instrucciones, (86, 100))
                # self.botonContinuar.rect.center = (600, 450)
                # self.screen.blit(self.botonContinuar.image, self.botonContinuar.rect)
                #===============================================================
            
            elif self.juego:
                self.btnRegresar.update(self.screen, self.cursor)
                # pass
                
            elif self.gano:
                
                if(self.unaVez):
                    pygame.display.update()
                    pygame.time.wait(1000)
                    self.unaVez = False
                
                if pasoSonidoExito == False:
                    self.tablero.sonidoExito.play()
                    pasoSonidoExito = True
                    
                self.msjGanaste.visible = True
                    
                #===============================================================
                # self.screen.blit(self.transparente, (0, 0))
                # self.screen.blit(self.letrero, (380, 100))
                # self.screen.blit(self.botonTerminar.image, self.botonTerminar.rect)
                #===============================================================
            
            
            
            pygame.display.update()
            self.clock.tick(60)
            
                
