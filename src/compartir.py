'''
Created on 5/10/2013

@author: Luis
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, os, mouse, json, requests, textBox2, datetime, botonContinuar, botonTerminar
from pygame.locals import *
from textBox import TextBox
from control import resource
from modelo import Boton, MensajeEmergente
class Compartir(object):
    
    
    def __init__(self,screen,cursor, clock, padre):
        resource.set_images_path(os.path.join("imagenes", "compartir"))
        self.background = resource.get_image("fondoCompartir.png")
        
        imgBtnEnviar = resource.get_image("botonEnviar.png")
        imgBtnEnviarSelec = resource.get_image("BotonesEnviar_selec.png")
        
        self.btnEnviar = Boton.Boton(imgBtnEnviar, imgBtnEnviarSelec, 700,550)
        
        
        
        self.screen = screen
        self.clock = clock
        self.tablero = padre

        self.mouse = mouse.Mouse()
        self.cursor = cursor
  
        self.inicio = True
        self.juego = False
        self.terminar = False
        self.envio = False
        self.letreroEnvio = False
        self.letreroNoEnvio = False
        self.CamposVacios = False
        

        self.tb1 = TextBox(position=(460,250),size=(400,25),textsize=22,editable=False)
        self.tb2 = TextBox(position=(460,300),size=(400,25),textsize=22,editable=False)
        self.contendora = textBox2.Contenedora()
        rutaFuente = os.path.join("fuentes", "PatrickHand-Regular.ttf")
        self.font = pygame.font.Font(rutaFuente, 22) 
        self.img=self.font.render("Nombre: ",1,(0,0,0))
        self.img2=self.font.render("Colegio: ",1,(0,0,0))
        self.img3=self.font.render("Mensaje: ",1,(0,0,0))
        
        
        resource.set_images_path(os.path.join("imagenes"))
        imgBtnRegresar = resource.get_image("boton_regresar.png")
        imgBtnRegresarSelec = resource.get_image("boton_regresar_selec.png")
        
        self.background2 = resource.get_image("Fondo.jpg", False)
        
        
        
        self.btnRegresar = Boton.Boton(imgBtnRegresar, imgBtnRegresarSelec, (1200 - 214 - 10), 10)
        
        self.msjInicio = MensajeEmergente.MensajeInicial(30, "Compartir")
        self.msjVacios = MensajeEmergente.MensajeInicial(30, "Compartir2")
        self.msjNoEnvio = MensajeEmergente.MensajeInicial(30, "Compartir3")
        self.msjEnvio = MensajeEmergente.MensajeInicial(30, "Compartir4")
    
    def enviarDatos(self):
        
        if(self.tb1.text=="-" or self.tb1.text=="|" or self.tb1.text=="" or self.tb2.text=="-" or self.tb2.text=="|" or self.tb2.text==""):
            pass
        else:

            try:
                url = 'http://valorar.somee.com/api/Servicio'
                
                payload = {'Nombre':self.tb1.text, 'Msg':self.contendora.texto(), 'Valor':self.valor, 'Colegio':self.tb2.text, 'Actividad':self.actividad, 'Fecha':datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}
                headers = {'content-type': 'application/json'}
                r = requests.post(url, data = json.dumps(payload), headers = headers)
                self.envio = True
                
            except Exception as e:
                    # Se alista todo para una nueva conexion
                    self.envio = False
        
    def reiniciar(self):
        self.inicio = True
        self.juego = False
        self.terminar = False
        self.envio = False
        self.letreroEnvio = False
        self.letreroNoEnvio = False
        self.CamposVacios = False
        
        self.tb1.reiniciar()
        self.tb2.reiniciar()
        self.contendora.reiniciar()
        
    def run(self,valor,actividad):
        
        
        self.valor = valor
        self.actividad = actividad
        self.reiniciar()
        self.tb1.text = self.tablero.personaje.nombre
        self.tb2.text = self.tablero.personaje.colegio
        
        while not self.terminar:
            for event in pygame.event.get():
                if self.juego:
                    self.tb1.Event(event)
                    self.tb2.Event(event)
                self.contendora.Event(event)
                if event.type == pygame.QUIT: 
                    sys.exit()
                   
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.mouse.rect.center = pygame.mouse.get_pos() 
                        
                        if self.cursor.colliderect(self.btnRegresar.rect):
                            self.tablero.sonido2.stop()
                            self.terminar = True
                            self.tablero.sonido.play(-1)
                            self.tablero.run()
                        
                        if self.juego and self.cursor.colliderect(self.btnEnviar.rect):
                            
                            if self.tb1.text.strip() =="" or self.tb2.text.strip() == "" or self.contendora.texto().strip() == "":
                                self.juego = False
                                self.CamposVacios = True
                            else:
                                self.juego = False
                                self.enviarDatos()
                                if self.envio:
                                    self.letreroEnvio = True
                                else:
                                    self.letreroNoEnvio = True
      
                        if self.cursor.colliderect(self.msjInicio.btn.rect) and self.inicio:
                            self.msjInicio.visible = False
                            self.inicio = False
                            self.juego = True
                            
                        elif (self.letreroEnvio and self.cursor.colliderect(self.msjEnvio.btn.rect)) or (self.letreroNoEnvio and self.cursor.colliderect(self.msjNoEnvio.btn.rect)):
                            self.terminar = True
                            self.tablero.sonido2.stop()
                            self.tablero.sonido.play(-1)
                            self.tablero.run()
                            
                        elif self.CamposVacios and self.cursor.colliderect(self.msjVacios.btn.rect):
                            self.msjVacios.visible = False
                            self.juego = True
                            self.CamposVacios = False
                            
                            
                        
                        
                            
                            
            self.screen.fill((0,0,0)) 
            self.screen.blit(self.background2,(0,0))                   
            self.screen.blit(self.background,(0,0))
            
            
            self.screen.blit(self.img,(380,245))   
            self.screen.blit(self.img2,(380,295))      
            self.screen.blit(self.img3,(380,340))   
            self.tb1.Draw(self.screen)
            self.tb2.Draw(self.screen)
            self.contendora.draw(self.screen)
            self.cursor.update()
            
            if self.inicio:
                self.msjInicio.visible = True
                self.btnRegresar.update(self.screen, self.cursor)
                self.msjInicio.update(self.screen, self.cursor)
                
            elif self.juego:
                self.btnRegresar.update(self.screen, self.cursor)
                self.btnEnviar.update(self.screen, self.cursor)
            
            elif self.letreroEnvio:
                self.msjEnvio.update(self.screen, self.cursor)      
                self.msjEnvio.visible = True
                self.btnRegresar.update(self.screen, self.cursor)
            
            elif self.letreroNoEnvio:
                self.msjNoEnvio.update(self.screen, self.cursor)      
                self.msjNoEnvio.visible = True
                self.btnRegresar.update(self.screen, self.cursor)
            
            elif self.CamposVacios:
                self.msjVacios.update(self.screen, self.cursor)      
                self.msjVacios.visible = True
                self.btnRegresar.update(self.screen, self.cursor)
            
            self.clock.tick(60)
            
            
            pygame.display.update() 
            