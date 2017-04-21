'''
Created on 14/07/2013

@author: Luis
'''
import pygame
class Widget:
    """base class for all widgets"""
    def __init__(self,parent,pos=[0,0],size=[10,10]):
        """init widget """
        self.pos=pos[:]
        self.size=size[:]
        self.active=0
        #callbacks
        self.onClick=None
        self.onMottion=None
        self.onUnder=None
    
    def Update(self,event):
        """update widget (send events)"""
        mx,my=pygame.mouse.get_pos()
        if self.IsUnder((mx,my))==True:
            if self.onUnder!=None:
                self.onUnder(self)
            if self.onClick!=None and event.type==pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]==1:
                self.onClick(self)
                
    def IsUnder(self,point):
        """check is point is under widget
        return True if under , otherwise False"""
        mousex,mousey=point
        if mousex>=self.pos[0] and mousex<=self.pos[0]+self.size[0] and mousey>=self.pos[1] and mousey<=self.pos[1]+self.size[1]:
            return True
        else:return False
    
    def Connect(self,signal,function):
        """Connect event to function
        check constans module for signals IDs"""
        if signal==0:self.onClick=function
        if signal==1:self.onMottion=function
        if signal==2:self.onUnder=function