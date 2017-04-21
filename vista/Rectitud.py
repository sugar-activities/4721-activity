#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, os, sys, random
from control import Servicios
from modelo import ObjetoCaneca, Boton, Caneca, Cursor, MensajeEmergente
from pygame.locals import *

class Rectitud(object):

    def __init__(self, cursor, screen, clock, padre):
        self.dirImagenes = os.path.join("imagenes", "rectitud")
        self.cursor = cursor
        self.screen = screen
        self.clock = clock
        self.audio = Servicios.cargarSonido("rectitud.ogg", os.path.join("audios", "cuentos"))
        
        self.tablero = padre
        self.personaje = self.tablero.personaje
        
        self.botonContinuar = Boton.BotonContinuar()
        self.botonTerminar = Boton.BotonTerminar()
        
        self.msjInicio = MensajeEmergente.MensajeInicial(40, "CuentoRectitud")
        self.msjGanaste = MensajeEmergente.MensajeGanaste(28, "JuegoRectitud")

        self.transparente = pygame.image.load(os.path.join("imagenes", "transparente.png")).convert_alpha()
        
        self.mouse = Cursor.Mouse()
        
        
        self.fondo = Servicios.cargarImagen("fondo_rectitud.png", self.dirImagenes)
       
        self.gano = False
        
        self.objeto = None
        
        imgBtnRegresar = Servicios.cargarImagen("boton_regresar.png", "imagenes")
        imgBtnRegresarSelec = Servicios.cargarImagen("boton_regresar_selec.png", "imagenes")
        
        self.btnRegresar = Boton.Boton(imgBtnRegresar, imgBtnRegresarSelec, (1200 - 214 - 10), 10)
        
    def run(self):
        
        self.personaje.setAncho(100)
        self.personaje.setX(10)
        self.personaje.setY(385)
        
        anchoCanecas = 100 
        xICanecas = 850
        deltaXCanecas = anchoCanecas + 10
        yICanecas = 700
        
        canecaAzul = Caneca.Caneca(xICanecas, yICanecas, anchoCanecas, 1)
        canecaBlanca = Caneca.Caneca(xICanecas + deltaXCanecas , yICanecas, anchoCanecas, 2)
        canecaGris = Caneca.Caneca(xICanecas + 2 * deltaXCanecas, yICanecas, anchoCanecas, 3)
        
        canecaAzul.setAncho2(anchoCanecas + 30)
        canecaBlanca.setAncho2(anchoCanecas + 30)
        canecaGris.setAncho2(anchoCanecas + 30)
        
        
        y2 = canecaAzul.alto2
        
        
        canecaAzul.setCoord2(330, (480 / 2 - y2 / 2))
        canecaBlanca.setCoord2(420, (480 / 2 - y2 / 2))
        canecaGris.setCoord2(510, (480 / 2 - y2 / 2))
        
        
        xAzul = canecaAzul.x2 + 260
        xBlanca = canecaBlanca.x2 + 300
        xGris = canecaGris.x2 + 340
        
        y = canecaGris.y2 + 200
        
        canecaAzul.setCoord2(xAzul, y)
        canecaGris.setCoord2(xGris, y)
        canecaBlanca.setCoord2(xBlanca, y)
        
        canecaAzul.setAnchoInfo(anchoCanecas + 110)
        canecaBlanca.setAnchoInfo(anchoCanecas + 110)
        canecaGris.setAnchoInfo(anchoCanecas + 110)
        
        yInfo = canecaAzul.altoInfo
        
        canecaAzul.setCoordInfo(300, (825 / 2 - yInfo / 2 - 25))
        canecaBlanca.setCoordInfo(550, (825 / 2 - yInfo / 2 - 25))
        canecaGris.setCoordInfo(800, (825 / 2 - yInfo / 2 - 25))
        
        obj1 = ObjetoCaneca.ObjetoCaneca(255, 600, 60, random.randint(1, 3), random.randint(1, 4))
        obj2 = ObjetoCaneca.ObjetoCaneca(100, 720, 60, random.randint(1, 3), random.randint(1, 4))
        obj3 = ObjetoCaneca.ObjetoCaneca(600, 580, 60, random.randint(1, 3), random.randint(1, 4))
        obj4 = ObjetoCaneca.ObjetoCaneca(1065, 570, 60, random.randint(1, 3), random.randint(1, 4))
        obj5 = ObjetoCaneca.ObjetoCaneca(630, 685, 60, random.randint(1, 3), random.randint(1, 4))
        
        listaObjetos = []
        objActual = 0
        
        puedeMoverse = True
        
        encontro1 = False
        encontro2 = False
        encontro3 = False
        encontro4 = False
        encontro5 = False
        
        guardo1 = False
        guardo2 = False
        guardo3 = False
        guardo4 = False
        guardo5 = False
        
        sonido2Sonando = False
        
        guardoTodos = False
        
        vioMensaje = False
        popUpFaltanVisible = False
        popUpTerminoVisible = False
        popUpAyudaVisible = False
        botandoBasura = False
        
        pasoSonidoExito = False
        
        fuenteTitulo = pygame.font.SysFont("helvetica", 28, True)
        fuenteTexto = pygame.font.SysFont("helvetica", 20)
        fuenteTextoN = pygame.font.SysFont("helvetica", 20, True)
        
        imgEncontro = Servicios.cargarImagen("letreroEncontro.png", self.dirImagenes)
        imgFalta = Servicios.cargarImagen("letreroFalta.png", self.dirImagenes)
        imgTermino = Servicios.cargarImagen("letreroTermino.png", self.dirImagenes)
        imgBotando = Servicios.cargarImagen("letreroBotandoBasura.png", self.dirImagenes)
        
        xImgEncontro = (1200 / 2) - (imgEncontro.get_width() / 2)
        xImgFalta = (1200 / 2) - (imgFalta.get_width() / 2)
        xImgTermino = (1200 / 2) - (imgTermino.get_width() / 2)
        xImgBotando = (1200 / 2) - (imgBotando.get_width() / 2)
        
        yImgEncontro = (825 / 2) - (imgEncontro.get_height() / 2)
        yImgFalta = (825 / 2) - (imgFalta.get_height() / 2)
        yImgTermino = (825 / 2) - (imgTermino.get_height() / 2)
        yImgBotando = (825 / 2) - (imgBotando.get_height() / 2)
        
        imgBtnRecoger = Servicios.cargarImagen("boton_continuar.png", "imagenes")
        imgBtnRecogerSelec = Servicios.cargarImagen("boton_continuar_selec.png", "imagenes")
            
        btnRecoger = Boton.Boton(imgBtnRecoger, imgBtnRecogerSelec, (1200 / 2) - (imgBtnRecoger.get_width() / 2), 600)
        
        imgBtnAceptar = Servicios.cargarImagen("boton_continuar.png", "imagenes")
        imgBtnAceptarSelec = Servicios.cargarImagen("boton_continuar_selec.png", "imagenes")
            
        btnAceptar = Boton.Boton(imgBtnAceptar, imgBtnAceptarSelec, (1200 / 2) - (imgBtnAceptar.get_width() / 2), 400)
        
        imgBtnAceptar2 = Servicios.cargarImagen("boton_continuar.png", "imagenes")
        imgBtnAceptar2Selec = Servicios.cargarImagen("boton_continuar_selec.png", "imagenes")
            
        btnAceptar2 = Boton.Boton(imgBtnAceptar2, imgBtnAceptar2Selec, (1200 / 2) - (imgBtnAceptar.get_width() / 2), 600)
        
        imgBtnAyuda = Servicios.cargarImagen("botonAyuda.png", self.dirImagenes)
        imgBtnAyudaSelec = Servicios.cargarImagen("botonAyuda.png", self.dirImagenes)
            
        btnAyuda = Boton.Boton(imgBtnAyuda, imgBtnAyudaSelec, (1200 / 2) - (imgBtnAceptar.get_width() / 2), 600)
        
        pygame.key.set_repeat(1, 25)  # Activa repeticion de teclas
        
        
        
        inicio = True
        juego = False
        gano = False
        
        moviendose = False
        mov = ""
        
        self.gano = False
        
        
        
        self.audio.play()

        while self.gano == False:
            
            self.clock.tick(60)
            
            self.cursor.update()
            
            self.screen.blit(self.fondo, (0, 0))
            
            self.msjInicio.update(self.screen, self.cursor)
            self.msjGanaste.update(self.screen, self.cursor)
            
            if inicio:
                self.msjInicio.visible = True
                self.btnRegresar.update(self.screen, self.cursor)
            
            elif juego:
                
                self.btnRegresar.update(self.screen, self.cursor)
            
                
                if moviendose:
                    self.personaje.dibujarMov(self.screen, mov)
                else:
                    self.personaje.dibujar(self.screen)
                
                if encontro1 == False and guardo1 == False:
                    self.screen.blit(obj1.imagen, (obj1.x, obj1.y))   
                if encontro2 == False and guardo2 == False:
                    self.screen.blit(obj2.imagen, (obj2.x, obj2.y))    
                if encontro3 == False and guardo3 == False:
                    self.screen.blit(obj3.imagen, (obj3.x, obj3.y))
                if encontro4 == False and guardo4 == False:
                    self.screen.blit(obj4.imagen, (obj4.x, obj4.y))
                if encontro5 == False and guardo5 == False:
                    self.screen.blit(obj5.imagen, (obj5.x, obj5.y))
                
                self.screen.blit(canecaGris.imagen, (canecaGris.x, canecaGris.y))
                self.screen.blit(canecaBlanca.imagen, (canecaBlanca.x, canecaBlanca.y))
                self.screen.blit(canecaAzul.imagen, (canecaAzul.x, canecaAzul.y))
                
                if encontro1 == True:
                    puedeMoverse = False
                    self.screen.blit(self.transparente, (0, 0))
                    self.screen.blit(imgEncontro, (xImgEncontro, yImgEncontro))
                    obj1.setAncho(150)
                    self.screen.blit(obj1.imagen, ((1200 / 2) - (obj1.ancho / 2), 350))
                    # texto = fuenteTitulo.render("Encontraste un objeto", 1, (0, 0, 0))
                    nombre = fuenteTexto.render(obj1.nombre, 1, (0, 0, 0))
                    # self.screen.blit(texto, (210, 60))
                    self.screen.blit(nombre, ((1200 / 2) - (obj1.ancho / 2), 315))
                    btnRecoger.update(self.screen, self.cursor)
                    
                if encontro2 == True:
                    puedeMoverse = False
                    self.screen.blit(self.transparente, (0, 0))
                    self.screen.blit(imgEncontro, (xImgEncontro, yImgEncontro))
                    obj2.setAncho(150)
                    self.screen.blit(obj2.imagen, ((1200 / 2) - (obj2.ancho / 2), 350))
                    # texto = fuenteTitulo.render("Encontraste un objeto", 1, (0, 0, 0))
                    nombre = fuenteTexto.render(obj2.nombre, 1, (0, 0, 0))
                    # self.screen.blit(texto, (200, 60))
                    self.screen.blit(nombre, ((1200 / 2) - (obj2.ancho / 2), 315))
                    btnRecoger.update(self.screen, self.cursor)
                    
                if encontro3 == True:
                    puedeMoverse = False
                    self.screen.blit(self.transparente, (0, 0))
                    self.screen.blit(imgEncontro, (xImgEncontro, yImgEncontro))
                    obj3.setAncho(150)
                    self.screen.blit(obj3.imagen, ((1200 / 2) - (obj3.ancho / 2), 350))
                    # texto = fuenteTitulo.render("Encontraste un objeto", 1, (0, 0, 0))
                    nombre = fuenteTexto.render(obj3.nombre, 1, (0, 0, 0))
                    # self.screen.blit(texto, (200, 60))
                    self.screen.blit(nombre, ((1200 / 2) - (obj3.ancho / 2), 315))
                    btnRecoger.update(self.screen, self.cursor)
                    
                if encontro4 == True:
                    puedeMoverse = False
                    self.screen.blit(self.transparente, (0, 0))
                    self.screen.blit(imgEncontro, (xImgEncontro, yImgEncontro))
                    obj4.setAncho(150)
                    self.screen.blit(obj4.imagen, ((1200 / 2) - (obj4.ancho / 2), 350))
                    # texto = fuenteTitulo.render("Encontraste un objeto", 1, (0, 0, 0))
                    nombre = fuenteTexto.render(obj4.nombre, 1, (0, 0, 0))
                    # self.screen.blit(texto, (200, 60))
                    self.screen.blit(nombre, ((1200 / 2) - (obj4.ancho / 2), 315))
                    btnRecoger.update(self.screen, self.cursor)
                    
                if encontro5 == True:
                    puedeMoverse = False
                    self.screen.blit(self.transparente, (0, 0))
                    self.screen.blit(imgEncontro, (xImgEncontro, yImgEncontro))
                    obj5.setAncho(150)
                    self.screen.blit(obj5.imagen, ((1200 / 2) - (obj5.ancho / 2), 350))
                    # texto = fuenteTitulo.render("Encontraste un objeto", 1, (0, 0, 0))
                    nombre = fuenteTexto.render(obj5.nombre, 1, (0, 0, 0))
                    # self.screen.blit(texto, (200, 60))
                    self.screen.blit(nombre, ((1200 / 2) - (obj5.ancho / 2), 315))
                    btnRecoger.update(self.screen, self.cursor)
                
                if guardoTodos == True and vioMensaje == False:
                    puedeMoverse = False
                    self.screen.blit(self.transparente, (0, 0))
                    self.screen.blit(imgTermino, (xImgTermino, yImgTermino))
                    # texto = fuenteTitulo.render("Has recogido todos los objetos ", 1, (0, 0, 0))
                    # texto2 = fuenteTexto.render("Ahora debes ponerlos en su lugar. Dirigete a las canecas. ", 1, (0, 0, 0))
                    # self.screen.blit(texto, (150, 130))
                    # self.screen.blit(texto2, (120, 200))
                    btnAceptar.update(self.screen, self.cursor)
                
                if guardo1 == True and guardo2 == True and guardo3 == True and guardo4 == True and guardo5 == True:
                    guardoTodos = True     
                    
                if self.personaje.rect.colliderect(obj1.rect):
                    print "colisiono con objeto 1", obj1.nombre
                    obj1.setCoord(0, 0)
                    encontro1 = True     
                
                if self.personaje.rect.colliderect(obj2.rect):
                    print "colisiono con objeto 2", obj2.nombre
                    obj2.setCoord(0, 0)
                    encontro2 = True  
                
                if self.personaje.rect.colliderect(obj3.rect):
                    print "colisiono con objeto 3", obj3.nombre
                    obj3.setCoord(0, 0)
                    encontro3 = True  
                    
                if self.personaje.rect.colliderect(obj4.rect):
                    print "colisiono con objeto 4", obj4.nombre
                    obj4.setCoord(0, 0)
                    encontro4 = True  
                    
                if self.personaje.rect.colliderect(obj5.rect):
                    print "colisiono con objeto 5", obj5.nombre
                    obj5.setCoord(0, 0)
                    encontro5 = True
                    
                if self.personaje.rect.colliderect(canecaAzul.rect) or self.personaje.rect.colliderect(canecaBlanca.rect) or self.personaje.rect.colliderect(canecaGris.rect):
                    # print "colisiono con canecas"
                    if guardoTodos == False:
                        popUpFaltanVisible = True
                    else:
                        popUpTerminoVisible = True
                        
                if popUpFaltanVisible:
                    puedeMoverse = False
                    self.screen.blit(self.transparente, (0, 0))
                    self.screen.blit(imgFalta, (xImgFalta, yImgFalta))
                    # texto = fuenteTitulo.render("Faltan objetos por recoger", 1, (0, 0, 0))
                    # texto2 = fuenteTexto.render("Cuando recojas todos los objetos podras depositarlos en las canecas.", 1, (0, 0, 0))
                    # self.screen.blit(texto, (180, 130))
                    # self.screen.blit(texto2, (60, 200))
                    btnAceptar.update(self.screen, self.cursor)
                    
                if popUpTerminoVisible:
                    puedeMoverse = False
                    botandoBasura = True
                    self.screen.blit(self.transparente, (0, 0))
                    self.screen.blit(imgBotando, (xImgBotando, yImgBotando))
                    
                    if objActual < len(listaObjetos):
                    
                        self.objeto = listaObjetos[objActual]
                        
                        # texto = fuenteTitulo.render("Poniendo la basura en su lugar", 1, (0, 0, 0))
                        textoObjeto = fuenteTextoN.render("Objeto: %s" % (self.objeto.nombre), 1, (0, 0, 0))
                        textoCanecas = fuenteTextoN.render("Canecas", 1, (0, 0, 0))
                        # textoInfo = fuenteTexto.render("Haz click en la caneca adecuada para depositar el objeto.", 1, (0, 0, 0))
                        # self.screen.blit(texto, (160, 60))
                        self.screen.blit(textoObjeto, (340, 130 + 200))
                        self.screen.blit(textoCanecas, (canecaAzul.x2, 130 + 200))
                        # self.screen.blit(textoInfo, (120, 100))
                        self.screen.blit(canecaGris.imagen2, (canecaGris.x2, canecaGris.y2))
                        self.screen.blit(canecaBlanca.imagen2, (canecaBlanca.x2, canecaBlanca.y2))
                        self.screen.blit(canecaAzul.imagen2, (canecaAzul.x2, canecaAzul.y2))
                                            
                        self.screen.blit(self.objeto.imagen, (340, 160 + 200))
    
                        btnAyuda.update(self.screen, self.cursor)
    # GANOOOOOOOOO                    
                    else:
                        # self.gano = True
                        # self.cita.run()
                        gano = True
                        juego = False
                        
                
                if popUpAyudaVisible:
                    botandoBasura = False
                    self.screen.blit(imgBotando, (xImgBotando, yImgBotando))
                    self.screen.blit(canecaGris.imagenInfo, (canecaGris.xInfo, canecaGris.yInfo))
                    self.screen.blit(canecaBlanca.imagenInfo, (canecaBlanca.xInfo, canecaBlanca.yInfo))
                    self.screen.blit(canecaAzul.imagenInfo, (canecaAzul.xInfo, canecaAzul.yInfo))
                    btnAceptar2.update(self.screen, self.cursor)      
            
            elif gano:
                if pasoSonidoExito == False:
                    self.tablero.sonidoExito.play()
                    pasoSonidoExito = True
                
                self.msjGanaste.visible = True 
                    
                #===============================================================
                # self.screen.blit(self.transparente, (0, 0))
                # self.screen.blit(self.letrero, (380, 100))
                # self.screen.blit(self.botonTerminar.image, self.botonTerminar.rect)
                #===============================================================
            
            pygame.display.flip()
            
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
                        if sonido2Sonando == False:
                            sonido2Sonando = True
                            self.tablero.sonido2.play(-1)
                        inicio = False
                        juego = True
                    
                    if self.cursor.colliderect(self.msjGanaste.btn.rect):
                        self.msjGanaste.visible = False
                        pygame.key.set_repeat(1000, 25)
                        self.tablero.sonido2.stop()
                        self.gano = True
                        # self.cita.run()
                        self.tablero.pasoCuentoRectitud = True
                        self.tablero.compartir.run("Rectitud", "Juego")
                    
                    if botandoBasura:
                        if self.cursor.colliderect(canecaAzul.rect2):
                            if self.objeto.caneca == 1:
                                print "bien"
                                objActual += 1
                            else:
                                print "mal"
                                
                    
                        if self.cursor.colliderect(canecaBlanca.rect2):
                            if self.objeto.caneca == 2:
                                print "bien"
                                objActual += 1
                            else:
                                print "mal"
                        
                        if self.cursor.colliderect(canecaGris.rect2):
                            if self.objeto.caneca == 3:
                                print "bien"
                                objActual += 1
                            else:
                                print "mal"
                        
                    
                    
                    
                    if self.cursor.colliderect(btnRecoger.rect):
                        if encontro1 == True:
                            guardo1 = True
                            encontro1 = False
                            listaObjetos.append(obj1)
                        if encontro2 == True:
                            guardo2 = True
                            encontro2 = False
                            listaObjetos.append(obj2)
                        if encontro3 == True:
                            guardo3 = True
                            encontro3 = False
                            listaObjetos.append(obj3)
                        if encontro4 == True:
                            guardo4 = True
                            encontro4 = False
                            listaObjetos.append(obj4)
                        if encontro5 == True:
                            guardo5 = True
                            encontro5 = False
                            listaObjetos.append(obj5)
                        puedeMoverse = True
                    
                    if self.cursor.colliderect(btnAceptar.rect):
                        if guardoTodos == True:
                            vioMensaje = True
                            puedeMoverse = True
                        if popUpFaltanVisible:
                            popUpFaltanVisible = False
                            puedeMoverse = True
                            self.personaje.setX(self.personaje.x - 5)
                            self.personaje.setY(self.personaje.y - 5)
                     
                    if self.cursor.colliderect(btnAyuda.rect):
                        if popUpTerminoVisible and popUpAyudaVisible == False:
                            popUpAyudaVisible = True
                        else:
                            popUpAyudaVisible = False  
                        
                elif event.type == pygame.KEYDOWN:
                    if puedeMoverse:
                        if event.key == K_UP:
                            if self.personaje.y >= 350:
                                moviendose = True
                                mov = "arriba"
                                self.personaje.setY(self.personaje.y - 5)
                        elif event.key == K_DOWN:
                            if self.personaje.y <= 650:
                                moviendose = True
                                mov = "abajo"    
                                self.personaje.setY(self.personaje.y + 5)
                        elif event.key == K_RIGHT:  
                            if self.personaje.x <= 1100:
                                moviendose = True
                                mov = "der"
                                self.personaje.setX(self.personaje.x + 5)
                        elif event.key == K_LEFT:
                            if self.personaje.x >= 0:
                                moviendose = True
                                mov = "izq"
                                self.personaje.setX(self.personaje.x - 5)
                                
                elif event.type == pygame.KEYUP:
                    moviendose = False
            
