'''
Created on 14/07/2013

@author: Luis
'''
import pygame, os
from pygame.locals import *
from widget import Widget


class Contenedora:
    def __init__(self,parent=None,text="",editable=True):
        self.caracteresMaximo = 44
        self.tb4 = TextBox2(position=(460,350),size=(400,25),textsize=22)
        self.tb5 = TextBox2(position=(460,375),size=(400,25),textsize=22)
        self.tb6 = TextBox2(position=(460,400),size=(400,25),textsize=22)
        self.tb7 = TextBox2(position=(460,425),size=(400,25),textsize=22)
        self.tb8 = TextBox2(position=(460,450),size=(400,25),textsize=22)
        self.tb9 = TextBox2(position=(460,475),size=(400,25),textsize=22)
        self.tb10 = TextBox2(position=(460,500),size=(400,25),textsize=22)
        self.tb11 = TextBox2(position=(460,525),size=(400,25),textsize=22)
        self.active = False
        self.editable = editable
        self.text =text
    
    def draw(self,screen):
        self.tb4.Draw(screen)
        self.tb5.Draw(screen)
        self.tb6.Draw(screen)
        self.tb7.Draw(screen)
        self.tb8.Draw(screen)
        self.tb9.Draw(screen)
        self.tb10.Draw(screen)
        self.tb11.Draw(screen)
    
    def reiniciar(self):
        self.tb4.reiniciar()
        self.tb5.reiniciar()
        self.tb6.reiniciar()
        self.tb7.reiniciar()
        self.tb8.reiniciar()
        self.tb9.reiniciar()
        self.tb10.reiniciar()
        self.tb11.reiniciar()
        self.active = False
        self.text = ""
    
    def texto(self):
        return self.tb4.text+""+self.tb5.text+""+self.tb6.text+""+self.tb7.text+""+self.tb8.text+""+self.tb9.text+""+self.tb10.text+""+self.tb11.text
    
    def Event(self,event):
        mx,my=pygame.mouse.get_pos()
        #changeing active status
        
        click = self.tb4.IsUnder((mx,my)) or self.tb5.IsUnder((mx,my)) or self.tb6.IsUnder((mx,my)) or self.tb7.IsUnder((mx,my)) or self.tb8.IsUnder((mx,my)) or self.tb9.IsUnder((mx,my)) or self.tb10.IsUnder((mx,my)) or self.tb11.IsUnder((mx,my))
        
        if click and event.type==pygame.MOUSEBUTTONDOWN and self.editable==True:
            if pygame.mouse.get_pressed()[0]==1:
                self.active=True
                if(len(self.tb4.text)<self.caracteresMaximo):
                    self.tb4.active=True
                elif(len(self.tb5.text)<self.caracteresMaximo):
                    self.tb5.active=True
                elif(len(self.tb6.text)<self.caracteresMaximo):
                    self.tb6.active=True
                elif(len(self.tb7.text)<self.caracteresMaximo):
                    self.tb7.active=True
                elif(len(self.tb8.text)<self.caracteresMaximo):
                    self.tb8.active=True
                elif(len(self.tb9.text)<self.caracteresMaximo):
                    self.tb9.active=True
                elif(len(self.tb10.text)<self.caracteresMaximo):
                    self.tb10.active=True
                elif(len(self.tb11.text)<self.caracteresMaximo):
                    self.tb11.active=True
        elif event.type==pygame.MOUSEBUTTONDOWN:
            self.active=False
            self.tb4.active=False
            self.tb5.active=False
            self.tb6.active=False
            self.tb7.active=False
            self.tb8.active=False
            self.tb9.active=False
            self.tb10.active=False
            self.tb11.active=False
        #keyboard events1
        if self.active==True and event.type==pygame.KEYDOWN:
            if event.key==pygame.K_BACKSPACE:
                if(len(self.tb11.text)>0):
                    if len(self.tb11.text)==1:
                        self.tb11.active=False
                        self.tb10.active=True
                    self.tb11.text=self.tb11.text[:-1]
                elif(len(self.tb10.text)>0):
                    if len(self.tb10.text)==1:
                        self.tb10.active=False
                        self.tb9.active=True
                    self.tb10.text=self.tb10.text[:-1]
                elif(len(self.tb9.text)>0):
                    if len(self.tb9.text)==1:
                        self.tb9.active=False
                        self.tb8.active=True
                    self.tb9.text=self.tb9.text[:-1]
                elif(len(self.tb8.text)>0):
                    if len(self.tb8.text)==1:
                        self.tb8.active=False
                        self.tb7.active=True
                    self.tb8.text=self.tb8.text[:-1]
                elif(len(self.tb7.text)>0):
                    if len(self.tb7.text)==1:
                        self.tb7.active=False
                        self.tb6.active=True
                    self.tb7.text=self.tb7.text[:-1]
                elif(len(self.tb6.text)>0):
                    if len(self.tb6.text)==1:
                        self.tb6.active=False
                        self.tb5.active=True
                    self.tb6.text = self.tb6.text[:-1]
                elif(len(self.tb5.text)>0):
                    if len(self.tb5.text)==1:
                        self.tb5.active=False
                        self.tb4.active=True
                    self.tb5.text=self.tb5.text[:-1]
                elif(len(self.tb4.text)>0):
                    self.tb4.text=self.tb4.text[:-1]
   
            elif event.key==pygame.K_RETURN:self.active=0
            else:
                if event.key<=255:
                    if(len(self.tb4.text)<self.caracteresMaximo):
                        self.tb4.text+=chr(event.key)
                        if len(self.tb4.text)==44:
                            self.tb4.active=False
                            self.tb5.active=True
                    elif(len(self.tb5.text)<self.caracteresMaximo):
                        self.tb5.text+=chr(event.key)
                        if len(self.tb5.text)==44:
                            self.tb5.active=False
                            self.tb6.active=True
                    elif(len(self.tb6.text)<self.caracteresMaximo):
                        self.tb6.text+=chr(event.key)
                        if len(self.tb6.text)==44:
                            self.tb6.active=False
                            self.tb7.active=True
                    elif(len(self.tb7.text)<self.caracteresMaximo):
                        self.tb7.text+=chr(event.key)
                        if len(self.tb7.text)==44:
                            self.tb7.active=False
                            self.tb8.active=True
                    elif(len(self.tb8.text)<self.caracteresMaximo):
                        self.tb8.text+=chr(event.key)
                        if len(self.tb8.text)==44:
                            self.tb8.active=False
                            self.tb9.active=True
                    elif(len(self.tb9.text)<self.caracteresMaximo):
                        self.tb9.text+=chr(event.key)
                        if len(self.tb9.text)==44:
                            self.tb9.active=False
                            self.tb10.active=True
                    elif(len(self.tb10.text)<self.caracteresMaximo):
                        self.tb10.text+=chr(event.key)
                        if len(self.tb10.text)==44:
                            self.tb10.active=False
                            self.tb11.active=True
                    elif(len(self.tb11.text)<self.caracteresMaximo):
                        self.tb11.text+=chr(event.key)

class TextBox2(Widget):
    """TextBox is a widget to enter one-line text and/or as a button"""
    def __init__(self,parent=None,text="",textsize=18,color=(255,255,255),position=(0,0),size=(200,20),editable=True):
        """init TextBox
        when editable is set to False then we get a Button"""
        Widget.__init__(self,parent,position,size)
        rutaFuente = os.path.join("fuentes", "PatrickHand-Regular.ttf")
        self.font = pygame.font.Font(rutaFuente, textsize) 
        self.text=text
        self.color=color
        self.editable=editable
        self.active=False
        
    def reiniciar(self):
        self.active=False
        self.text = ""
            
    def Draw(self,screen):
        """draw TextBox to given surface"""
        image=pygame.Surface(self.size)
        prefix=""
        #if active show line |
        if self.active==True:
            prefix="|"
        
        img=self.font.render(self.text+prefix,0,self.color)
        if img.get_size()[0]>self.size[0]:
            image.blit(img,(0,0),(img.get_size()[0]-self.size[0],0,self.size[0],self.size[1]))
        else:
            image.blit(img,(0,0))
        screen.blit(image,self.pos)