'''
Created on 14/07/2013

@author: Luis
'''
import pygame, os

class BotonEnviar(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load(os.path.join("imagenes", "compartir", "botonEnviar.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (870,590)