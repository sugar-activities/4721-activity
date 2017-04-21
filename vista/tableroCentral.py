#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, os, VentanaMandala, Amor, Rectitud, pazSemillas, pacman, puzzle, Karaoke, Cita
from control import Servicios, resource
from modelo import Boton, MensajeEmergente
from src import compartir
from pygame.locals import *

class tableroCentral(object):
    
    def __init__(self, ventPadre, cursor, screen, clock, anchoVentana, altoVentana):
        
        self.compartir = compartir.Compartir(screen, cursor, clock, self)
        
        self.menu = ventPadre
        
        self.ancho = anchoVentana
        self.alto = altoVentana
        
        self.msjInicio = MensajeEmergente.MensajeInicial(40, "Tablero")
        
        self.personaje = self.menu.personaje
        
        self.mandala = None
        self.cuento = None
        self.cita = None
        self.canto = None

        self.sonido = self.menu.musicaMenu
        
        self.audio = Servicios.cargarSonido("intro.ogg", os.path.join("audios", "cuentos"))
        
        # cargo a memoria los audios
        resource.set_sounds_path(os.path.join("audios"))
        self.sonidoAmor = resource.get_sound("amor_instrum.ogg")
        self.sonidoRectitud = resource.get_sound("rectitud_instrum.ogg")
        self.sonidoPaz = resource.get_sound("paz_instrum.ogg")
        self.sonidoVerdad = resource.get_sound("verdad_instrum.ogg")
        self.sonidoNoViolencia = resource.get_sound("noViolencia_instrum.ogg")
        # self.sonido2=resource.get_sound("verdad_instrum.ogg")
        self.sonido2 = None
        
        
        # self.sonidoExito = Servicios.cargarSonido("exito.wav", "audios")
        self.sonidoExito = resource.get_sound("exito.wav")
        
        self.dirImagenes = os.path.join("imagenes", "tableroCentral")
        
        resource.set_images_path(self.dirImagenes)
        
        # self.background = Servicios.cargarImagen("Mandala_Tablero_Blanco.png", self.dirImagenes)
        # self.imagenPaz = Servicios.cargarImagen("Mandala_Tablero_Paz.png", self.dirImagenes)
        # self.imagenPazSel = Servicios.cargarImagen("Mandala_Tablero_Paz_Seleccionado.png", self.dirImagenes)
        # self.imagenAmor = Servicios.cargarImagen("Mandala_Tablero_Amor.png", self.dirImagenes)
        # self.imagenAmorSel = Servicios.cargarImagen("Mandala_Tablero_Amor_Seleccionado.png", self.dirImagenes)
        # self.imagenRectitud = Servicios.cargarImagen("Mandala_Tablero_Rectitud.png", self.dirImagenes)
        # self.imagenRectitudSel = Servicios.cargarImagen("Mandala_Tablero_Rectitud_Seleccionado.png", self.dirImagenes)
        # self.imagenVerdad = Servicios.cargarImagen("Mandala_Tablero_Verdad.png", self.dirImagenes)
        # self.imagenVerdadSel = Servicios.cargarImagen("Mandala_Tablero_Verdad_Seleccionado.png", self.dirImagenes)
        # self.imagenNoViolencia = Servicios.cargarImagen("Mandala_Tablero_NoViolencia.png", self.dirImagenes)
        # self.imagenNoViolenciaSel = Servicios.cargarImagen("Mandala_Tablero_NoViolencia_Seleccionado.png", self.dirImagenes)
        # self.candadoRectitud = Servicios.cargarImagen("candado_rectitud.png", self.dirImagenes)
        # self.candadoPaz = Servicios.cargarImagen("candado_paz.png", self.dirImagenes)
        # self.candadoVerdad = Servicios.cargarImagen("candado_verdad.png", self.dirImagenes)
        # self.candadoNoViolencia = Servicios.cargarImagen("candado_noviolencia.png", self.dirImagenes)
        
        self.background = resource.get_image("Mandala_Tablero_Blanco.png")
        self.imagenPaz = resource.get_image("Mandala_Tablero_Paz.png")
        self.imagenPazSel = resource.get_image("Mandala_Tablero_Paz_Seleccionado.png")
        self.imagenAmor = resource.get_image("Mandala_Tablero_Amor.png")
        self.imagenAmorSel = resource.get_image("Mandala_Tablero_Amor_Seleccionado.png")
        self.imagenRectitud = resource.get_image("Mandala_Tablero_Rectitud.png")
        self.imagenRectitudSel = resource.get_image("Mandala_Tablero_Rectitud_Seleccionado.png")
        self.imagenVerdad = resource.get_image("Mandala_Tablero_Verdad.png")
        self.imagenVerdadSel = resource.get_image("Mandala_Tablero_Verdad_Seleccionado.png")
        self.imagenNoViolencia = resource.get_image("Mandala_Tablero_NoViolencia.png")
        self.imagenNoViolenciaSel = resource.get_image("Mandala_Tablero_NoViolencia_Seleccionado.png")
        self.candadoRectitud = resource.get_image("candado_rectitud.png")
        self.candadoPaz = resource.get_image("candado_paz.png")
        self.candadoVerdad = resource.get_image("candado_verdad.png")
        self.candadoNoViolencia = resource.get_image("candado_noviolencia.png")
        
        self.cursor = cursor
        self.screen = screen
        self.clock = clock
        
        self.pasoSilencioAmor = False
        self.pasoCuentoAmor = False
        self.pasoCitaAmor = False
        self.pasoCantoAmor = False
        self.pasoAmor = False
        
        self.pasoSilencioRectitud = False
        self.pasoCuentoRectitud = False
        self.pasoCitaRectitud = False
        self.pasoCantoRectitud = False
        self.pasoRectitud = False
        
        self.pasoSilencioPaz = False
        self.pasoCuentoPaz = False
        self.pasoCitaPaz = False
        self.pasoCantoPaz = False
        self.pasoPaz = False
        
        self.pasoSilencioVerdad = False
        self.pasoCuentoVerdad = False
        self.pasoCitaVerdad = False
        self.pasoCantoVerdad = False
        self.pasoVerdad = False
        
        self.pasoSilencioNoViolencia = False
        self.pasoCuentoNoViolencia = False
        self.pasoCitaNoViolencia = False
        self.pasoCantoNoViolencia = False
        self.pasoNoViolencia = False
        
        sumarAX = 100
        sumarAY = 63
        
        x = 431 + sumarAX
        y = 50 + 5 + sumarAY
        anch = 141
        alt = 141
        self.areaPaz = Rect(x, y, anch, alt) 
        
        x = 643 + sumarAX
        y = 197 + 15 + sumarAY
        anch = 141
        alt = 141
        self.areaRectitud = Rect(x, y, anch, alt) 
        
        x = 558 + sumarAX
        y = 430 + 30 + sumarAY
        anch = 141
        alt = 141
        self.areaAmor = Rect(x, y, anch, alt) 
        
        x = 297 + sumarAX
        y = 430 + 30 + sumarAY
        anch = 141
        alt = 141
        self.areaNoViolencia = Rect(x, y, anch, alt) 
        
        x = 216 + sumarAX
        y = 197 + 15 + sumarAY
        anch = 141
        alt = 141
        self.areaVerdad = Rect(x, y, anch, alt)    
        
        # imgBtnRegresar = Servicios.cargarImagen("boton_regresar.png", "imagenes")
        # imgBtnRegresarSelec = Servicios.cargarImagen("boton_regresar_selec.png", "imagenes")
        
        resource.set_images_path(os.path.join("imagenes"))
        imgBtnRegresar = resource.get_image("boton_regresar.png")
        imgBtnRegresarSelec = resource.get_image("boton_regresar_selec.png")
        
        self.btnRegresar = Boton.Boton(imgBtnRegresar, imgBtnRegresarSelec, (self.ancho - 214 - 10), 10)
        
        self.initFont()
        
        self.intro = True
        self.msjInicio = MensajeEmergente.MensajeInicial(40, "Tablero")
        
    def initFont(self):
            pygame.font.init()
            rutaFuente = os.path.join("fuentes", "PatrickHand-Regular.ttf")
            self.fuenteGrande = pygame.font.Font(rutaFuente, 40)  # tamaño de la fuente
            self.fuente = pygame.font.Font(rutaFuente, 35)  # tamaño de la fuente
            
    def run(self):
        
        if self.intro:
            self.sonido.stop()
            self.audio.play()
          
        self.xSelector = 0
        self.ySelector = -200
        
        resource.set_images_path(self.dirImagenes)
        # imgBtnSilencio = Servicios.cargarImagen("icono_silencio.png", self.dirImagenes)
        # imgBtnSilencioSelec = Servicios.cargarImagen("icono_silencio_selec.png", self.dirImagenes)
        imgBtnSilencio = resource.get_image("icono_silencio.png")
        imgBtnSilencioSelec = resource.get_image("icono_silencio_selec.png")
        self.btnSilencio = Boton.Boton(imgBtnSilencio, imgBtnSilencioSelec, self.xSelector, self.ySelector)
        
        imgBtnSilencioGris = resource.get_image("icono_silencio_gris.png")
        self.btnSilencioGris = Boton.Boton(imgBtnSilencioGris, imgBtnSilencioSelec, self.xSelector, self.ySelector)
        
        # imgBtnCuento = Servicios.cargarImagen("icono_cuento.png", self.dirImagenes)
        # imgBtnCuentoSelec = Servicios.cargarImagen("icono_cuento_selec.png", self.dirImagenes)
        imgBtnCuento = resource.get_image("icono_cuento.png")
        imgBtnCuentoSelec = resource.get_image("icono_cuento_selec.png")
        self.btnCuento = Boton.Boton(imgBtnCuento, imgBtnCuentoSelec, self.xSelector + 65, self.ySelector)
        
        imgBtnCuentoGris = resource.get_image("icono_cuento_gris.png")
        self.btnCuentoGris = Boton.Boton(imgBtnCuentoGris, imgBtnCuentoSelec, self.xSelector + 65, self.ySelector)
        
        # imgBtnCita = Servicios.cargarImagen("icono_cita.png", self.dirImagenes)
        # imgBtnCitaSelec = Servicios.cargarImagen("icono_cita_selec.png", self.dirImagenes)
        imgBtnCita = resource.get_image("icono_cita.png")
        imgBtnCitaSelec = resource.get_image("icono_cita_selec.png")
        self.btnCita = Boton.Boton(imgBtnCita, imgBtnCitaSelec, self.xSelector, self.ySelector + 65)
        
        imgBtnCitaGris = resource.get_image("icono_cita_gris.png")
        self.btnCitaGris = Boton.Boton(imgBtnCitaGris, imgBtnCitaSelec, self.xSelector, self.ySelector + 65)
        
        # imgBtnCanto = Servicios.cargarImagen("icono_canto.png", self.dirImagenes)
        # imgBtnCantoSelec = Servicios.cargarImagen("icono_canto_selec.png", self.dirImagenes)
        imgBtnCanto = resource.get_image("icono_canto.png")
        imgBtnCantoSelec = resource.get_image("icono_canto_selec.png")
        self.btnCanto = Boton.Boton(imgBtnCanto, imgBtnCantoSelec, self.xSelector + 65, self.ySelector + 65) 
        
        imgBtnCantoGris = resource.get_image("icono_canto_gris.png")
        self.btnCantoGris = Boton.Boton(imgBtnCantoGris, imgBtnCantoSelec, self.xSelector + 65, self.ySelector + 65) 
        
        if self.mandala is None:
            self.mandala = VentanaMandala.VentanaMandala(self.cursor, self.screen, self.clock, self.ancho, self.alto, "Flor", self)
        
        resource.set_images_path(os.path.join("imagenes"))
        # fondo = Servicios.cargarImagen("Fondo.jpg", os.path.join("imagenes"))
        fondo = resource.get_image("Fondo.jpg")
        
        x = self.ancho - (self.ancho / 2) - (self.background.get_width() / 2)
        y = self.alto - (self.alto / 2) - (self.background.get_height() / 2)
        
        fuenteTitulo = pygame.font.SysFont("helvetica", 30, True)
        
        textoNombre = self.fuenteGrande.render("Bienvenido(a) %s" % (self.personaje.nombre), 1, (255, 255, 255))
        textoInfo = self.fuenteGrande.render("Selecciona un valor presionando uno de los iconos", 1, (255, 255, 255))
        
        selectorAmor = False
        selectorRectitud = False
        selectorPaz = False
        selectorVerdad = False
        selectorNoViolencia = False
        
        valorSelector = ""
        
        #=======================================================================
        # print self.pasoSilencioAmor
        # print self.pasoCuentoAmor
        # print self.pasoCitaAmor
        # print self.pasoCantoAmor
        #=======================================================================
        
        self.pasoAmor = self.pasoSilencioAmor and self.pasoCuentoAmor and self.pasoCitaAmor and self.pasoCantoAmor
        self.pasoRectitud = self.pasoSilencioRectitud and self.pasoCuentoRectitud and self.pasoCitaRectitud and self.pasoCantoRectitud
        self.pasoPaz = self.pasoSilencioPaz and self.pasoCuentoPaz and self.pasoCitaPaz and self.pasoCantoPaz
        self.pasoVerdad = self.pasoSilencioVerdad and self.pasoCuentoVerdad and self.pasoCitaVerdad and self.pasoCantoVerdad
        self.pasoNoViolencia = self.pasoSilencioNoViolencia and self.pasoCuentoNoViolencia and self.pasoCitaNoViolencia and self.pasoCantoNoViolencia
        
        salir = False
        
        while salir == False:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                            
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    
                    if self.cursor.colliderect(self.btnRegresar.rect):
                        salir = True 
                        self.menu.run()
                    if self.cursor.colliderect(self.msjInicio.btn.rect):
                        self.msjInicio.visible = False
                        self.audio.stop()
                        self.sonido.play(-1)
                        self.intro = False
