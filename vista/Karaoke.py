#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, os, time
from modelo import Boton, Cursor, MensajeEmergente
from control import Servicios
from pygame.locals import *
class Karaoke(object):
    
    
    def __init__(self, cursor, screen, clock, tipo, padre):
    # def __init__(self, cursor, screen, clock):
        self.dirImagenes = os.path.join("imagenes", "karaoke")
        self.screen = screen
        self.clock = clock
        self.cursor = cursor
        self.tipo = tipo
        self.tablero = padre
        self.fondo = Servicios.cargarImagen("Fondo.jpg", "imagenes")
        # self.instrucciones = Servicios.cargarImagen("letrero_karaoke.png", self.dirImagenes)
        # self.transparente = pygame.image.load(os.path.join("imagenes", "verdad", "transparente.png")).convert_alpha()
        self.botonAceptar = Boton.BotonContinuar()
        self.mouse = Cursor.Mouse()
        
        self.msjInicio = MensajeEmergente.MensajeInicial(40, "Canto")
        
        imgBtnRegresar = Servicios.cargarImagen("boton_regresar.png", "imagenes")
        imgBtnRegresarSelec = Servicios.cargarImagen("boton_regresar_selec.png", "imagenes")
        
        self.btnRegresar = Boton.Boton(imgBtnRegresar, imgBtnRegresarSelec, (1200 - 214 - 10), 10)
        
        self.initFont()
        
        # tipo
        if self.tipo == 1:
            
            # self.compartir = compartirAmor.CompartirAmor(self.screen, self.clock, self.tablero)
            
            # self.letra = Servicios.cargarImagen("letra_paz.png", self.dirImagenes)
            self.linea1 = self.font.render(u"   Levanta la mano y grita fuerte  ", False, (0, 0, 0))
            self.linea2 = self.font.render(u"              amor, amor, amor         ", False, (0, 0, 0))
            self.linea3 = self.font.render(u"        Libera al mundo de su rabia    ", False, (0, 0, 0))
            self.linea4 = self.font.render(u"               y su mal humor          ", False, (0, 0, 0))
            self.linea5 = self.font.render(u"Mira hacia adentro en tu corazón...", False, (0, 0, 0))
            self.linea6 = self.linea5
            self.linea7 = self.font.render(u"         Haz silencio y escucha      ", False, (0, 0, 0))
            self.linea8 = self.font.render(u"         la razón... amor, amor      ", False, (0, 0, 0))
            self.linea9 = self.linea1
            self.linea10 = self.linea2
            self.linea11 = self.font.render(u"     Búscate dentro y encuentra    ", False, (0, 0, 0))
            self.linea12 = self.font.render(u"        el valor del amor, amor      ", False, (0, 0, 0))
            self.linea13 = self.font.render(u" Mira a los ojos y levanta tu voz...", False, (0, 0, 0))
            self.linea14 = self.linea2
            self.linea15 = self.font.render(u"         Transforma el planeta      ", False, (0, 0, 0))
            self.linea16 = self.font.render(u"             protege el árbol         ", False, (0, 0, 0))
            self.linea17 = self.font.render(u"        Canta, juega e imagina...    ", False, (0, 0, 0))
            self.linea18 = self.font.render(u"         Haz silencio se anuncia     ", False, (0, 0, 0))
            self.linea19 = self.linea12
            self.linea20 = self.linea1
            self.linea21 = self.linea2
            self.linea22 = self.font.render("Mira a los ojos y levanta tu voz...", False, (0, 0, 0))
            self.linea23 = self.linea2
            self.linea24 = self.font.render(u"    Busca en los ojos y descubre   ", False, (0, 0, 0))
            self.linea25 = self.linea12
            
            
            self.cancion = Servicios.cargarSonido("amor.ogg", os.path.join("audios"))
            
        elif self.tipo == 2:
            
            # self.compartir = compartirRectitud.CompartirRectitud(self.screen, self.clock, self.tablero)
            
            self.linea1 = self.font.render(u"         Siempre en la ruta hay dos caminos    ", False, (0, 0, 0))
            self.linea2 = self.font.render(u"                   y yo elijo ¿cuál seguire?    ", False, (0, 0, 0))
            self.linea3 = self.font.render(u"            Si grito fuerte todos se asustan   ", False, (0, 0, 0))
            self.linea4 = self.font.render(u"                mejor dialogo, ¡yo lo haré!    ", False, (0, 0, 0))
            self.linea5 = self.font.render(u"       Miro a lo lejos un bosque sucio y pienso", False, (0, 0, 0))
            self.linea6 = self.font.render(u"                        ¿qué debo hacer?       ", False, (0, 0, 0))
            self.linea7 = self.font.render(u"             Una voz dentro responde fuerte    ", False, (0, 0, 0))
            self.linea8 = self.font.render(u"                           ¡lo limpiaré!        ", False, (0, 0, 0))
            self.linea9 = self.font.render(u"   Y en las tardes ya en mi casa algo pregunta  ", False, (0, 0, 0))
            self.linea10 = self.linea6
            self.linea11 = self.font.render(u" pienso en los juegos en mis amigos ir a la calle", False, (0, 0, 0))
            self.linea12 = self.font.render(u"               pero alegre respondo pronto       ", False, (0, 0, 0))
            self.linea13 = self.font.render(u"                  ¡Primero haré mi deber!         ", False, (0, 0, 0))
            self.linea14 = self.linea13
            self.linea15 = self.linea13
            
            self.cancion = Servicios.cargarSonido("rectitud.ogg", os.path.join("audios"))
            
        elif self.tipo == 3:
            
            # self.compartir = compartirPaz.CompartirPaz(self.screen, self.clock, self.tablero)
            
            self.linea1 = self.font.render(u"       Árbol, perro, ave, río, aire soy ", False, (0, 0, 0))
            self.linea2 = self.font.render(u"            Comprendo lo que digo       ", False, (0, 0, 0))
            self.linea3 = self.font.render(u"               por eso hoy te cuido...  ", False, (0, 0, 0))
            self.linea4 = self.font.render(u"Mestizo, negro, blanco, indio, zambo soy", False, (0, 0, 0))
            self.linea5 = self.font.render(u"               Te quiero y te respeto   ", False, (0, 0, 0))
            self.linea6 = self.font.render(u"               contigo siempre voy...   ", False, (0, 0, 0))
            self.linea7 = self.font.render(u"            En el mar, en la montaña   ", False, (0, 0, 0))
            self.linea8 = self.font.render(u"              en la selva o la ciudad    ", False, (0, 0, 0))
            self.linea9 = self.font.render(u"           como hermanos andaremos     ", False, (0, 0, 0))
            self.linea10 = self.font.render(u"                  para vivir en paz     ", False, (0, 0, 0))
            self.linea11 = self.font.render(u"              En un día de disgustos     ", False, (0, 0, 0))
            self.linea12 = self.font.render(u"                de peleas sin razón      ", False, (0, 0, 0))
            self.linea13 = self.font.render(u"                miro fijo a tus ojos      ", False, (0, 0, 0))
            self.linea14 = self.linea13
            self.linea15 = self.font.render(u"               para ver el corazón       ", False, (0, 0, 0))
            self.linea16 = self.linea7
            self.linea17 = self.linea8
            self.linea18 = self.linea9
            self.linea19 = self.linea10
            self.linea20 = self.linea7
            self.linea21 = self.linea8
            self.linea22 = self.linea9
            self.linea23 = self.linea10
            
            self.cancion = Servicios.cargarSonido("paz.ogg", os.path.join("audios"))
        
        elif self.tipo == 4:
            
            # self.compartir = compartirVerdad.CompartirVerdad(self.screen, self.clock, self.tablero)
            
            self.linea1 = self.font.render(u"                Verdad, verdad, verdad     ", False, (0, 0, 0))
            self.linea2 = self.font.render(u"       no más mentiras, por favor no más   ", False, (0, 0, 0))
            self.linea3 = self.font.render(u"                    por favor no más       ", False, (0, 0, 0))
            self.linea4 = self.font.render(u" que en la guerra no se pierdan mis sueños ", False, (0, 0, 0))
            self.linea5 = self.font.render(u"               quiero crecer en libertad   ", False, (0, 0, 0))
            self.linea6 = self.font.render(u"        Quiero siempre el calor del sol    ", False, (0, 0, 0))
            self.linea7 = self.font.render(u"     que me acompañe un gran resplandor    ", False, (0, 0, 0))
            self.linea8 = self.font.render(u"la esencia está adentro y entiendo el valor", False, (0, 0, 0))
            self.linea9 = self.font.render(u"         de todo lo que dice tu corazón    ", False, (0, 0, 0))
            self.linea10 = self.font.render(u"              Un espejo te reflejará       ", False, (0, 0, 0))
            self.linea11 = self.font.render("        pero no te pierdas en la vanidad    ", False, (0, 0, 0))
            self.linea12 = self.font.render("       si me hablas siempre con la verdad   ", False, (0, 0, 0))
            self.linea13 = self.font.render(u"        mi corazón explota de felicidad    ", False, (0, 0, 0))
            self.linea14 = self.linea1
            self.linea15 = self.linea2
            self.linea16 = self.linea3
            self.linea17 = self.linea4
            self.linea18 = self.linea5
            self.linea19 = self.linea1
            self.linea20 = self.linea2
            self.linea21 = self.linea3
            self.linea22 = self.linea4
            self.linea23 = self.linea5
            
            
            self.cancion = Servicios.cargarSonido("verdad.ogg", os.path.join("audios"))
            
        elif self.tipo == 5:
            
            # self.compartir = compartirNoViolencia.CompartirNoViolencia(self.screen, self.clock, self.tablero)
            
            self.linea1 = self.font.render(u"    Cierra las manos hacia el frente", False, (0, 0, 0))
            self.linea2 = self.font.render(u"        alista un dedo, el de señalar", False, (0, 0, 0))
            self.linea3 = self.font.render(u"      muévelo a un lado y hacia al otro", False, (0, 0, 0))
            self.linea4 = self.font.render(u"         y a los violentos tú les dirás", False, (0, 0, 0))
            self.linea5 = self.font.render(u"      Ya no más gritos, ya no más armas", False, (0, 0, 0))
            self.linea6 = self.font.render(u"               no quiero más guerra    ", False, (0, 0, 0))
            self.linea7 = self.font.render(u"                     ¡no violencia!    ", False, (0, 0, 0))
            self.linea8 = self.linea5
            self.linea9 = self.linea6
            self.linea10 = self.linea7
            self.linea11 = self.font.render(u"         Corre rápido hacia tu familia ", False, (0, 0, 0))
            self.linea12 = self.font.render(u"         Pero los brazos debes levantar ", False, (0, 0, 0))
            self.linea13 = self.font.render(u"           y cuando los tengas cerca    ", False, (0, 0, 0))
            self.linea14 = self.font.render(u"           Con un abrazo tú les dirás   ", False, (0, 0, 0))
            self.linea15 = self.font.render(u"      Ya no más gritos, no más peleas", False, (0, 0, 0))
            self.linea16 = self.font.render(u"                   No más ofensas        ", False, (0, 0, 0))
            self.linea17 = self.linea7
            self.linea18 = self.linea15
            self.linea19 = self.linea16
            self.linea20 = self.linea7
            
            
            self.cancion = Servicios.cargarSonido("noViolencia.ogg", os.path.join("audios"))
        
        
        # self.cancion = Servicios.cargarSonido("cancion_karaoke.ogg", os.path.join("audios"))
        
        imgBotonContinuar = pygame.image.load(os.path.join("imagenes", "boton_continuar.png")).convert_alpha()
        
        self.botonContinuar = Boton.Boton(imgBotonContinuar, imgBotonContinuar, 10, 100)
        
        imgBotonReproducir = Servicios.cargarImagen("boton_play.png", self.dirImagenes)
        imgBotonReproducirSelec = Servicios.cargarImagen("boton_play_selec.png", self.dirImagenes)
        
        self.botonReproducir = Boton.Boton(imgBotonReproducir, imgBotonReproducirSelec, 10, 50)
        
        imgBotonPausar = Servicios.cargarImagen("boton_pause.png", self.dirImagenes)
        imgBotonPausarSelec = Servicios.cargarImagen("boton_pause_selec.png", self.dirImagenes)
        # pausar, reanudar
        self.botonPausar = Boton.Boton(imgBotonPausar, imgBotonPausarSelec, 70, 50)
        # detener, reproducir
        imgBotonDetener = Servicios.cargarImagen("boton_stop.png", self.dirImagenes)
        imgBotonDetenerSelec = Servicios.cargarImagen("boton_stop_selec.png", self.dirImagenes)
        
        self.botonDetener = Boton.Boton(imgBotonDetener, imgBotonDetenerSelec, 130, 50)
        
        
        
    
    def initFont(self):
        pygame.font.init()
        self.rutaFuente = os.path.join("fuentes", "PatrickHand-Regular.ttf")
        self.font = pygame.font.Font(self.rutaFuente, 70)  # tamaño de la fuente
        

       
    def run(self):
        
        inicio = True
        juego = False
        
        duracion = int(self.cancion.get_length())
        minDuracion = int(duracion / 60)
        tMinDuracion = "0%i" % (minDuracion)
        segDuracion = duracion - (minDuracion * 60)
        if segDuracion < 10:
            tSegDuracion = "0%i" % (segDuracion)
        else:
            tSegDuracion = "%i" % (segDuracion)
            
        fuenteTitulo = pygame.font.SysFont("helvetica", 30, True)
        terminar = False
        pausado = False
        detenido = False
        continuarVisible = False
        t = time.time()
        t2 = 0
        segundos = 0
        segundos2 = 0
        segundosAlPausar = 0
        minutos = 0
        while not terminar:
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                            
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    
                    if self.cursor.colliderect(self.btnRegresar.rect):
                            self.cancion.stop()
                            terminar = True
                            self.tablero.sonido.play(-1)
                            self.tablero.run()
                            
                    if self.cursor.colliderect(self.msjInicio.btn.rect):
                            self.msjInicio.visible = False
                            inicio = False
                            juego = True
                            t = time.time()
                            self.cancion.play()
                    
                    #===========================================================
                    # self.mouse.rect.center = pygame.mouse.get_pos()
                    #     
                    # if inicio and pygame.sprite.collide_rect(self.botonAceptar, self.mouse):
                    #         inicio = False
                    #         juego = True 
                    #         t = time.time()
                    #         self.cancion.play()
                    #===========================================================
                    
                    if self.cursor.colliderect(self.botonContinuar.rect):
                        terminar = True

                        if self.tipo == 1:
                            self.tablero.pasoCantoAmor = True
                            # self.tablero.sonido.play(-1)
                            self.tablero.compartir.run("Amor", "Canto")
                        if self.tipo == 2:
                            self.tablero.pasoCantoRectitud = True
                            # self.tablero.sonido.play(-1)
                            self.tablero.compartir.run("Rectitud", "Canto")
                        if self.tipo == 3:
                            self.tablero.pasoCantoPaz = True
                            # self.tablero.sonido.play(-1)
                            self.tablero.compartir.run("Paz", "Canto")
                        if self.tipo == 4:
                            self.tablero.pasoCantoVerdad = True
                            # self.tablero.sonido.play(-1)
                            self.tablero.compartir.run("Verdad", "Canto")
                        if self.tipo == 5:
                            self.tablero.pasoCantoNoViolencia = True
                            # self.tablero.sonido.play(-1)
                            self.tablero.compartir.run("NoViolencia", "Canto")
                        
                        
                        # self.tablero.run()
                        
                    
                    if self.cursor.colliderect(self.botonPausar.rect):
                        if pausado == False:
                            pausado = True
                            segundosAlPausar = segundos
                            pygame.mixer.pause()
        
                    if self.cursor.colliderect(self.botonReproducir.rect):
                        if pausado == True:
                            pausado = False
                            continuarVisible = False
                            t = time.time() - segundosAlPausar
                            pygame.mixer.unpause()
                        if detenido == True:
                            detenido = False
                            pausado = False
                            continuarVisible = False
                            t = time.time()
                            # segundos = 0
                            self.cancion.play()
                            
                    
                    if self.cursor.colliderect(self.botonDetener.rect):
                        if detenido == False:
                            detenido = True
                            continuarVisible = True
                            segundos = 0
                            segundos2 = 0
                            minutos = 0
                            self.cancion.stop()
                        
                
            
            self.clock.tick(60)
            self.cursor.update()
            
            self.screen.blit(self.fondo, (0, 0))
            
            self.msjInicio.update(self.screen, self.cursor)
            
            if inicio:
                self.msjInicio.visible = True
                self.btnRegresar.update(self.screen, self.cursor)
                #===============================================================
                # self.screen.blit(self.transparente, (0, 0))
                # self.btnRegresar.update(self.screen, self.cursor)
                # self.screen.blit(self.instrucciones, (600 - 431, 100))
                # self.botonAceptar.rect.center = (600, 400)
                # self.screen.blit(self.botonAceptar.image, self.botonAceptar.rect)
                #===============================================================
            
            elif juego:
                
                self.btnRegresar.update(self.screen, self.cursor)
                
                if self.tipo == 1:
                
                    x = 150
                    y = 350
                
                    # self.screen.blit(self.letra, (0, 0))
                    if segundos > 70:
                        self.screen.blit(self.linea25, (x, y)) 
                    elif segundos > 67:
                        self.screen.blit(self.linea24, (x, y)) 
                    elif segundos > 64:
                        self.screen.blit(self.linea23, (x, y)) 
                    elif segundos > 61:
                        self.screen.blit(self.linea22, (x, y)) 
                    elif segundos > 58:
                        self.screen.blit(self.linea21, (x, y)) 
                    elif segundos > 56:
                        self.screen.blit(self.linea20, (x, y)) 
                    elif segundos > 53:
                        self.screen.blit(self.linea19, (x, y)) 
                    elif segundos > 50:
                        self.screen.blit(self.linea18, (x, y)) 
                    elif segundos > 46:
                        self.screen.blit(self.linea17, (x, y))   
                    elif segundos > 44:
                        self.screen.blit(self.linea16, (x, y))
                    elif segundos > 42:
                        self.screen.blit(self.linea15, (x, y))
                    elif segundos > 40:
                        self.screen.blit(self.linea14, (x, y))
                    elif segundos > 37:
                        self.screen.blit(self.linea13, (x, y))
                    elif segundos > 34:
                        self.screen.blit(self.linea12, (x, y))
                    elif segundos > 32:
                        self.screen.blit(self.linea11, (x, y))
                    elif segundos > 29:
                        self.screen.blit(self.linea10, (x, y))
                    elif segundos > 26:
                        self.screen.blit(self.linea9, (x, y))
                    elif segundos > 23:
                        self.screen.blit(self.linea8, (x, y))
                    elif segundos > 20:
                        self.screen.blit(self.linea7, (x, y))
                    elif segundos > 15:
                        self.screen.blit(self.linea6, (x, y))
                    elif segundos > 12:
                        self.screen.blit(self.linea5, (x, y))
                    elif segundos > 9:
                        self.screen.blit(self.linea4, (x, y))
                    elif segundos > 6:
                        self.screen.blit(self.linea3, (x, y))
                    elif segundos > 3:
                        self.screen.blit(self.linea2, (x, y))
                    elif segundos > 1:
                        self.screen.blit(self.linea1, (x, y))
                        
                    
                if self.tipo == 2:
                    
                    
                    x = 0
                    y = 350
                    
                    if segundos > 51:
                        self.screen.blit(self.linea15, (x, y))
                    elif segundos > 47:
                        self.screen.blit(self.linea14, (x, y))
                    elif segundos > 44:
                        self.screen.blit(self.linea13, (x, y))
                    elif segundos > 40:
                        self.screen.blit(self.linea12, (x, y))
                    elif segundos > 34:
                        self.screen.blit(self.linea11, (x, y))
                    elif segundos > 33:
                        self.screen.blit(self.linea10, (x, y))
                    elif segundos > 27:
                        self.screen.blit(self.linea9, (x, y))
                    elif segundos > 25:
                        self.screen.blit(self.linea8, (x, y))
                    elif segundos > 20:
                        self.screen.blit(self.linea7, (x, y))
                    elif segundos > 19:
                        self.screen.blit(self.linea6, (x, y))
                    elif segundos > 13:
                        self.screen.blit(self.linea5, (x, y))
                    elif segundos > 11:
                        self.screen.blit(self.linea4, (x, y))
                    elif segundos > 7:
                        self.screen.blit(self.linea3, (x, y))
                    elif segundos > 4:
                        self.screen.blit(self.linea2, (x, y))
                    elif segundos > 0:
                        self.screen.blit(self.linea1, (x, y))
                        
                
                if self.tipo == 3:
                
                    x = 100
                    y = 350
                
                    # self.screen.blit(self.letra, (0, 0))
                    if segundos > 72:
                        self.screen.blit(self.linea23, (x, y)) 
                    elif segundos > 69:
                        self.screen.blit(self.linea22, (x, y)) 
                    elif segundos > 66:
                        self.screen.blit(self.linea21, (x, y)) 
                    elif segundos > 64:
                        self.screen.blit(self.linea20, (x, y)) 
                    elif segundos > 61:
                        self.screen.blit(self.linea19, (x, y)) 
                    elif segundos > 58:
                        self.screen.blit(self.linea18, (x, y)) 
                    elif segundos > 55:
                        self.screen.blit(self.linea17, (x, y))   
                    elif segundos > 53:
                        self.screen.blit(self.linea16, (x, y))
                    elif segundos > 50:
                        self.screen.blit(self.linea15, (x, y))
                    elif segundos > 47:
                        self.screen.blit(self.linea14, (x, y))
                    elif segundos > 44:
                        self.screen.blit(self.linea13, (x, y))
                    elif segundos > 42:
                        self.screen.blit(self.linea12, (x, y))
                    elif segundos > 38:
                        self.screen.blit(self.linea11, (x, y))
                    elif segundos > 36:
                        self.screen.blit(self.linea10, (x, y))
                    elif segundos > 33:
                        self.screen.blit(self.linea9, (x, y))
                    elif segundos > 30:
                        self.screen.blit(self.linea8, (x, y))
                    elif segundos > 27:
                        self.screen.blit(self.linea7, (x, y))
                    elif segundos > 25:
                        self.screen.blit(self.linea6, (x, y))
                    elif segundos > 21:
                        self.screen.blit(self.linea5, (x, y))
                    elif segundos > 16:
                        self.screen.blit(self.linea4, (x, y))
                    elif segundos > 13:
                        self.screen.blit(self.linea3, (x, y))
                    elif segundos > 11:
                        self.screen.blit(self.linea2, (x, y))
                    elif segundos > 5:
                        self.screen.blit(self.linea1, (x, y))
                        
                if self.tipo == 4:
                
                    x = 70
                    y = 350
                
                    # self.screen.blit(self.letra, (0, 0))
                    if segundos > 66:
                        self.screen.blit(self.linea23, (x, y)) 
                    elif segundos > 63:
                        self.screen.blit(self.linea22, (x, y)) 
                    #elif segundos > 62:
                        #self.screen.blit(self.linea21, (x, y)) 
                    elif segundos > 60:
                        self.screen.blit(self.linea20, (x, y)) 
                    elif segundos > 57:
                        self.screen.blit(self.linea19, (x, y)) 
                    elif segundos > 55:
                        self.screen.blit(self.linea18, (x, y)) 
                    elif segundos > 51:
                        self.screen.blit(self.linea17, (x, y))   
                    #elif segundos > 50:
                        #self.screen.blit(self.linea16, (x, y))
                    elif segundos > 49:
                        self.screen.blit(self.linea15, (x, y))
                    elif segundos > 45:
                        self.screen.blit(self.linea14, (x, y))
                    elif segundos > 39:
                        self.screen.blit(self.linea13, (x, y))
                    elif segundos > 37:
                        self.screen.blit(self.linea12, (x, y))
                    elif segundos > 34:
                        self.screen.blit(self.linea11, (x, y))
                    elif segundos > 31:
                        self.screen.blit(self.linea10, (x, y))
                    elif segundos > 27:
                        self.screen.blit(self.linea9, (x, y))
                    elif segundos > 24:
                        self.screen.blit(self.linea8, (x, y))
                    elif segundos > 22:
                        self.screen.blit(self.linea7, (x, y))
                    elif segundos > 19:
                        self.screen.blit(self.linea6, (x, y))
                    elif segundos > 12:
                        self.screen.blit(self.linea5, (x, y))
                    elif segundos > 9:
                        self.screen.blit(self.linea4, (x, y))
                    #elif segundos > 7:
                        #self.screen.blit(self.linea3, (x, y))
                    elif segundos > 6:
                        self.screen.blit(self.linea2, (x, y))
                    elif segundos > 3:
                        self.screen.blit(self.linea1, (x, y))
                
                if self.tipo == 5:
                
                    x = 100
                    y = 350
                
                    # self.screen.blit(self.letra, (0, 0))
                    if segundos > 58:
                        self.screen.blit(self.linea20, (x, y)) 
                    elif segundos > 57:
                        self.screen.blit(self.linea19, (x, y)) 
                    elif segundos > 54:
                        self.screen.blit(self.linea18, (x, y)) 
                    elif segundos > 52:
                        self.screen.blit(self.linea17, (x, y))   
                    elif segundos > 50:
                        self.screen.blit(self.linea16, (x, y))
                    elif segundos > 48:
                        self.screen.blit(self.linea15, (x, y))
                    elif segundos > 43:
                        self.screen.blit(self.linea14, (x, y))
                    elif segundos > 40:
                        self.screen.blit(self.linea13, (x, y))
                    elif segundos > 37:
                        self.screen.blit(self.linea12, (x, y))
                    elif segundos > 33:
                        self.screen.blit(self.linea11, (x, y))
                    elif segundos > 27:
                        self.screen.blit(self.linea10, (x, y))
                    elif segundos > 25:
                        self.screen.blit(self.linea9, (x, y))
                    elif segundos > 22:
                        self.screen.blit(self.linea8, (x, y))
                    elif segundos > 20:
                        self.screen.blit(self.linea7, (x, y))
                    elif segundos > 18:
                        self.screen.blit(self.linea6, (x, y))
                    elif segundos > 15:
                        self.screen.blit(self.linea5, (x, y))
                    elif segundos > 11:
                        self.screen.blit(self.linea4, (x, y))
                    elif segundos > 8:
                        self.screen.blit(self.linea3, (x, y))
                    elif segundos > 5:
                        self.screen.blit(self.linea2, (x, y))
                    elif segundos > 1:
                        self.screen.blit(self.linea1, (x, y))
                
                self.cursor.update()
                
                if continuarVisible:
                    self.botonContinuar.update(self.screen, self.cursor)
                # if pausado:
                self.botonReproducir.update(self.screen, self.cursor)
                # else:
                self.botonPausar.update(self.screen, self.cursor)
                
        
                self.botonDetener.update(self.screen, self.cursor)
                
                
                if pausado == False and detenido == False:   
                    segundos = time.time() - t
                    segundos = int(segundos)
                    segundos2 = segundos
                    if segundos >= 60:
                        minutos = int(duracion / 60)
                        segundos2 = segundos - (minutos * 60)
                
                if segundos > duracion:
                    detenido = True
                    segundos = 0
                    segundos2 = 0
                    minutos = 0
                    continuarVisible = True
                    
                else:
                    
                    tMinutos = "0%i" % (minutos)
                    
                    if segundos2 < 10:
                        tSegundos = "0%i" % (segundos2)
                    else:
                        tSegundos = "%i" % (segundos2)
                        
                    textoInfo = fuenteTitulo.render("%s:%s/%s:%s" % (tMinutos, tSegundos, tMinDuracion, tSegDuracion) , 1, (255, 255, 255))
                    self.screen.blit(textoInfo, (10, 10))
        
            pygame.display.flip()
            
