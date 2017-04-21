#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, os, sys
from control import Servicios
from modelo import Monstruo, Boton, Cursor, MensajeEmergente
from pygame.locals import *

class Amor(object):

    def __init__(self, cursor, screen, clock, padre):
        self.dirImagenes = os.path.join("imagenes", "amor")
        self.cursor = cursor
        self.screen = screen
        self.clock = clock
        self.tablero = padre
        
        self.audio = Servicios.cargarSonido("amor.ogg", os.path.join("audios", "cuentos"))
        
        # self.cita = fraseAmor.FraseAmor(self.screen, self.clock, self.cursor, self.tablero)
        
        # self.botonContinuar = Boton.BotonContinuar()
        # self.botonTerminar = Boton.BotonTerminar()
        
        # self.instrucciones = pygame.image.load(os.path.join("imagenes", "amor", "inicioAmor.png")).convert_alpha()
        # self.letrero = pygame.image.load(os.path.join("imagenes", "amor", "ganaste.png")).convert_alpha()
        # self.letreroReintento = pygame.image.load(os.path.join("imagenes", "amor", "perdiste.png")).convert_alpha()
        # self.transparente = pygame.image.load(os.path.join("imagenes", "verdad", "transparente.png")).convert_alpha()
        
        self.msjInicio = MensajeEmergente.MensajeInicial(40, "CuentoAmor")
        self.msjGanaste = MensajeEmergente.MensajeGanaste(28, "JuegoAmor")
        self.msjPerdiste = MensajeEmergente.MensajePerdiste(28, "JuegoAmor")
        
        #self.mouse = Cursor.Mouse()
        
        self.nivel = 1
        
        self.personaje = self.tablero.personaje
        
        self.fuente1 = pygame.font.Font(None, 24)
        self.texto1 = self.fuente1.render(" Perdiste, intenta de nuevo", 0, (255, 230, 245), (50, 50, 50))
        
        self.fondo = Servicios.cargarImagen("fondo_amor.png", self.dirImagenes)
        self.gano = False
        
        imgBtnRegresar = Servicios.cargarImagen("boton_regresar.png", "imagenes")
        imgBtnRegresarSelec = Servicios.cargarImagen("boton_regresar_selec.png", "imagenes")
        
        self.btnRegresar = Boton.Boton(imgBtnRegresar, imgBtnRegresarSelec, (1200 - 214 - 10), 10)
            
    
    def run(self):
        
        # pygame.mouse.set_visible(True)
        
        inicio = True
        juego = False
        gano = False
        
        
        pasoSonidoExito = False
        
        objetosN1 = Servicios.cargarImagen("nivel1.png", self.dirImagenes)
        objetosN2 = Servicios.cargarImagen("nivel2.png", self.dirImagenes)
        objetosN3 = Servicios.cargarImagen("nivel3.png", self.dirImagenes)
        
        self.gano = False
        self.nivel = 1
        
        self.personaje = self.tablero.personaje
        
        monstruoN11 = Monstruo.Monstruo(280, 0, 100, 1)
        monstruoN12 = Monstruo.Monstruo(680, 0, 100, 1)
        
        monstruoN21 = Monstruo.Monstruo(128 * 2, 0, 100, 2)
        monstruoN22 = Monstruo.Monstruo(256 * 2, 0, 100, 2)
        monstruoN23 = Monstruo.Monstruo(384 * 2, 0, 100, 2)
        monstruoN24 = Monstruo.Monstruo(512 * 2, 0, 100, 2)
        
        monstruoN31 = Monstruo.Monstruo(91 * 2, 0, 100, 3)
        monstruoN32 = Monstruo.Monstruo(183 * 2, 0, 100, 3)
        monstruoN33 = Monstruo.Monstruo(274 * 2, 0, 100, 3)
        monstruoN34 = Monstruo.Monstruo(366 * 2, 0, 100, 3)
        monstruoN35 = Monstruo.Monstruo(457 * 2, 0, 100, 3)
        monstruoN36 = Monstruo.Monstruo(548 * 2, 0, 100, 3)
        
        velocidad = 8
        
        anchoN1 = 80
        xN1 = -anchoN1
        yN1 = 252
        
        anchoN2 = 137
        xN2 = -anchoN1
        yN2 = 283
        
        anchoN3 = 185
        xN3 = -anchoN1
        yN3 = 301
        
        self.personaje.setAncho(anchoN1)
        self.personaje.setX(xN1)
        self.personaje.setY(yN1)
        
        
        
        self.audio.play()
        
        while self.gano == False:
            
            #-------Eventos-------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    
                    if self.cursor.colliderect(self.btnRegresar.rect):
                        self.tablero.sonido2.stop()
                        self.audio.stop()
                        self.gano = True
                        self.tablero.sonido.play(-1)
                        self.tablero.run()
                        
                    if self.cursor.colliderect(self.msjInicio.btn.rect):
                        self.msjInicio.visible = False
                        self.audio.stop()
                        self.tablero.sonido2.play(-1)
                        inicio = False
                        juego = True
                    
                    if self.cursor.colliderect(self.msjGanaste.btn.rect):
                        self.msjGanaste.visible = False
                        self.tablero.sonido2.stop()
                        self.gano = True
                        self.tablero.pasoCuentoAmor = True
                        # self.tablero.sonido.play(-1)
                        self.tablero.compartir.run("Amor", "Juego")
                        
                    if self.cursor.colliderect(self.msjPerdiste.btn.rect):
                        self.msjPerdiste.visible = False
                    
                    #===========================================================
                    # self.mouse.rect.center = pygame.mouse.get_pos()
                    #     
                    # if gano and pygame.sprite.collide_rect(self.botonTerminar, self.mouse):
                    #         self.tablero.sonido2.stop()
                    #         self.gano = True
                    #         self.tablero.pasoCuentoAmor = True
                    #         # self.tablero.sonido.play(-1)
                    #         self.tablero.compartir.run("Amor", "Juego")
                    #===========================================================
                            
                            # self.tablero.run()
                        
                    #===========================================================
                    # if inicio and pygame.sprite.collide_rect(self.botonContinuar, self.mouse):
                    #         inicio = False
                    #         juego = True
                    #===========================================================
                    
                    if self.cursor.colliderect(monstruoN11.rect):
                        monstruoN11.convertir()
                        # monstruoN11.rect.left, monstruoN11.rect.top = (0, 0)
                    if self.cursor.colliderect(monstruoN12.rect):
                        monstruoN12.convertir()
                        # monstruoN12.rect.left, monstruoN12.rect.top = (0, 0)
                        
                    if self.cursor.colliderect(monstruoN21.rect):
                        monstruoN21.convertir()
                        # monstruoN21.rect.left, monstruoN21.rect.top = (0, 0)
                    if self.cursor.colliderect(monstruoN22.rect):
                        monstruoN22.convertir()
                        # monstruoN22.rect.left, monstruoN22.rect.top = (0, 0)
                    if self.cursor.colliderect(monstruoN23.rect):
                        monstruoN23.convertir()
                        # monstruoN23.rect.left, monstruoN23.rect.top = (0, 0)
                    if self.cursor.colliderect(monstruoN24.rect):
                        monstruoN24.convertir()
                        # monstruoN24.rect.left, monstruoN24.rect.top = (0, 0)
                        
                    if self.cursor.colliderect(monstruoN31.rect):
                        monstruoN31.convertir()
                        # monstruoN31.rect.left, monstruoN31.rect.top = (0, 0)
                    if self.cursor.colliderect(monstruoN32.rect):
                        monstruoN32.convertir()
                        # monstruoN32.rect.left, monstruoN32.rect.top = (0, 0)
                    if self.cursor.colliderect(monstruoN33.rect):
                        monstruoN33.convertir()
                        # monstruoN33.rect.left, monstruoN33.rect.top = (0, 0)
                    if self.cursor.colliderect(monstruoN34.rect):
                        monstruoN34.convertir()
                        # monstruoN34.rect.left, monstruoN34.rect.top = (0, 0)
                    if self.cursor.colliderect(monstruoN35.rect):
                        monstruoN35.convertir()
                        # monstruoN35.rect.left, monstruoN35.rect.top = (0, 0)
                    if self.cursor.colliderect(monstruoN36.rect):
                        monstruoN36.convertir()
                        # monstruoN36.rect.left, monstruoN36.rect.top = (0, 0)

            self.clock.tick(60)
            
            self.cursor.update()
            
            self.screen.blit(self.fondo, (0, 0))
            
            self.msjInicio.update(self.screen, self.cursor)
            self.msjGanaste.update(self.screen, self.cursor)
            self.msjPerdiste.update(self.screen, self.cursor)
            self.btnRegresar.update(self.screen, self.cursor)
            
            if inicio:
                self.msjInicio.visible = True
                
                #===============================================================
                # self.screen.blit(self.transparente, (0, 0))
                # self.btnRegresar.update(self.screen, self.cursor)
                # 
                # self.screen.blit(self.instrucciones, (600 - 425, 100))
                # self.botonContinuar.rect.center = (600, 590)
                # self.screen.blit(self.botonContinuar.image, self.botonContinuar.rect)
                #===============================================================
            
            elif juego and self.msjPerdiste.visible == False:
            
                self.personaje.dibujarMov(self.screen, "der")
                
                if self.nivel == 1:

                    self.screen.blit(objetosN1, (0, 0))
                    
                    # aparece monstruo gradualmente
                    if(self.personaje.getX() > 20):
                        monstruoN11.dibujar(self.screen, self.personaje, velocidad)
                        
                    if(self.personaje.getX() > 400):
                        monstruoN12.dibujar(self.screen, self.personaje, velocidad)
                    
                    # GANO
                    if(self.personaje.getX() > 1200):
                        pygame.display.update()
                        pygame.time.delay(2000)
                        # incrementar el nivel
                        self.nivel = 2
                        self.personaje.setAncho(anchoN2)
                        self.personaje.setX(xN2)
                        self.personaje.setY(yN2)
                        monstruoN21 = Monstruo.Monstruo(128, 0, 85, 2)
                        monstruoN22 = Monstruo.Monstruo(256, 0, 85, 2)
                        monstruoN23 = Monstruo.Monstruo(384, 0, 85, 2)
                        monstruoN24 = Monstruo.Monstruo(512, 0, 85, 2)
                    
                    # PERDIO
                    if (self.personaje.rect.colliderect(monstruoN11.rect) and monstruoN11.vivo) or (self.personaje.rect.colliderect(monstruoN12.rect) and monstruoN12.vivo):
                        self.screen.blit(self.texto1, (550, 390))
                        # pygame.display.update()
                        # pygame.time.delay(4000)
                        self.msjPerdiste.visible = True
                        monstruoN11 = Monstruo.Monstruo(213, 0, 75, 1)
                        monstruoN12 = Monstruo.Monstruo(427, 0, 75, 1)
                        self.personaje.setX(xN1)
                        self.personaje.setY(yN1)
                    
                    self.personaje.setX(self.personaje.x + velocidad)
                    
                
                if self.nivel == 2:
                    
                    self.screen.blit(objetosN2, (0, 0))
                    
                    # aparece monstruo gradualmente
                    if(self.personaje.getX() > 20):
                        monstruoN21.dibujar(self.screen, self.personaje, velocidad)
                        
                    if(self.personaje.getX() > 120):
                        monstruoN22.dibujar(self.screen, self.personaje, velocidad)
                    
                    if(self.personaje.getX() > 220):
                        monstruoN23.dibujar(self.screen, self.personaje, velocidad)
                        
                    if(self.personaje.getX() > 400):
                        monstruoN24.dibujar(self.screen, self.personaje, velocidad)
                    
                    # GANO
                    if(self.personaje.getX() > 1200):
                        pygame.display.update()
                        pygame.time.delay(2000)
                        # incrementar el nivel
                        self.nivel = 3
                        self.personaje.setAncho(anchoN3)
                        self.personaje.setX(xN3)
                        self.personaje.setY(yN3)
                        monstruoN31 = Monstruo.Monstruo(91, 0, 85, 3)
                        monstruoN32 = Monstruo.Monstruo(183, 0, 85, 3)
                        monstruoN33 = Monstruo.Monstruo(274, 0, 85, 3)
                        monstruoN34 = Monstruo.Monstruo(366, 0, 85, 3)
                        monstruoN35 = Monstruo.Monstruo(457, 0, 85, 3)
                        monstruoN36 = Monstruo.Monstruo(548, 0, 85, 3)
                    
                    # PERDIO
                    if (self.personaje.rect.colliderect(monstruoN21.rect) and monstruoN21.vivo) or (self.personaje.rect.colliderect(monstruoN22.rect) and monstruoN22.vivo) or (self.personaje.rect.colliderect(monstruoN23.rect) and monstruoN23.vivo) or (self.personaje.rect.colliderect(monstruoN24.rect) and monstruoN24.vivo):
                        self.screen.blit(self.texto1, (550, 390))
                        #pygame.display.update()
                        #pygame.time.delay(4000)
                        self.msjPerdiste.visible = True
                        monstruoN21 = Monstruo.Monstruo(128, 0, 85, 2)
                        monstruoN22 = Monstruo.Monstruo(256, 0, 85, 2)
                        monstruoN23 = Monstruo.Monstruo(384, 0, 85, 2)
                        monstruoN24 = Monstruo.Monstruo(512, 0, 85, 2)
                        self.personaje.setX(xN2)
                        self.personaje.setY(yN2)
                    
                    self.personaje.setX(self.personaje.x + velocidad)
                    
                
                if self.nivel == 3:
                    
                    self.screen.blit(objetosN3, (0, 0))
                    
                    # aparece monstruo gradualmente
                    if(self.personaje.getX() > 20):
                        monstruoN31.dibujar(self.screen, self.personaje, velocidad)
                        
                    if(self.personaje.getX() > 120):
                        monstruoN32.dibujar(self.screen, self.personaje, velocidad)
                    
                    if(self.personaje.getX() > 220):
                        monstruoN33.dibujar(self.screen, self.personaje, velocidad)
                        
                    if(self.personaje.getX() > 400):
                        monstruoN34.dibujar(self.screen, self.personaje, velocidad)
                        
                    if(self.personaje.getX() > 500):
                        monstruoN35.dibujar(self.screen, self.personaje, velocidad)
                        
                    if(self.personaje.getX() > 600):
                        monstruoN36.dibujar(self.screen, self.personaje, velocidad)
                    
                    # GANO
                    if(self.personaje.getX() > 1200):
                        
                        pygame.display.update()
                        pygame.time.delay(2000)
                        gano = True
                        juego = False
                    
                    # PERDIO
                    if (self.personaje.rect.colliderect(monstruoN31.rect) and monstruoN31.vivo) or (self.personaje.rect.colliderect(monstruoN32.rect) and monstruoN32.vivo) or (self.personaje.rect.colliderect(monstruoN33.rect) and monstruoN33.vivo) or (self.personaje.rect.colliderect(monstruoN34.rect) and monstruoN34.vivo) or (self.personaje.rect.colliderect(monstruoN35.rect) and monstruoN35.vivo) or (self.personaje.rect.colliderect(monstruoN36.rect) and monstruoN36.vivo):
                        
                        self.screen.blit(self.texto1, (550, 390))
                        #pygame.display.update()
                        #pygame.time.delay(4000)
                        self.msjPerdiste.visible = True
                        monstruoN31 = Monstruo.Monstruo(91, 0, 85, 3)
                        monstruoN32 = Monstruo.Monstruo(183, 0, 85, 3)
                        monstruoN33 = Monstruo.Monstruo(274, 0, 85, 3)
                        monstruoN34 = Monstruo.Monstruo(366, 0, 85, 3)
                        monstruoN35 = Monstruo.Monstruo(457, 0, 85, 3)
                        monstruoN36 = Monstruo.Monstruo(548, 0, 85, 3)
                        self.personaje.setX(xN3)
                        self.personaje.setY(yN3)
                    
                    self.personaje.setX(self.personaje.x + velocidad)
            
            elif gano:
                
                if pasoSonidoExito == False:
                    self.tablero.sonidoExito.play()
                    pasoSonidoExito = True
                
                self.msjGanaste.visible = True   
                # self.screen.blit(self.transparente, (0, 0))
                # self.screen.blit(self.letrero, (380, 100))
                # self.screen.blit(self.botonTerminar.image, self.botonTerminar.rect)
                
            pygame.display.flip()
            