# SILENCIO            
                    if self.cursor.colliderect(self.btnSilencioGris.rect) or self.cursor.colliderect(self.btnSilencio.rect):
                        
                        if valorSelector == "amor":
                            salir = True
                            self.sonido.stop()
                            self.mandala.setTipo("Flor")
                            self.mandala.run()
                            
                        if valorSelector == "rectitud":
                                salir = True
                                self.sonido.stop()
                                self.mandala.setTipo("Sol")
                                self.mandala.run()
                        
                        if valorSelector == "paz":
                                salir = True
                                self.sonido.stop()
                                self.mandala.setTipo("Hojas")
                                self.mandala.run()
                                
                        if valorSelector == "verdad":
                                salir = True
                                self.sonido.stop()
                                self.mandala.setTipo("Nino")
                                self.mandala.run()
                                
                        if valorSelector == "noviolencia":
                                salir = True
                                self.sonido.stop()
                                self.mandala.setTipo("Flor2")
                                self.mandala.run()
# CUENTO                               
                    if self.cursor.colliderect(self.btnCuentoGris.rect) or self.cursor.colliderect(self.btnCuento.rect):
                        
                        if valorSelector == "amor":
                            salir = True
                            self.sonido.stop()
                            self.cuento = Amor.Amor(self.cursor, self.screen, self.clock, self)
                            self.cuento.run()
                            
                        if valorSelector == "rectitud":
                                salir = True
                                self.sonido.stop()
                                self.cuento = Rectitud.Rectitud(self.cursor, self.screen, self.clock, self)
                                self.cuento.run()
                        
                        if valorSelector == "paz":
                                salir = True
                                self.sonido.stop()
                                self.cuento = pazSemillas.PazSemillas(self.cursor, self.screen, self.clock, self)
                                self.cuento.run()
                                
                        if valorSelector == "verdad":
                                salir = True
                                self.sonido.stop()
                                self.cuento = pacman.Pacman(self.cursor, self.screen, self.clock, self)
                                self.cuento.run()
                                
                        if valorSelector == "noviolencia":
                                salir = True
                                self.sonido.stop()
                                self.cuento = puzzle.Puzzle(self.cursor, self.screen, self.clock, self)
                                self.cuento.run()
