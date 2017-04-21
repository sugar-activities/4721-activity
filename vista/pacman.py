#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, os, datetime
from modelo import Personaje, moneda, bloque, nivel, monstruo1, monstruo2, monstruo3, Cursor, Boton, MensajeEmergente
from control import Servicios, resource
from pygame.locals import *
class Pacman(object):
    
    BLOCK_SIZE = 40
    
    def __init__(self, cursor, screen, clock, padre):
        self.cursor = cursor
        bif = os.path.join("imagenes", "verdad")
        resource.set_images_path(bif)
        self.background = resource.get_image("fondoPacman.png",False)
        
        self.estrella = resource.get_image("star.png",False)
        
        self.screen = screen
        self.clock = clock
        
        self.tablero = padre
        
        self.audio = Servicios.cargarSonido("verdad.ogg", os.path.join("audios", "cuentos"))
        
        self.inicioPoderoso = None
        
        # self.cita = fraseVerdad.FraseVerdad(self.screen, self.clock, self.cursor, self.tablero)
        
        self.mouse = Cursor.Mouse()
        #self.botonReintentar = Boton.BotonReintentar()
        #self.botonContinuar = Boton.BotonContinuar()
        #self.botonTerminar = Boton.BotonTerminar()
        
        self.msjInicio = MensajeEmergente.MensajeInicial(30, "CuentoVerdad")
        self.msjGanaste = MensajeEmergente.MensajeGanaste(28, "JuegoVerdad")
        self.msjPerdiste = MensajeEmergente.MensajePerdiste(28, "JuegoVerdad")
        
        # self.instrucciones = pygame.image.load(os.path.join("imagenes", "verdad", "inicioVerdad.png")).convert_alpha()
        # self.letrero = pygame.image.load(os.path.join("imagenes", "verdad", "ganastePacman.png")).convert_alpha()
        #self.letreroReintento = resource.get_image("perdistePacman.png")).convert_alpha()
  
        self.inicio = True
        self.juego = False
        self.terminar = False
        self.gano = False
        self.perdio = False
        self.numMonedas = 0
        
        self.personaje = Personaje.PersonajePacman((0,0),self.tablero.personaje.sexo)
        
        self.loadSprites();
        
        
        self.monstruos = pygame.sprite.Group()
        monstruo1V = monstruo1.Monstruo1()
        self.monstruos.add(monstruo1V)
        monstruo2V = monstruo2.Monstruo2()
        self.monstruos.add(monstruo2V)
        monstruo3V = monstruo3.Monstruo3()
        self.monstruos.add(monstruo3V)
        
        self.bloques.draw(self.background)
        
        resource.set_images_path(os.path.join("imagenes"))
        imgBtnRegresar = resource.get_image("boton_regresar.png")
        imgBtnRegresarSelec = resource.get_image("boton_regresar_selec.png")
        
        self.btnRegresar = Boton.Boton(imgBtnRegresar, imgBtnRegresarSelec, (1200 - 214 - 10), 10)
        
        
        
        
        
    def reiniciar(self):
        self.inicio = True
        self.juego = False
        self.terminar = False
        self.gano = False
        self.perdio = False
        self.numMonedas = 0
        
        self.monstruos.empty()
            
        monstruo1V = monstruo1.Monstruo1()
        self.monstruos.add(monstruo1V)
        monstruo2V = monstruo2.Monstruo2()
        self.monstruos.add(monstruo2V)
        monstruo3V = monstruo3.Monstruo3()
        self.monstruos.add(monstruo3V)
            
        self.monedas.empty()
        self.personajes.empty()
        
        self.loadSprites()
    
    def loadSprites(self):
        """Load all of the sprites that we need"""
        """calculate the center point offset"""
        x_offset = (Pacman.BLOCK_SIZE / 2)
        y_offset = (Pacman.BLOCK_SIZE / 2)
        """Load the level"""        
        level = nivel.Nivel()
        layout = level.getLayout()
        img_list = level.getSprites()
        
        """Create the Pellet group"""
        self.monedas = pygame.sprite.Group()
        """Create the block group"""
        self.bloques = pygame.sprite.Group()
        
        for y in range(len(layout)):
            for x in range(len(layout[y])):
                """Get the center point for the rects"""
                centerPoint = [(x * Pacman.BLOCK_SIZE) + x_offset + 172.8, (y * Pacman.BLOCK_SIZE + y_offset) + 37.3]
                if layout[y][x] == level.BLOQUE:
                    block = bloque.Bloque(img_list[level.BLOQUE], centerPoint)
                    self.bloques.add(block)
                elif layout[y][x] == level.PERSONAJE:
                    self.personaje.rect.center = centerPoint
                    pellet = moneda.Moneda(img_list[level.MONEDA], centerPoint, False, False)
                    pellet.image = pellet.image2
                    pellet.comida = True
                    self.monedas.add(pellet)
                elif layout[y][x] == level.MONEDA:
                    pellet = moneda.Moneda(img_list[level.MONEDA], centerPoint, False, False)
                    self.monedas.add(pellet) 
                    self.numMonedas += 1
                elif layout[y][x] == level.INTERSECCION:
                    pellet = moneda.Moneda(img_list[level.MONEDA], centerPoint, True, False)
                    self.monedas.add(pellet) 
                    self.numMonedas += 1
                elif layout[y][x] == level.SUPER:
                    pellet = moneda.Moneda(img_list[level.MONEDA], centerPoint, False, True)
                    self.monedas.add(pellet) 
                    #self.numMonedas += 1
        self.personajes = pygame.sprite.RenderPlain((self.personaje))
    
    def run(self):
        
        # pygame.mouse.set_visible(True)
        
        self.reiniciar()
        
        pasoSonidoExito = False
        
        terminar = False
        
        self.audio.play()
        
        
        while not terminar:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == KEYDOWN:
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        self.personaje.MoveKeyDown(event.key)
                elif event.type == KEYUP:
                    keys = pygame.key.get_pressed()
                    if (event.key == K_RIGHT and not keys[K_RIGHT]):
                        self.personaje.MoveKeyUp(event.key)
                    elif (event.key == K_LEFT and not keys[K_LEFT]):
                        self.personaje.MoveKeyUp(event.key)
                    elif (event.key == K_UP and not keys[K_UP]):
                        self.personaje.MoveKeyUp(event.key)
                    elif (event.key == K_DOWN and not keys[K_DOWN]):
                        self.personaje.MoveKeyUp(event.key)
                        
                    if self.personaje.xMove == 0 and self.personaje.yMove == 0 and keys[K_RIGHT] and not keys[K_LEFT] and not keys[K_UP] and not keys[K_DOWN] :
                        self.personaje.MoveKeyDown(K_RIGHT)
                    elif self.personaje.xMove == 0 and self.personaje.yMove == 0 and keys[K_LEFT] and not keys[K_RIGHT] and not keys[K_UP] and not keys[K_DOWN] :
                        self.personaje.MoveKeyDown(K_LEFT)
                    elif self.personaje.xMove == 0 and self.personaje.yMove == 0 and keys[K_UP] and not keys[K_LEFT] and not keys[K_RIGHT] and not keys[K_DOWN] :
                        self.personaje.MoveKeyDown(K_UP)
                    elif self.personaje.xMove == 0 and self.personaje.yMove == 0 and keys[K_DOWN] and not keys[K_LEFT] and not keys[K_UP] and not keys[K_RIGHT] :
                        self.personaje.MoveKeyDown(K_DOWN)
                        
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    
                    if self.cursor.colliderect(self.btnRegresar.rect):
                        self.tablero.sonido2.stop()
                        self.audio.stop()
                        terminar = True
                        self.tablero.sonido.play(-1)
                        self.tablero.run()
                        
                    if self.cursor.colliderect(self.msjInicio.btn.rect) and self.inicio:
                        self.msjInicio.visible = False
                        self.audio.stop()
                        self.tablero.sonido2.play(-1)
                        self.inicio = False
                        self.juego = True
                    
                    if self.cursor.colliderect(self.msjGanaste.btn.rect) and self.gano:
                        self.msjGanaste.visible = False
                        self.gano = False
                        terminar = True
                        # self.cita.run()
                        self.tablero.sonido2.stop()
                        self.tablero.pasoCuentoVerdad = True
                        self.tablero.compartir.run("Verdad", "Juego")
                        
                    if self.cursor.colliderect(self.msjPerdiste.btn.rect) and self.perdio:
                        self.msjPerdiste.visible = False
                        self.reiniciar()
                    
                    self.mouse.rect.center = pygame.mouse.get_pos()
                    
                    #===========================================================
                    # if self.gano and pygame.sprite.collide_rect(self.botonTerminar, self.mouse):
                    #     self.gano = False
                    #     terminar = True
                    #     #self.cita.run()
                    #     self.tablero.sonido2.stop()
                    #     self.tablero.pasoCuentoVerdad = True
                    #     self.tablero.compartir.run("Verdad","Juego")
                    #===========================================================
                        # self.tablero.sonido.play(-1)
                        # self.tablero.run()
                    #===========================================================
                    # if self.perdio:
                    #    if pygame.sprite.collide_rect(self.botonReintentar, self.mouse):
                    #        self.reiniciar()
                    #===========================================================
                            
                    #===========================================================
                    # if self.inicio and pygame.sprite.collide_rect(self.botonContinuar, self.mouse):
                    #     self.inicio = False
                    #     self.juego = True
                    #===========================================================
            
            self.screen.fill((255, 255, 255))                    
            self.screen.blit(self.background, (0, 0))
            self.cursor.update()
            
            
            
            if self.inicio:
                self.msjInicio.visible = True
                #self.btnRegresar.update(self.screen, self.cursor)
                #===============================================================
                # self.monedas.draw(self.screen)
                # self.monstruos.draw(self.screen)
                # self.personajes.draw(self.screen)
                # self.screen.blit(self.transparente, (0, 0))
                # self.btnRegresar.update(self.screen, self.cursor)
                # self.screen.blit(self.instrucciones, (86, 100))
                # self.botonContinuar.rect.center = (600, 450)
                # self.screen.blit(self.botonContinuar.image, self.botonContinuar.rect)
                #===============================================================
            
            elif self.juego:
                #self.btnRegresar.update(self.screen, self.cursor)
                self.personajes.update(self.bloques)
                self.monstruos.update(self.bloques, self.monedas)  
                self.monedas.update()      
                
                
                
                lstCols = pygame.sprite.spritecollide(self.personaje, self.monedas, False)
    
                for m in lstCols:
    
                    distancia = abs(m.rect.centerx - self.personaje.rect.centerx)
                    distancia2 = abs(m.rect.centery - self.personaje.rect.centery)
                    
                    if (distancia2 < 14 and distancia2 > 1) and (self.personaje.xMove == 4 or self.personaje.xMove == -4):
                        self.personaje.rect.centery = m.rect.centery
                    elif (distancia < 14 and distancia > 1) and (self.personaje.yMove == 4 or self.personaje.yMove == -4):
                        self.personaje.rect.centerx = m.rect.centerx
                        
                    if (distancia < 5) and (self.personaje.xMove == 4 or self.personaje.xMove == -4):
                        if not m.comida:
                            m.image = m.image2
                            m.comida = True
                            if m.poderosa:
                                self.personaje.poderoso = True
                                self.inicioPoderoso = datetime.datetime.now()
                                m.startTime = datetime.datetime.now()
                            else:
                                self.numMonedas -= 1
                    elif (distancia2 < 5) and (self.personaje.yMove == 4 or self.personaje.yMove == -4):
                        if not m.comida:
                            m.image = m.image2
                            m.comida = True
                                
                            if m.poderosa:
                                self.personaje.poderoso = True
                                self.inicioPoderoso = datetime.datetime.now()
                                m.startTime = datetime.datetime.now()
                            else:
                                self.numMonedas -= 1
                
                if pygame.sprite.spritecollideany(self.personaje, self.monstruos):
                    if not self.personaje.poderoso:
                        self.juego = False
                        self.perdio = True  # perdio
                    else:
                        pygame.sprite.spritecollide(self.personaje, self.monstruos, True)
                      
                self.monedas.draw(self.screen)
                self.monstruos.draw(self.screen)
                self.personajes.draw(self.screen)
                    
                if self.personaje.poderoso:
                    endtime = datetime.datetime.now()
                    self.screen.blit(self.estrella, self.personaje.rect.center)
                    if(endtime-self.inicioPoderoso).total_seconds() >= 5:
                        self.personaje.poderoso = False
                        print("Ya no soy poderoso")
            
                if (self.numMonedas == 0) and (len(self.monstruos) == 0):
                    self.juego = False
                    self.gano = True
                
            elif self.gano:
                self.monedas.draw(self.screen)
                self.monstruos.draw(self.screen)
                self.personajes.draw(self.screen)
                
                if pasoSonidoExito == False:
                    self.tablero.sonidoExito.play()
                    pasoSonidoExito = True
                
                self.msjGanaste.visible = True
                #===============================================================
                # self.screen.blit(self.transparente, (0, 0))
                # self.screen.blit(self.letrero, (380, 100))
                # self.screen.blit(self.botonTerminar.image, self.botonTerminar.rect)
                #===============================================================
            
            elif self.perdio:
                self.monedas.draw(self.screen)
                self.monstruos.draw(self.screen)
                self.personajes.draw(self.screen)
                if self.msjPerdiste.visible == False:
                    self.msjPerdiste.visible = True
                #===============================================================
                # self.screen.blit(self.transparente, (0, 0))
                # self.screen.blit(self.letreroReintento, (380, 100))  # mirar coordenadas
                # self.screen.blit(self.botonReintentar.image, self.botonReintentar.rect)
                #===============================================================
            
            self.msjInicio.update(self.screen, self.cursor)
            self.msjGanaste.update(self.screen, self.cursor)
            self.msjPerdiste.update(self.screen, self.cursor)
            self.btnRegresar.update(self.screen, self.cursor)
               
            pygame.display.update()
            self.clock.tick(60)
