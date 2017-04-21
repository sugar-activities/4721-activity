#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, datetime, os
from modelo import piedraFactory, Boton, Cursor, MensajeEmergente, nivel, bloque
from control import Servicios, resource
from random import randint
from pygame.locals import *
class Cita(object):
    
    BLOCK_SIZE = 80
    
    def __init__(self, screen, clock, cursor, tipo, padre):
        
        # nuevo
        resource.set_images_path(os.path.join("imagenes"))
        self.transparente = resource.get_image("transparente.png")
        resource.set_images_path(os.path.join("imagenes", "citas"))
        self.inicio2 = resource.get_image("Bot_inicio_selec.png")
        self.fin2 = resource.get_image("Bot_fin_selec.png")
        self.background = resource.get_image("Fondo_lago.jpg",False)
        
        self.screen = screen
        self.clock = clock
        self.cursor = cursor
        self.mouse = Cursor.Mouse()
        self.tipo = tipo
        self.tablero = padre
        
        #Botones
        imgBtnLimpiar = resource.get_image("Bot_limpiar.png")
        imgBtnLimpiarSelect = resource.get_image("Bot_limpiar_selec.png")
        self.botonLimpiar = Boton.Boton(imgBtnLimpiar,imgBtnLimpiarSelect,1200-530,10)
        
        imgBtnRegresar = resource.get_image("boton_regresar.png")
        imgBtnRegresarSelec = resource.get_image("boton_regresar_selec.png")
        self.btnRegresar = Boton.Boton(imgBtnRegresar, imgBtnRegresarSelec, (1200 - 214 - 10), 10)
        
        imgBtnAyuda = resource.get_image("BotonesAyuda.png")
        imgBtnAyudaSelec = resource.get_image("BotonesAyuda_selec.png")
        self.btnAyuda = Boton.Boton(imgBtnAyuda, imgBtnAyudaSelec, (1200 - 600), 10)
        
        
        self.inicio = True
        self.juego = False
        self.terminar = False
        self.gano = False
        
        self.msjInicio = MensajeEmergente.MensajeInicial(40, "Cita")
        
        self.piedraFactory = piedraFactory.PiedraFactory()
        
        #self.instrucciones = pygame.image.load(os.path.join("imagenes", "citas", "inicioFrases.png")).convert_alpha()
        
        # copiar y pegar de aqui pa abajo y despues agregar lo del tablero.run
        
        
        self.level = nivel.Nivel()
        # amor
        if self.tipo == 1:
               
            self.msjGanaste = MensajeEmergente.MensajeGanaste(40, "CitaAmor")
            #self.letrero = pygame.image.load(os.path.join("imagenes", "citas", "letreroAmor.png")).convert_alpha()
            
            self.correcto = [91,76,61,46,31,32,33,34,35,36,37,52,67,82,81,80,79,94,109,124,139,140,141,142,143,144,129,114,99,84,69,54,39,40,41,56,71,86,101,116,131,146,147,148,133,118,103,88,73,58,59,60,75,90,105,120,135]
            self.correcto2 = [91,76,61,46,31,32,33,34,35,36,37,52,67,82,81,80,79,94,109,124,139,140,141,142,143,144,129,114,99,84,69,54,39,40,41,56,71,86,101,116,131,146,147,148,133,118,103,88,73,58,59,60,75,90,105,120,135]
        
        # rectitud    
        if self.tipo == 2:
            self.msjGanaste = MensajeEmergente.MensajeGanaste(40, "CitaRectitud")
            #self.letrero = pygame.image.load(os.path.join("imagenes", "citas", "letreroRectitud.png")).convert_alpha()
            
            self.correcto = [31,46,61,76,91,106,121,136,137,138,139,124,109,94,95,96,97,98,83,68,53,38,39,40,55,70,85,100,115,130,131,132,117,102,87,72,57,42,27,28,29,30,45,60,75,90,105,120]
            self.correcto2 = [31,46,61,76,91,106,121,136,137,138,139,124,109,94,95,96,97,98,83,68,53,38,39,40,55,70,85,100,115,130,131,132,117,102,87,72,57,42,27,28,29,30,45,60,75,90,105,120]
        
        # paz    
        if self.tipo == 3:
            self.msjGanaste = MensajeEmergente.MensajeGanaste(40, "CitaPaz")
            #self.letrero = pygame.image.load(os.path.join("imagenes", "citas", "letreroPaz.png")).convert_alpha()
            
            self.correcto = [121,106,91,92,93,78,63,48,33,34,35,50,65,80,95,96,97,98,113,128,143,144,145,130,115,116,117,132,147,148,149,150,135,120,105]
            self.correcto2 = [121,106,91,92,93,78,63,48,33,34,35,50,65,80,95,96,97,98,113,128,143,144,145,130,115,116,117,132,147,148,149,150,135,120,105]
            
        # verdad    
        if self.tipo == 4:
            self.msjGanaste = MensajeEmergente.MensajeGanaste(40, "CitaVerdad")
            #self.letrero = pygame.image.load(os.path.join("imagenes", "citas", "letreroVerdad.png")).convert_alpha()
            
            self.correcto = [17,18,33,48,63,78,93,94,95,96,97,98,113,128,143,144,145,146,131,116,101,86,71,56,41,26,27,28,43,58,73,88,103,118,119,120,105,90,75]
            self.correcto2 = [17,18,33,48,63,78,93,94,95,96,97,98,113,128,143,144,145,146,131,116,101,86,71,56,41,26,27,28,43,58,73,88,103,118,119,120,105,90,75]
            
        # no violencia    
        if self.tipo == 5:
            self.msjGanaste = MensajeEmergente.MensajeGanaste(40, "CitaNoViolencia")
            #self.letrero = pygame.image.load(os.path.join("imagenes", "citas", "letreroNoViolencia.png")).convert_alpha()
            
            self.correcto = [31,46,61,76,91,106,121,122,123,108,93,78,63,48,49,50,51,66,81,96,111,126,141,142,143,128,113,98,83,84,85,86,101,116,131,146,147,148,133,118,103,88,73,58,43,28,29,30,45,60,75,90,105]
            self.correcto2 = [31,46,61,76,91,106,121,122,123,108,93,78,63,48,49,50,51,66,81,96,111,126,141,142,143,128,113,98,83,84,85,86,101,116,131,146,147,148,133,118,103,88,73,58,43,28,29,30,45,60,75,90,105]
 
        self.correcto.sort(reverse=False)
        self.hundidas = []
        
        self.alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        
        self.rutaFuente = os.path.join("fuentes", "PatrickHand-Regular.ttf")
    
        self.fuente = pygame.font.Font(self.rutaFuente, 40)
            
        self.piedras = pygame.sprite.Group()
        self.bloques = pygame.sprite.Group()
        
        self.cargarPiedras()
        
        # tiempo
        self.starttime = datetime.datetime.now()
        
    
    def ayuda(self):
        
        planta2 = None
        for correcta in self.correcto2:
            encontro = False
            for planta in self.hundidas:
                if planta==correcta:
                    encontro = True
            if not encontro:
                planta2 = correcta
                break
        if planta2 is not None:        
            for piedra in self.piedras:
                if  (piedra.numero) == planta2:
                    piedra.ayuda()
                    break  
                    
        
    def tex(self):
        # self.screen.blit(self.texto1,(79-5,90-5))
        
        for bloque in self.piedras:
            texto = self.fuente.render(bloque.letra, True, (0, 0, 0))
            self.screen.blit(texto, bloque.location)
            
    def reiniciar2(self):
        self.inicio = True
        self.juego = False
        self.terminar = False
        self.gano = False
        self.hundidas = []
        self.piedras.empty()
        self.bloques.empty()
        self.cargarPiedras()
        self.starttime = datetime.datetime.now()
        
    def setTipo(self, tipo):
        self.tipo = tipo
        
        # Amor
        if self.tipo == 1:
               
            self.msjGanaste.tipo = "CitaAmor" 
            #self.letrero = pygame.image.load(os.path.join("imagenes", "citas", "letreroAmor.png")).convert_alpha()
            
            self.correcto = [91,76,61,46,31,32,33,34,35,36,37,52,67,82,81,80,79,94,109,124,139,140,141,142,143,144,129,114,99,84,69,54,39,40,41,56,71,86,101,116,131,146,147,148,133,118,103,88,73,58,59,60,75,90,105,120,135]
            
        
        # rectitud    
        if self.tipo == 2:
            self.msjGanaste.tipo = "CitaRectitud"
            #self.letrero = pygame.image.load(os.path.join("imagenes", "citas", "letreroRectitud.png")).convert_alpha()
            
            self.correcto = [31,46,61,76,91,106,121,136,137,138,139,124,109,94,95,96,97,98,83,68,53,38,39,40,55,70,85,100,115,130,131,132,117,102,87,72,57,42,27,28,29,30,45,60,75,90,105,120]
        
        # paz    
        if self.tipo == 3:
            self.msjGanaste.tipo = "CitaPaz"
            #self.letrero = pygame.image.load(os.path.join("imagenes", "citas", "letreroPaz.png")).convert_alpha()
            
            self.correcto = [121,106,91,92,93,78,63,48,33,34,35,50,65,80,95,96,97,98,113,128,143,144,145,130,115,116,117,132,147,148,149,150,135,120,105]
            
        # verdad    
        if self.tipo == 4:
            self.msjGanaste.tipo = "CitaVerdad"
            #self.letrero = pygame.image.load(os.path.join("imagenes", "citas", "letreroVerdad.png")).convert_alpha()
            
            self.correcto = [17,18,33,48,63,78,93,94,95,96,97,98,113,128,143,144,145,146,131,116,101,86,71,56,41,26,27,28,43,58,73,88,103,118,119,120,105,90,75]
            
        # no violencia    
        if self.tipo == 5:
            self.msjGanaste.tipo = "CitaNoViolencia"
            #self.letrero = pygame.image.load(os.path.join("imagenes", "citas", "letreroNoViolencia.png")).convert_alpha()
            
            self.correcto = [31,46,61,76,91,106,121,122,123,108,93,78,63,48,49,50,51,66,81,96,111,126,141,142,143,128,113,98,83,84,85,86,101,116,131,146,147,148,133,118,103,88,73,58,43,28,29,30,45,60,75,90,105]
 
        self.correcto.sort(reverse=False)
    
    def cargarPiedras(self):
        #AMOR------------------------------------------------------------------------
        if self.tipo == 1:
            layout = self.level.getLayoutCitaAmor()
            
        #RECTITUD------------------------------------------------------------------------
        if self.tipo == 2:
            layout = self.level.getLayoutCitaRectitud()
        
        #PAZ------------------------------------------------------------------------
        if self.tipo == 3:  
            layout = self.level.getLayoutCitaPaz()
            
        #VERDAD------------------------------------------------------------------------
        if self.tipo == 4:
            layout = self.level.getLayoutCitaVerdad()
            
        #NOVIOLENCIA------------------------------------------------------------------------
        if self.tipo == 5:
            layout = self.level.getLayoutCitaNoViolencia()
            
              
        """Load all of the sprites that we need"""
        """calculate the center point offset"""
        x_offset = (Cita.BLOCK_SIZE / 2)
        y_offset = (Cita.BLOCK_SIZE / 2) 
        
        """Create the Pellet group"""
        cont =  0
        for y in range(len(layout)):
            for x in range(len(layout[y])):
                """Get the center point for the rects"""
                cont+=1
                if layout[y][x] == self.level.PLANTA:
                    piedra = self.piedraFactory.getPiedra((x * Cita.BLOCK_SIZE) + x_offset , (y * Cita.BLOCK_SIZE + y_offset), u"" +self.alfabeto[randint(0,26)], cont)
                    self.piedras.add(piedra)
                elif layout[y][x] == self.level.INICIO:
                    bloque2 = bloque.Bloque(self.inicio2,((x * Cita.BLOCK_SIZE) + x_offset , (y * Cita.BLOCK_SIZE + y_offset)))
                    self.bloques.add(bloque2)
                elif layout[y][x] == self.level.FIN:
                    bloque2 = bloque.Bloque(self.fin2,((x * Cita.BLOCK_SIZE) + x_offset , (y * Cita.BLOCK_SIZE + y_offset)))
                    self.bloques.add(bloque2)
                elif layout[y][x] == self.level.NADA:
                    continue
                else:
                    piedra = self.piedraFactory.getPiedra((x * Cita.BLOCK_SIZE) + x_offset , (y * Cita.BLOCK_SIZE + y_offset), u"" + layout[y][x], cont)
                    self.piedras.add(piedra)
                    
            
    def chequeo(self):
        self.hundidas.sort(reverse=False)
        if self.hundidas == self.correcto:
            self.juego = False
            self.gano = True
            return True     
        else: 
            return False
        
    def reset(self):
        for block in self.piedras:
            if block.imagen == 1:
                block.update()
        
        self.hundidas = []
    
    def run(self):
        # noPaso = True
        
        self.reiniciar2()
        self.tablero.sonido2.play(-1)
        
        pasoSonidoExito = False
        
        
        
        while not self.terminar:  # noPaso:
            for event in pygame.event.get():
                    if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                            
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        
                        if self.cursor.colliderect(self.btnRegresar.rect):
                            self.tablero.sonido2.stop()
                            self.terminar = True
                            self.tablero.sonido.play(-1)
                            self.tablero.run()
                        
                        if self.cursor.colliderect(self.msjGanaste.btn.rect) and not self.inicio and self.gano:
                            self.msjGanaste.visible = False
                            self.gano = False
                            self.terminar = True
                            #self.tablero.sonido2.stop()
                            
                            if self.tipo == 1:
                                self.tablero.pasoCitaAmor = True
                                #self.tablero.sonido2.stop()
                                # self.tablero.sonido.play(-1)
                                self.tablero.compartir.run("Amor", "Cita")
                            if self.tipo == 2:
                                self.tablero.pasoCitaRectitud = True
                                #self.tablero.sonido2.stop()
                                # self.tablero.sonido.play(-1)
                                self.tablero.compartir.run("Rectitud", "Cita")
                            if self.tipo == 3:
                                self.tablero.pasoCitaPaz = True
                                #self.tablero.sonido2.stop()
                                # self.tablero.sonido.play(-1)
                                self.tablero.compartir.run("Paz", "Cita")
                            if self.tipo == 4:
                                self.tablero.pasoCitaVerdad = True
                                #self.tablero.sonido2.stop()
                                # self.tablero.sonido.play(-1)
                                self.tablero.compartir.run("Verdad", "Cita")
                            if self.tipo == 5:
                                self.tablero.pasoCitaNoViolencia = True
                                #self.tablero.sonido2.stop()
                                # self.tablero.sonido.play(-1)
                                self.tablero.compartir.run("NoViolencia", "Cita")
                        
                        self.mouse.rect.center = pygame.mouse.get_pos() 
                        
                        '''
                        if self.gano and pygame.sprite.collide_rect(self.botonTerminar, self.mouse):
                            self.gano = False
                            self.terminar = True
                            self.tablero.sonido2.stop()
                            
                            if self.tipo == 1:
                                self.tablero.pasoCitaAmor = True
                                self.tablero.sonido2.stop()
                                # self.tablero.sonido.play(-1)
                                self.tablero.compartir.run("Amor", "Cita")
                            if self.tipo == 2:
                                self.tablero.pasoCitaRectitud = True
                                self.tablero.sonido2.stop()
                                # self.tablero.sonido.play(-1)
                                self.tablero.compartir.run("Rectitud", "Cita")
                            if self.tipo == 3:
                                self.tablero.pasoCitaPaz = True
                                self.tablero.sonido2.stop()
                                # self.tablero.sonido.play(-1)
                                self.tablero.compartir.run("Paz", "Cita")
                            if self.tipo == 4:
                                self.tablero.pasoCitaVerdad = True
                                self.tablero.sonido2.stop()
                                # self.tablero.sonido.play(-1)
                                self.tablero.compartir.run("Verdad", "Cita")
                            if self.tipo == 5:
                                self.tablero.pasoCitaNoViolencia = True
                                self.tablero.sonido2.stop()
                                # self.tablero.sonido.play(-1)
                                self.tablero.compartir.run("NoViolencia", "Cita")
                            '''
                            
                            # self.tablero.run()
                        if self.juego:
                            if pygame.sprite.collide_rect(self.botonLimpiar, self.mouse):
                                self.reset()
                            elif pygame.sprite.collide_rect(self.btnAyuda, self.mouse):
                                self.ayuda()
                            else:
                                blocks_hit_list = pygame.sprite.spritecollide(self.mouse, self.piedras, False)
                                soloUna = True
                                for block in blocks_hit_list:
                                    if soloUna:
                                        soloUna = False
                                        if block.imagen == 0 or block.imagen == 2:
                                            self.hundidas.append(block.numero)   
                                        else:
                                            self.hundidas.remove(block.numero)
                                        block.update()
                                        break
                                    
                        if self.cursor.colliderect(self.msjInicio.btn.rect) and self.inicio:
                            self.msjInicio.visible = False
                            self.inicio = False
                            self.juego = True
                        # if self.inicio and pygame.sprite.collide_rect(self.botonContinuar, self.mouse):
                            # self.inicio = False
                            # self.juego = True
                                
            self.screen.fill((255, 255, 255))                    
            self.screen.blit(self.background, (0, 0))
            self.cursor.update()
            self.piedras.draw(self.screen)
            self.tex()
            self.bloques.draw(self.screen)
            #self.screen.blit(self.inicio2, (0, 0))
            #self.screen.blit(self.fin2, (0, 0))
            
            
            if self.inicio:
                self.msjInicio.visible = True
                self.msjInicio.update(self.screen, self.cursor)
                # self.screen.blit(self.transparente, (0, 0))
                self.btnRegresar.update(self.screen, self.cursor)
                # self.screen.blit(self.instrucciones, (380, 100))
                # self.botonContinuar.rect.center = (600, 680)
                # self.screen.blit(self.botonContinuar.image, self.botonContinuar.rect)
            
            elif self.juego:
                
                self.btnRegresar.update(self.screen, self.cursor)
                self.botonLimpiar.update(self.screen, self.cursor)
                self.btnAyuda.update(self.screen, self.cursor)
                
                self.screen.blit(self.botonLimpiar.imagen_actual, self.botonLimpiar.rect)
                endtime = datetime.datetime.now()
                if (endtime - self.starttime).total_seconds() >= 1:
                    self.starttime = datetime.datetime.now()
                    if self.tipo == 1 and len(self.hundidas) == 57:
                        self.gano = self.chequeo()
                    if self.tipo == 2 and len(self.hundidas) == 48:
                        self.gano = self.chequeo()
                    if self.tipo == 3 and len(self.hundidas) == 35:
                        self.gano = self.chequeo()
                    if self.tipo == 4 and len(self.hundidas) == 39:
                        self.gano = self.chequeo()
                    if self.tipo == 5 and len(self.hundidas) == 53:
                        self.gano = self.chequeo()
            
            elif self.gano:
                if pasoSonidoExito == False:
                    self.tablero.sonidoExito.play()
                    pasoSonidoExito = True
                
                self.msjGanaste.visible = True  
                self.msjGanaste.update(self.screen, self.cursor)  
                #self.screen.blit(self.transparente, (0, 0))
                #self.screen.blit(self.letrero, (380, 100))
                #self.screen.blit(self.botonTerminar.image, self.botonTerminar.rect)   
            
            pygame.display.update()
            self.clock.tick(60)