# CITA                                
                    if self.cursor.colliderect(self.btnCitaGris.rect) or self.cursor.colliderect(self.btnCita.rect):
                        
                        if valorSelector == "amor":
                            salir = True
                            self.sonido.stop()
                            if self.cita is None :
                                self.cita = Cita.Cita(self.screen, self.clock, self.cursor, 1, self)
                            self.cita.setTipo(1)
                            self.cita.run()
                            
                        if valorSelector == "rectitud":
                                salir = True
                                self.sonido.stop()
                                if self.cita is None :
                                    self.cita = Cita.Cita(self.screen, self.clock, self.cursor, 2, self)
                                self.cita.setTipo(2)
                                self.cita.run()
                        
                        if valorSelector == "paz":
                                salir = True
                                self.sonido.stop()
                                if self.cita is None :
                                    self.cita = Cita.Cita(self.screen, self.clock, self.cursor, 3, self)
                                self.cita.setTipo(3)
                                self.cita.run()
                                
                        if valorSelector == "verdad":
                                salir = True
                                self.sonido.stop()
                                if self.cita is None :
                                    self.cita = Cita.Cita(self.screen, self.clock, self.cursor, 4, self)
                                self.cita.setTipo(4)
                                self.cita.run()
                                
                        if valorSelector == "noviolencia":
                                salir = True
                                self.sonido.stop()
                                if self.cita is None :
                                    self.cita = Cita.Cita(self.screen, self.clock, self.cursor, 5, self)
                                self.cita.setTipo(5)
                                self.cita.run()
