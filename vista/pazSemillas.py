#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, random, os
from pygame.locals import *
from control import Servicios
from modelo import semillasFactory, semilla, plantasFactory, planta, Boton, Cursor, MensajeEmergente

class PazSemillas(object):
    
    def __init__(self, cursor, screen, clock, padre):
        
        self.dirImagenes = os.path.join("imagenes", "paz")
        self.tablero = padre
        


        self.semillasFactory = semillasFactory.SemillasFactory()
        self.plantasFactory = plantasFactory.PlantasFactory()
        self.background = Servicios.cargarImagen("fondo_paz.png", self.dirImagenes, False)
        
        # anchoImg = self.tablero.ancho + 47
        # altoImg = anchoImg * self.background.get_height() / self.background.get_width()
        # self.background = pygame.transform.smoothscale(self.background, (anchoImg, altoImg))
        
        self.screen = screen
        self.clock = clock
        self.cursor = cursor
        
        self.audio = Servicios.cargarSonido("paz.ogg", os.path.join("audios", "cuentos"))
        
        # self.cita = frasePaz.FrasePaz(self.screen, self.clock, self.cursor, self.tablero)
        
        #nuevo----------------
        
        self.botonContinuar = Boton.BotonContinuar()
        self.botonTerminar = Boton.BotonTerminar()
        
        self.msjInicio = MensajeEmergente.MensajeInicial(40, "CuentoPaz")
        self.msjGanaste = MensajeEmergente.MensajeGanaste(28, "JuegoPaz")
        
        #self.instrucciones = pygame.image.load(os.path.join("imagenes", "paz", "inicioPaz.png")).convert_alpha()
        #self.letrero = pygame.image.load(os.path.join("imagenes", "paz", "ganaste.png")).convert_alpha()
        #self.letreroReintento = pygame.image.load(os.path.join("imagenes", "paz", "PerdistePaz.png")).convert_alpha()
        #self.transparente = pygame.image.load(os.path.join("imagenes", "transparente.png")).convert_alpha()
        
        
        
        self.mouse = Cursor.Mouse()
        
        
        
        #-------------------------

        self.x = 0
        self.orden = []
        self.texto = True 

        self.fuente1 = pygame.font.Font(None, 24)
        self.texto1 = self.fuente1.render(" Ahora  este lugar esta limpio pero no hay arboles ni flores, por eso vas       ", 0, (255, 230, 245), (50, 50, 50))
        self.texto2 = self.fuente1.render(" a sembrar semillas. estas van a aparecer con un numero, que debes           ", 0, (255, 230, 245), (50, 50, 50))
        self.texto3 = self.fuente1.render(" memorizar. para que queden sembradas debes darle click al numero        ", 0, (255, 230, 245), (50, 50, 50))
        self.texto4 = self.fuente1.render(" de cada semilla  de forma ascendente. A medida que vayas sembrando,    ", 0, (255, 230, 245), (50, 50, 50))
        self.texto5 = self.fuente1.render(" mas semillas van a aparecer, y debes irlas sembrando para llenar al           ", 0, (255, 230, 245), (50, 50, 50))
        self.texto6 = self.fuente1.render(" bosque de arboles otra vez.                                                                                   ", 0, (255, 230, 245), (50, 50, 50))
        self.texto7 = self.fuente1.render(" Perdiste, intenta de nuevo", 0, (255, 230, 245), (50, 50, 50))
        self.texto8 = self.fuente1.render(" Ganaste", 0, (255, 230, 245), (50, 50, 50))

        self.puntaje = 5000

        self.semilla1 = self.semillasFactory.getSemilla()
        self.semilla2 = self.semillasFactory.getSemilla()
        self.semilla3 = self.semillasFactory.getSemilla()
        self.semilla4 = self.semillasFactory.getSemilla()
        self.semilla5 = self.semillasFactory.getSemilla()
        self.semilla6 = self.semillasFactory.getSemilla()
        self.semilla7 = self.semillasFactory.getSemilla()
        
        self.planta1 = self.plantasFactory.getPlanta()
        self.planta1.rect.x = Servicios.reajustarCoord(5, self.tablero.alto, 1000)
        self.planta1.rect.y = Servicios.reajustarCoord(350, self.tablero.alto, 700)
        self.planta2 = self.plantasFactory.getPlanta()
        self.planta2.rect.x = Servicios.reajustarCoord(110, self.tablero.alto, 1000)
        self.planta2.rect.y = Servicios.reajustarCoord(450, self.tablero.alto, 700)
        self.planta3 = self.plantasFactory.getPlanta()
        self.planta3.rect.x = Servicios.reajustarCoord(500, self.tablero.alto, 1000)
        self.planta3.rect.y = Servicios.reajustarCoord(300, self.tablero.alto, 700)
        self.planta4 = self.plantasFactory.getPlanta()
        self.planta4.rect.x = Servicios.reajustarCoord(330, self.tablero.alto, 1000)
        self.planta4.rect.y = Servicios.reajustarCoord(400, self.tablero.alto, 700)
        self.planta5 = self.plantasFactory.getPlanta()
        self.planta5.rect.x = Servicios.reajustarCoord(350, self.tablero.alto, 1000)
        self.planta5.rect.y = Servicios.reajustarCoord(250, self.tablero.alto, 700)
        self.planta6 = self.plantasFactory.getPlanta()
        self.planta6.rect.x = Servicios.reajustarCoord(200, self.tablero.alto, 1000)
        self.planta6.rect.y = Servicios.reajustarCoord(350, self.tablero.alto, 700)


        self.vamos3 = True
        self.vamos5 = False
        self.vamos7 = False
        self.termino = False
        self.termino2 = 1
        
        imgBtnRegresar = Servicios.cargarImagen("boton_regresar.png", "imagenes")
        imgBtnRegresarSelec = Servicios.cargarImagen("boton_regresar_selec.png", "imagenes")
        
        self.btnRegresar = Boton.Boton(imgBtnRegresar, imgBtnRegresarSelec, (1200 - 214 - 10), 10)

    def tex(self):
        x = Servicios.reajustarCoord(100, self.tablero.ancho, 1000)
        self.screen.blit(self.texto1, (x, Servicios.reajustarCoord(300, self.tablero.alto, 700)))
        self.screen.blit(self.texto2, (x, Servicios.reajustarCoord(323, self.tablero.alto, 700)))
        self.screen.blit(self.texto3, (x, Servicios.reajustarCoord(346, self.tablero.alto, 700)))
        self.screen.blit(self.texto4, (x, Servicios.reajustarCoord(369, self.tablero.alto, 700)))
        self.screen.blit(self.texto5, (x, Servicios.reajustarCoord(392, self.tablero.alto, 700)))
        self.screen.blit(self.texto6, (x, Servicios.reajustarCoord(415, self.tablero.alto, 700)))
    

    def inisemillas3(self):
    
        self.x = 0
    
        secuencia = [1, 2, 3]
        random.shuffle(secuencia)
    
        self.semilla1.image = self.semilla1.imagenes[secuencia[0]]
        self.semilla1.numero = secuencia[0]
        self.semilla1.rect.x = 0
        self.semilla1.rect.y = Servicios.reajustarCoord(300, self.tablero.alto, 700)
        
        self.semilla2.image = self.semilla2.imagenes[secuencia[1]]
        self.semilla2.numero = secuencia[1]
        self.semilla2.rect.x = 0
        self.semilla2.rect.y = Servicios.reajustarCoord(400, self.tablero.alto, 700)
        
        self.semilla3.image = self.semilla3.imagenes[secuencia[2]]
        self.semilla3.numero = secuencia[2]
        self.semilla3.rect.x = 0
        self.semilla3.rect.y = Servicios.reajustarCoord(340, self.tablero.alto, 700)
    
    
    def inisemillas5(self):
    
        secuencia = [1, 2, 3, 4, 5]
        random.shuffle(secuencia)
    
        self.x = 0
        
        self.semilla1.image = self.semilla1.imagenes[secuencia[0]]
        self.semilla1.numero = secuencia[0]
        self.semilla1.rect.x = 0
        self.semilla1.rect.y = Servicios.reajustarCoord(300, self.tablero.alto, 700)
        
        self.semilla2.image = self.semilla2.imagenes[secuencia[1]]
        self.semilla2.numero = secuencia[1]
        self.semilla2.rect.x = 0
        self.semilla2.rect.y = Servicios.reajustarCoord(400, self.tablero.alto, 700)
        
        self.semilla3.image = self.semilla3.imagenes[secuencia[2]]
        self.semilla3.numero = secuencia[2]
        self.semilla3.rect.x = 0
        self.semilla3.rect.y = Servicios.reajustarCoord(340, self.tablero.alto, 700)
        
        self.semilla4.image = self.semilla4.imagenes[secuencia[3]]
        self.semilla4.numero = secuencia[3]
        self.semilla4.rect.x = 0
        self.semilla4.rect.y = Servicios.reajustarCoord(300, self.tablero.alto, 700)
        
        self.semilla5.image = self.semilla5.imagenes[secuencia[4]]
        self.semilla5.numero = secuencia[4]
        self.semilla5.rect.x = 0
        self.semilla5.rect.y = Servicios.reajustarCoord(400, self.tablero.alto, 700)
    
    def inisemillas7(self):
    
        secuencia = [1, 2, 3, 4, 5, 6, 7]
        random.shuffle(secuencia)
    
        self.x = 0
        
        self.semilla1.image = self.semilla1.imagenes[secuencia[0]]
        self.semilla1.numero = secuencia[0]
        self.semilla1.rect.x = 0
        self.semilla1.rect.y = Servicios.reajustarCoord(300, self.tablero.alto, 700)
        
        self.semilla2.image = self.semilla2.imagenes[secuencia[1]]
        self.semilla2.numero = secuencia[1]
        self.semilla2.rect.x = 0
        self.semilla2.rect.y = Servicios.reajustarCoord(300, self.tablero.alto, 700)
        
        self.semilla3.image = self.semilla3.imagenes[secuencia[2]]
        self.semilla3.numero = secuencia[2]
        self.semilla3.rect.x = 0
        self.semilla3.rect.y = Servicios.reajustarCoord(280, self.tablero.alto, 700)
        
        self.semilla4.image = self.semilla4.imagenes[secuencia[3]]
        self.semilla4.numero = secuencia[3]
        self.semilla4.rect.x = 0
        self.semilla4.rect.y = Servicios.reajustarCoord(440, self.tablero.alto, 700)
        
        self.semilla5.image = self.semilla5.imagenes[secuencia[4]]
        self.semilla5.numero = secuencia[4]
        self.semilla5.rect.x = 0
        self.semilla5.rect.y = Servicios.reajustarCoord(400, self.tablero.alto, 700)
        
        self.semilla6.image = self.semilla6.imagenes[secuencia[5]]
        self.semilla6.numero = secuencia[5]
        self.semilla6.rect.x = 0
        self.semilla6.rect.y = Servicios.reajustarCoord(350, self.tablero.alto, 700)
        
        self.semilla7.image = self.semilla7.imagenes[secuencia[6]]
        self.semilla7.numero = secuencia[6]
        self.semilla7.rect.x = 0
        self.semilla7.rect.y = Servicios.reajustarCoord(350, self.tablero.alto, 700)

    def semillas3(self):
           
    
        if self.x < Servicios.reajustarCoord(150, self.tablero.alto, 1000):
                self.x += 2
                self.semilla1.rect.move_ip(3, 0)
                self.semilla2.rect.move_ip(3, 0)
                self.semilla3.rect.move_ip(4, 0)
        else:
            if self.termino2 == 1:
                self.termino = True
                self.termino2 += 1
            
        self.screen.blit(self.semilla1.image, self.semilla1.rect)   
        self.screen.blit(self.semilla2.image, self.semilla2.rect) 
        self.screen.blit(self.semilla3.image, self.semilla3.rect)

    def semillas5(self):
           
    
        if self.x < Servicios.reajustarCoord(150, self.tablero.alto, 1000):
                self.x += 2
                self.semilla1.rect.move_ip(3, 0)
                self.semilla2.rect.move_ip(3, 0)
                self.semilla3.rect.move_ip(4.5, 0)
                self.semilla4.rect.move_ip(6, 0)
                self.semilla5.rect.move_ip(6, 0)
        else:
            if self.termino2 == 1:
                self.termino = True
                self.termino2 += 1
                
        self.screen.blit(self.planta1.image, self.planta1.rect)
        self.screen.blit(self.planta2.image, self.planta2.rect)   
        self.screen.blit(self.planta3.image, self.planta3.rect)       
                
        self.screen.blit(self.semilla1.image, self.semilla1.rect)   
        self.screen.blit(self.semilla2.image, self.semilla2.rect) 
        self.screen.blit(self.semilla3.image, self.semilla3.rect)
        self.screen.blit(self.semilla4.image, self.semilla4.rect) 
        self.screen.blit(self.semilla5.image, self.semilla5.rect)
    
    def semillas7(self):
           
    
        if self.x < Servicios.reajustarCoord(150, self.tablero.alto, 1000):
                self.x += 2
                self.semilla1.rect.move_ip(1, 0)
                self.semilla2.rect.move_ip(4, 0)
                self.semilla3.rect.move_ip(6, 0)
                self.semilla4.rect.move_ip(1, 0)
                self.semilla5.rect.move_ip(4, 0)
                self.semilla6.rect.move_ip(2, 0)
                self.semilla7.rect.move_ip(6, 0)
        else:
            if self.termino2 == 1:
                self.termino = True
                self.termino2 += 1
                
        self.screen.blit(self.planta1.image, self.planta1.rect)
        self.screen.blit(self.planta2.image, self.planta2.rect)   
        self.screen.blit(self.planta3.image, self.planta3.rect) 
        self.screen.blit(self.planta4.image, self.planta4.rect) 
        self.screen.blit(self.planta5.image, self.planta5.rect)
        self.screen.blit(self.planta6.image, self.planta6.rect) 
        
        self.screen.blit(self.semilla1.image, self.semilla1.rect)   
        self.screen.blit(self.semilla2.image, self.semilla2.rect) 
        self.screen.blit(self.semilla3.image, self.semilla3.rect)
        self.screen.blit(self.semilla4.image, self.semilla4.rect) 
        self.screen.blit(self.semilla5.image, self.semilla5.rect)
        self.screen.blit(self.semilla6.image, self.semilla6.rect) 
        self.screen.blit(self.semilla7.image, self.semilla7.rect)
    
       
    def orden3(self):
        
        
        if self.orden[0] == 1 and self.orden[1] == 2 and self.orden[2] == 3:
            return True
        else:
            return False
    
    def orden5(self):
            
        
        if self.orden[0] == 1 and self.orden[1] == 2 and self.orden[2] == 3 and self.orden[3] == 4 and self.orden[4] == 5:
            return True
        else:
            return False
    
    def orden7(self):
            
        
        if self.orden[0] == 1 and self.orden[1] == 2 and self.orden[2] == 3 and self.orden[3] == 4 and self.orden[4] == 5 and self.orden[5] == 6 and self.orden[6] == 7:
            return True
        else:
            return False
        
    def run(self):
        
        # pygame.mouse.set_visible(True)
        
        inicio = True
        juego = False
        # terminar = False
        gano = False
        # perdio = False
        
        pasoSonidoExito = False
        
        noPaso = True
        
        
        
        self.audio.play()
        
        while noPaso:
            for event in pygame.event.get():
                    if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                            
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        
                        if self.cursor.colliderect(self.btnRegresar.rect):
                            self.tablero.sonido2.stop()
                            self.audio.stop()
                            noPaso = False
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
                            gano = False
                            noPaso = False
                            self.tablero.sonido2.stop()
                            self.tablero.pasoCuentoPaz = True
                            self.tablero.compartir.run("Amor","Juego")
                        
                        self.mouse.rect.center = pygame.mouse.get_pos()
                        
                        #=======================================================
                        # if gano and pygame.sprite.collide_rect(self.botonTerminar, self.mouse):
                        #    gano = False
                        #    noPaso = False
                        #    self.tablero.sonido2.stop()
                        #    self.tablero.pasoCuentoPaz = True
                        #    self.tablero.compartir.run("Amor","Juego")
                        #=======================================================
                            #self.tablero.sonido.play(-1)
                            #self.tablero.run() 
                        
                        #=======================================================
                        # if inicio and pygame.sprite.collide_rect(self.botonContinuar, self.mouse):
                        #    inicio = False
                        #    juego = True
                        #=======================================================
                        
                        mousecoords = pygame.mouse.get_pos() 
                        coordinateRect = Rect(mousecoords[0], mousecoords[1], 10, 10)
                        if self.semilla1.rect.colliderect(coordinateRect):
                            if not(self.orden.__contains__(self.semilla1.numero)) and not self.termino:
                                self.orden.append(self.semilla1.numero)
                                self.semilla1.image = self.semilla1.imagenes[8]
                        if self.semilla2.rect.colliderect(coordinateRect):
                            if not(self.orden.__contains__(self.semilla2.numero)) and not self.termino:
                                self.orden.append(self.semilla2.numero)
                                self.semilla2.image = self.semilla2.imagenes[8]
                        if self.semilla3.rect.colliderect(coordinateRect):
                            if not(self.orden.__contains__(self.semilla3.numero)):
                                self.orden.append(self.semilla3.numero)
                                self.semilla3.image = self.semilla3.imagenes[8]
                        if self.vamos5 or self.vamos7:
                            if self.semilla4.rect.colliderect(coordinateRect):
                                if not(self.orden.__contains__(self.semilla4.numero)) and not self.termino:
                                    self.orden.append(self.semilla4.numero) 
                                    self.semilla4.image = self.semilla4.imagenes[8]  
                            if self.semilla5.rect.colliderect(coordinateRect):
                                if not(self.orden.__contains__(self.semilla5.numero)) and not self.termino:
                                    self.orden.append(self.semilla5.numero) 
                                    self.semilla5.image = self.semilla5.imagenes[8]
                        if self.vamos7:
                            if self.semilla6.rect.colliderect(coordinateRect):
                                if not(self.orden.__contains__(self.semilla6.numero)) and not self.termino:
                                    self.orden.append(self.semilla6.numero)
                                    self.semilla6.image = self.semilla6.imagenes[8]
                            if self.semilla7.rect.colliderect(coordinateRect):
                                if not(self.orden.__contains__(self.semilla7.numero)) and not self.termino:
                                    self.orden.append(self.semilla7.numero)
                                    self.semilla7.image = self.semilla7.imagenes[8]  
                                
            self.screen.blit(self.background, (0, 0))
            self.clock.tick(60)
            self.cursor.update()
            
            # otro = ((pygame.time.get_ticks()/1000)<12)
            
            

            
            if inicio:
                self.msjInicio.visible = True
                self.btnRegresar.update(self.screen, self.cursor)
                #===============================================================
                # self.screen.blit(self.transparente, (0, 0))
                # self.btnRegresar.update(self.screen, self.cursor)
                # self.screen.blit(self.instrucciones, (600 - 425, 100))
                # self.botonContinuar.rect.center = (600, 525)
                # self.screen.blit(self.botonContinuar.image, self.botonContinuar.rect)
                #===============================================================
                self.inisemillas3()
                
            elif juego:
                
                self.btnRegresar.update(self.screen, self.cursor)
                    
                if self.vamos3:
                    if not(self.termino):
                        self.semillas3()
                        if len(self.orden) == 3:
                            if self.orden3():
                                self.screen.blit(self.texto8, (Servicios.reajustarCoord(400, self.tablero.ancho, 1000), Servicios.reajustarCoord(350, self.tablero.alto, 700)))
                                self.orden = []
                                # texto9 = self.fuente1.render("Puntaje " + str(self.puntaje), 0, (50, 50, 50))
                                # self.screen.blit(texto9, (5, 5))
                                pygame.display.update()
                                pygame.time.delay(4000)
                                self.vamos3 = False
                                self.termino2 = 1
                                self.inisemillas5()
                                self.vamos5 = True
                            else:
                                self.screen.blit(self.texto7, (Servicios.reajustarCoord(400, self.tablero.ancho, 1000), Servicios.reajustarCoord(350, self.tablero.alto, 700)))
                                self.orden = []
                                self.termino2 = 1
                                self.inisemillas3()
                                self.puntaje -= 200
                                # texto9 = self.fuente1.render("Puntaje " + str(self.puntaje), 0, (50, 50, 50))
                                # self.screen.blit(texto9, (5, 5))
                                pygame.display.update()
                                pygame.time.delay(4000)
                        # texto9 = self.fuente1.render("Puntaje " + str(self.puntaje), 0, (50, 50, 50))
                        # self.screen.blit(texto9, (5, 5))
                        pygame.display.update()
                    else:
                        pygame.time.delay(5000)
                        self.semilla1.image = self.semilla1.imagenes[0]
                        self.semilla2.image = self.semilla2.imagenes[0]
                        self.semilla3.image = self.semilla3.imagenes[0]
                        self.termino = False
                    
                elif self.vamos5:
                    if not(self.termino):
                        self.semillas5()
                        if len(self.orden) == 5:
                            if self.orden5():
                                self.screen.blit(self.texto8, (Servicios.reajustarCoord(400, self.tablero.ancho, 1000), Servicios.reajustarCoord(350, self.tablero.alto, 700)))
                                self.orden = []
                                # texto9 = self.fuente1.render("Puntaje " + str(self.puntaje), 0, (50, 50, 50))
                                # self.screen.blit(texto9, (5, 5))
                                pygame.display.update()
                                pygame.time.delay(4000)
                                self.vamos5 = False
                                self.termino2 = 1
                                self.inisemillas7()
                                self.vamos7 = True
                            else:
                                
                                self.screen.blit(self.texto7, (Servicios.reajustarCoord(400, self.tablero.ancho, 1000), Servicios.reajustarCoord(350, self.tablero.alto, 700)))
                                self.orden = []
                                self.termino2 = 1
                                self.inisemillas5()
                                self.puntaje -= 200
                                # texto9 = self.fuente1.render("Puntaje " + str(self.puntaje), 0, (50, 50, 50))
                                # self.screen.blit(texto9, (5, 5))
                                pygame.display.update()
                                pygame.time.delay(4000)
                        # texto9 = self.fuente1.render("Puntaje " + str(self.puntaje), 0, (50, 50, 50))
                        # self.screen.blit(texto9, (5, 5))
                        pygame.display.update()
                    else:
                        pygame.time.delay(5000)
                        self.semilla1.image = self.semilla1.imagenes[0]
                        self.semilla2.image = self.semilla2.imagenes[0]
                        self.semilla3.image = self.semilla3.imagenes[0]
                        self.semilla4.image = self.semilla4.imagenes[0]
                        self.semilla5.image = self.semilla5.imagenes[0]
                        self.termino = False
                elif self.vamos7:
                    if not(self.termino):
                        self.semillas7()
                        if len(self.orden) == 7:
                            if self.orden7():
                                self.orden = []
                                # texto9 = self.fuente1.render("Puntaje " + str(self.puntaje), 0, (50, 50, 50))
                                # self.screen.blit(texto9, (5, 5))
                                # if self.puntaje > 2400:
                                # texto10 = self.fuente1.render("Has completado el nivel de paz", 0, (255, 230, 245), (50, 50, 50))
                                # self.screen.blit(texto10, (Servicios.reajustarCoord(380, self.tablero.ancho, 1000), Servicios.reajustarCoord(350, self.tablero.alto, 700)))
                                # pygame.display.update()
                                # pygame.time.delay(4000)
                                self.vamos7 = False
                                self.vamos3 = True
                                self.termino2 = 1
                                self.puntaje = 5000
                                
                                
                                # self.texto = True
                # gano
                                juego = False
                                gano = True
                                # noPaso = False
                                # self.tablero.pasoPaz = True
                                # self.cita.run()
                                #===============================================
                                # else:
                                #    texto10 = self.fuente1.render("No obtuviste el puntaje suficiente. Intenta de nuevo", 0, (255, 230, 245), (50, 50, 50))
                                #    self.screen.blit(texto10, (Servicios.reajustarCoord(280, self.tablero.ancho, 1000), Servicios.reajustarCoord(350, self.tablero.alto, 700)))
                                #    self.puntaje = 5000
                                #    pygame.display.update()
                                #    pygame.time.delay(4000)
                                #    self.vamos7 = False
                                #    self.vamos3 = True
                                #    self.termino2 = 1
                                #    noPaso = False
                                #    self.texto = True
                                #===============================================
                                    
                                
                
                            else:
                                self.screen.blit(self.texto7, (Servicios.reajustarCoord(400, self.tablero.ancho, 1000), Servicios.reajustarCoord(350, self.tablero.alto, 700)))
                                self.orden = []
                                self.termino2 = 1
                                self.inisemillas7()
                                self.puntaje -= 200
                                # texto9 = self.fuente1.render("Puntaje " + str(self.puntaje), 0, (50, 50, 50))
                                # self.screen.blit(texto9, (5, 5))
                                pygame.display.update()
                                pygame.time.delay(4000)
                        # texto9 = self.fuente1.render("Puntaje " + str(self.puntaje), 0, (50, 50, 50))
                        # self.screen.blit(texto9, (5, 5))
                        pygame.display.update()
                    else:
                        pygame.time.delay(5000)
                        self.semilla1.image = self.semilla1.imagenes[0]
                        self.semilla2.image = self.semilla2.imagenes[0]
                        self.semilla3.image = self.semilla3.imagenes[0]
                        self.semilla4.image = self.semilla4.imagenes[0]
                        self.semilla5.image = self.semilla5.imagenes[0]
                        self.semilla6.image = self.semilla6.imagenes[0]
                        self.semilla7.image = self.semilla7.imagenes[0]
                        self.termino = False
            
            elif gano:
                self.screen.blit(self.planta1.image, self.planta1.rect)
                self.screen.blit(self.planta2.image, self.planta2.rect)   
                self.screen.blit(self.planta3.image, self.planta3.rect) 
                self.screen.blit(self.planta4.image, self.planta4.rect) 
                self.screen.blit(self.planta5.image, self.planta5.rect)
                self.screen.blit(self.planta6.image, self.planta6.rect) 
                
                self.screen.blit(self.semilla1.image, self.semilla1.rect)   
                self.screen.blit(self.semilla2.image, self.semilla2.rect) 
                self.screen.blit(self.semilla3.image, self.semilla3.rect)
                self.screen.blit(self.semilla4.image, self.semilla4.rect) 
                self.screen.blit(self.semilla5.image, self.semilla5.rect)
                self.screen.blit(self.semilla6.image, self.semilla6.rect) 
                self.screen.blit(self.semilla7.image, self.semilla7.rect)
                
                if pasoSonidoExito == False:
                    self.tablero.sonidoExito.play()
                    pasoSonidoExito = True
                
                self.msjGanaste.visible = True
                
                #===============================================================
                # self.screen.blit(self.transparente, (0, 0))
                # self.screen.blit(self.letrero, (380, 100))
                # self.screen.blit(self.botonTerminar.image, self.botonTerminar.rect)
                #===============================================================
                    
            
            self.msjInicio.update(self.screen, self.cursor)
            self.msjGanaste.update(self.screen, self.cursor)       
            pygame.display.update()
