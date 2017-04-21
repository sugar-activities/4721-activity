'''
Created on 14/07/2013

@author: Luis
'''

import pygame
from pygame.locals import *
from widget import Widget

class TextBox(Widget):
    """TextBox is a widget to enter one-line text and/or as a button"""
    def __init__(self,parent=None,text="",textsize=18,color=(255,255,255),position=(0,0),size=(200,20),editable=True):
        """init TextBox
        when editable is set to False then we get a Button"""
        Widget.__init__(self,parent,position,size)
        self.font=pygame.font.SysFont("monospace",textsize)
        self.text=text
        self.color=color
        self.editable=editable
        self.active=False
        
    def reiniciar(self):
        self.active=False
        self.text = ""

    def Event(self,event):
        """event handler for TextBox"""
        mx,my=pygame.mouse.get_pos()
        #changeing active status
        
        if self.IsUnder((mx,my)) and event.type==pygame.MOUSEBUTTONDOWN and self.editable==True:
            if pygame.mouse.get_pressed()[0]==1:
                self.active=True
        elif event.type==pygame.MOUSEBUTTONDOWN:
            self.active=False
        #keyboard events1
        if self.active==True and event.type==pygame.KEYDOWN:
            if event.key==pygame.K_BACKSPACE:self.text=self.text[:-1]
            elif event.key==pygame.K_RETURN:self.active=0
            else:
                if event.key<=255:self.text+=chr(event.key)
        
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