# CANTO                    
                    if self.cursor.colliderect(self.btnCantoGris.rect) or self.cursor.colliderect(self.btnCanto.rect):
                        
                        if valorSelector == "amor":
                            salir = True
                            self.sonido.stop()
                            self.canto = Karaoke.Karaoke(self.cursor, self.screen, self.clock, 1, self)
                            self.canto.run()
                            
                        if valorSelector == "rectitud":
                                salir = True
                                self.sonido.stop()
                                self.canto = Karaoke.Karaoke(self.cursor, self.screen, self.clock, 2, self)
                                self.canto.run()
                        
                        if valorSelector == "paz":
                                salir = True
                                self.sonido.stop()
                                self.canto = Karaoke.Karaoke(self.cursor, self.screen, self.clock, 3, self)
                                self.canto.run()
                                
                        if valorSelector == "verdad":
                                salir = True
                                self.sonido.stop()
                                self.canto = Karaoke.Karaoke(self.cursor, self.screen, self.clock, 4, self)
                                self.canto.run()
                                
                        if valorSelector == "noviolencia":
                                salir = True
                                self.sonido.stop()
                                self.canto = Karaoke.Karaoke(self.cursor, self.screen, self.clock, 5, self)
                                self.canto.run()

                    if self.cursor.colliderect(self.areaAmor):
                        print "Click en amor"
                        
                        self.sonido2 = self.sonidoAmor
                        # self.sonido2 = Servicios.cargarSonido("amor_instrum.ogg", os.path.join("audios"))
                        
                        valorSelector = "amor"
                        
                        self.xSelector = 658 + 10
                        self.ySelector = 523 + 15
                        
                        if self.pasoSilencioAmor:
                            self.btnSilencio.setCoord(self.xSelector, self.ySelector)
                            self.btnSilencioGris.setCoord(0, -200)
                        else:
                            self.btnSilencioGris.setCoord(self.xSelector, self.ySelector)
                            self.btnSilencio.setCoord(0, -200)
                        
                        if self.pasoCuentoAmor:
                            self.btnCuento.setCoord(self.xSelector + 65, self.ySelector)
                            self.btnCuentoGris.setCoord(0, -200)
                        else:
                            self.btnCuentoGris.setCoord(self.xSelector + 65, self.ySelector)
                            self.btnCuento.setCoord(0, -200)
                        if self.pasoCitaAmor:
                            self.btnCita.setCoord(self.xSelector, self.ySelector + 65)
                            self.btnCitaGris.setCoord(0, -200)
                        else:
                            self.btnCitaGris.setCoord(self.xSelector, self.ySelector + 65)
                            self.btnCita.setCoord(0, -200)
                        if self.pasoCantoAmor:
                            self.btnCanto.setCoord(self.xSelector + 65, self.ySelector + 65)
                            self.btnCantoGris.setCoord(0, -200)
                        else:
                            self.btnCantoGris.setCoord(self.xSelector + 65, self.ySelector + 65)
                            self.btnCanto.setCoord(0, -200)
                        # salir = True
                        # self.sonido.stop()
                        # self.mandala.setTipo("Flor")
                        # self.mandala.run()
                        
                    
                    if self.cursor.colliderect(self.areaRectitud):
                        print "Click en rectitud"
                        
  #------                      if self.pasoAmor:
                        
                        self.sonido2 = self.sonidoRectitud
                        # self.sonido2 = Servicios.cargarSonido("rectitud_instrum.ogg", os.path.join("audios"))
                        
                        valorSelector = "rectitud"
                                
                        self.xSelector = 743 + 10
                        self.ySelector = 275 + 15
                                
                        if self.pasoSilencioRectitud:
                            self.btnSilencio.setCoord(self.xSelector, self.ySelector)
                            self.btnSilencioGris.setCoord(0, -200)
                        else:
                            self.btnSilencioGris.setCoord(self.xSelector, self.ySelector)
                            self.btnSilencio.setCoord(0, -200)
                        
                        if self.pasoCuentoRectitud:
                            self.btnCuento.setCoord(self.xSelector + 65, self.ySelector)
                            self.btnCuentoGris.setCoord(0, -200)
                        else:
                            self.btnCuentoGris.setCoord(self.xSelector + 65, self.ySelector)
                            self.btnCuento.setCoord(0, -200)
                        if self.pasoCitaRectitud:
                            self.btnCita.setCoord(self.xSelector, self.ySelector + 65)
                            self.btnCitaGris.setCoord(0, -200)
                        else:
                            self.btnCitaGris.setCoord(self.xSelector, self.ySelector + 65)
                            self.btnCita.setCoord(0, -200)
                        if self.pasoCantoRectitud:
                            self.btnCanto.setCoord(self.xSelector + 65, self.ySelector + 65)
                            self.btnCantoGris.setCoord(0, -200)
                        else:
                            self.btnCantoGris.setCoord(self.xSelector + 65, self.ySelector + 65)
                            self.btnCanto.setCoord(0, -200)
                            
                            # if self.pasoAmor:
                            # self.mandala.setTipo("Sol")
                            # self.sonido.stop()
                            # salir = True
                            # self.mandala.run()
                            
                    if self.cursor.colliderect(self.areaPaz):
                        print "Click en paz"
                        
  #------                      if self.pasoRectitud:
                        
                        self.sonido2 = self.sonidoPaz
                        # self.sonido2 = Servicios.cargarSonido("paz_instrum.ogg", os.path.join("audios"))
                        
                        valorSelector = "paz"
                                
                        self.xSelector = 531 + 10
                        self.ySelector = 118 
                                
                        if self.pasoSilencioPaz:
                            self.btnSilencio.setCoord(self.xSelector, self.ySelector)
                            self.btnSilencioGris.setCoord(0, -200)
                        else:
                            self.btnSilencioGris.setCoord(self.xSelector, self.ySelector)
                            self.btnSilencio.setCoord(0, -200)
                        
                        if self.pasoCuentoPaz:
                            self.btnCuento.setCoord(self.xSelector + 65, self.ySelector)
                            self.btnCuentoGris.setCoord(0, -200)
                        else:
                            self.btnCuentoGris.setCoord(self.xSelector + 65, self.ySelector)
                            self.btnCuento.setCoord(0, -200)
                        if self.pasoCitaPaz:
                            self.btnCita.setCoord(self.xSelector, self.ySelector + 65)
                            self.btnCitaGris.setCoord(0, -200)
                        else:
                            self.btnCitaGris.setCoord(self.xSelector, self.ySelector + 65)
                            self.btnCita.setCoord(0, -200)
                        if self.pasoCantoPaz:
                            self.btnCanto.setCoord(self.xSelector + 65, self.ySelector + 65)
                            self.btnCantoGris.setCoord(0, -200)
                        else:
                            self.btnCantoGris.setCoord(self.xSelector + 65, self.ySelector + 65)
                            self.btnCanto.setCoord(0, -200)
                            # if self.pasoRectitud:
                            # self.mandala.setTipo("Hojas")
                            # salir = True
                            # self.sonido.stop()
                            # self.mandala.run()
                            
                    if self.cursor.colliderect(self.areaVerdad):
                        print "Click en verdad"
                        
  #------                      if self.pasoPaz:
                        
                        self.sonido2 = self.sonidoVerdad
                        # self.sonido2 = Servicios.cargarSonido("noViolencia_instrum.ogg", os.path.join("audios"))
                        
                        valorSelector = "verdad"
                                
                        self.xSelector = 316 + 10
                        self.ySelector = 275 + 15
                                
                        if self.pasoSilencioVerdad:
                            self.btnSilencio.setCoord(self.xSelector, self.ySelector)
                            self.btnSilencioGris.setCoord(0, -200)
                        else:
                            self.btnSilencioGris.setCoord(self.xSelector, self.ySelector)
                            self.btnSilencio.setCoord(0, -200)
                        
                        if self.pasoCuentoVerdad:
                            self.btnCuento.setCoord(self.xSelector + 65, self.ySelector)
                            self.btnCuentoGris.setCoord(0, -200)
                        else:
                            self.btnCuentoGris.setCoord(self.xSelector + 65, self.ySelector)
                            self.btnCuento.setCoord(0, -200)
                        if self.pasoCitaVerdad:
                            self.btnCita.setCoord(self.xSelector, self.ySelector + 65)
                            self.btnCitaGris.setCoord(0, -200)
                        else:
                            self.btnCitaGris.setCoord(self.xSelector, self.ySelector + 65)
                            self.btnCita.setCoord(0, -200)
                        if self.pasoCantoVerdad:
                            self.btnCanto.setCoord(self.xSelector + 65, self.ySelector + 65)
                            self.btnCantoGris.setCoord(0, -200)
                        else:
                            self.btnCantoGris.setCoord(self.xSelector + 65, self.ySelector + 65)
                            self.btnCanto.setCoord(0, -200)
                            # if self.pasoPaz:
                            # self.mandala.setTipo("Nino")
                            # self.sonido.stop()
                            # salir = True
                            # self.mandala.run()
                    
                    if self.cursor.colliderect(self.areaNoViolencia):
                        print "Click en No violencia"
                        
  #------                      if self.pasoVerdad:
                        
                        self.sonido2 = self.sonidoNoViolencia
                        # self.sonido2 = Servicios.cargarSonido("noViolencia_instrum.ogg", os.path.join("audios"))
                        
                        valorSelector = "noviolencia"
                            
                        self.xSelector = 397 + 10
                        self.ySelector = 523 + 15
                                
                        if self.pasoSilencioNoViolencia:
                            self.btnSilencio.setCoord(self.xSelector, self.ySelector)
                            self.btnSilencioGris.setCoord(0, -200)
                        else:
                            self.btnSilencioGris.setCoord(self.xSelector, self.ySelector)
                            self.btnSilencio.setCoord(0, -200)
                        
                        if self.pasoCuentoNoViolencia:
                            self.btnCuento.setCoord(self.xSelector + 65, self.ySelector)
                            self.btnCuentoGris.setCoord(0, -200)
                        else:
                            self.btnCuentoGris.setCoord(self.xSelector + 65, self.ySelector)
                            self.btnCuento.setCoord(0, -200)
                        if self.pasoCitaNoViolencia:
                            self.btnCita.setCoord(self.xSelector, self.ySelector + 65)
                            self.btnCitaGris.setCoord(0, -200)
                        else:
                            self.btnCitaGris.setCoord(self.xSelector, self.ySelector + 65)
                            self.btnCita.setCoord(0, -200)
                        if self.pasoCantoNoViolencia:
                            self.btnCanto.setCoord(self.xSelector + 65, self.ySelector + 65)
                            self.btnCantoGris.setCoord(0, -200)
                        else:
                            self.btnCantoGris.setCoord(self.xSelector + 65, self.ySelector + 65)
                            self.btnCanto.setCoord(0, -200)
                            # if self.pasoVerdad:
                            # self.mandala.setTipo("Flor2")
                            # self.sonido.stop()
                            # salir = True
                            # self.mandala.run()
                        
                    print valorSelector
                    
            
            self.clock.tick(60)
            
            self.cursor.update()
            
            self.screen.blit(fondo, (0, 0))
            
            self.screen.blit(self.background, (x, y))
            
            valorElegido = ""
            
            self.btnRegresar.update(self.screen, self.cursor)
            
            self.msjInicio.update(self.screen, self.cursor)
            
            if self.intro:
                self.msjInicio.visible = True
                #self.btnRegresar.update(self.screen, self.cursor)
            else:
                
                if self.pasoAmor:
                    self.screen.blit(self.imagenAmor, (x, y))
                # else:
                    # self.screen.blit(self.candadoRectitud, (x, y))
                    
                if self.pasoRectitud:
                    self.screen.blit(self.imagenRectitud, (x, y))
                # else:
                    # self.screen.blit(self.candadoPaz, (x, y))
                
                if self.pasoPaz:
                    self.screen.blit(self.imagenPaz, (x, y))
                # else:
                    # self.screen.blit(self.candadoVerdad, (x, y))
                    
                if self.pasoVerdad:
                    self.screen.blit(self.imagenVerdad, (x, y))
                # else:
                    # self.screen.blit(self.candadoNoViolencia, (x, y))
                    
                if self.pasoNoViolencia:
                    self.screen.blit(self.imagenNoViolencia, (x, y))
                    
                    
                
                
                if self.cursor.colliderect(self.areaAmor):
                    valorElegido = "    AMOR    "
                    self.screen.blit(self.imagenAmorSel, (x, y))
                    
                if self.cursor.colliderect(self.areaRectitud):
                    valorElegido = "  RECTITUD  "
                    self.screen.blit(self.imagenRectitudSel, (x, y))
                    if not self.pasoAmor:
                        self.screen.blit(self.candadoRectitud, (x, y))
                        
                if self.cursor.colliderect(self.areaPaz):
                    valorElegido = "     PAZ    "
                    self.screen.blit(self.imagenPazSel, (x, y))
                    if not self.pasoRectitud:
                        self.screen.blit(self.candadoPaz, (x, y))
                    
                if self.cursor.colliderect(self.areaVerdad):
                    valorElegido = "   VERDAD   "
                    self.screen.blit(self.imagenVerdadSel, (x, y))
                    if not self.pasoPaz:
                        self.screen.blit(self.candadoVerdad, (x, y))
                    
                if self.cursor.colliderect(self.areaNoViolencia):
                    valorElegido = "NO VIOLENCIA"
                    self.screen.blit(self.imagenNoViolenciaSel, (x, y))
                    if not self.pasoVerdad:
                        self.screen.blit(self.candadoNoViolencia, (x, y))
                
                
                self.btnSilencio.update(self.screen, self.cursor)
                self.btnSilencioGris.update(self.screen, self.cursor)
                self.btnCuento.update(self.screen, self.cursor)
                self.btnCuentoGris.update(self.screen, self.cursor)
                self.btnCita.update(self.screen, self.cursor)
                self.btnCitaGris.update(self.screen, self.cursor)
                self.btnCanto.update(self.screen, self.cursor)
                self.btnCantoGris.update(self.screen, self.cursor)
                
                
                textoValor = fuenteTitulo.render(valorElegido, 1, (255, 255, 255))
                self.screen.blit(textoValor, (530, 770))
                
                self.screen.blit(textoNombre, (10, 3))
                self.screen.blit(textoInfo, (10, 33))
                
                #===================================================================
                # pygame.draw.rect (self.screen , (100, 100, 100) , self.areaPaz, 2)
                # pygame.draw.rect (self.screen , (100, 100, 100) , self.areaRectitud, 2)
                # pygame.draw.rect (self.screen , (100, 100, 100) , self.areaAmor, 2)
                # pygame.draw.rect (self.screen , (100, 100, 100) , self.areaNoViolencia, 2)
                # pygame.draw.rect (self.screen , (100, 100, 100) , self.areaVerdad, 2)
                #===================================================================

            pygame.display.update()
            
